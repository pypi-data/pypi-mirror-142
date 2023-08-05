# Boltlight - a LN node wrapper
#
# Copyright (C) 2021-2022 boltlight contributors
# Copyright (C) 2018 inbitcoin s.r.l.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Security operations module.

Handle implementation secrets, macaroons creation and storage.
"""

import sys
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as TimeoutErrFut
from configparser import Error as ConfigError
from contextlib import suppress
from datetime import datetime, timedelta, timezone
from getpass import getpass
from logging import CRITICAL, getLogger
from os import devnull, environ, path, remove, urandom
from select import select
from signal import SIGTERM, signal
from time import sleep, time

from sqlalchemy.exc import SQLAlchemyError

from . import settings as sett
from .macaroons import MAC_VERSION, MACAROONS, get_baker
from .utils.db import (
    init_db, is_db_ok, save_mac_params_to_db, save_secret_to_db,
    save_token_to_db, session_scope)
from .utils.exceptions import InterruptException
from .utils.misc import (
    die, handle_importerror, handle_keyboardinterrupt, handle_sigterm,
    init_common, str2bool)
from .utils.network import FakeContext
from .utils.security import Crypter, ScryptParams, check_password, get_secret

signal(SIGTERM, handle_sigterm)

LOGGER = getLogger(__name__)


def _consume_bytes(consumable, num):
    """Consume num elements from a byte string and return them."""
    consumable = list(consumable)
    i = 0
    data = []
    while i < num:
        data.append(consumable.pop(0))
        i = i + 1
    return bytes(data)


def _remove_files():
    """Remove database and macaroons."""
    LOGGER.info('Removing database and macaroons')
    with suppress(FileNotFoundError):
        remove(sett.DB_PATH)
        for file_name in MACAROONS:
            macaroon_file = path.join(sett.MACAROONS_DIR, file_name)
            remove(macaroon_file)


def _get_eclair_password():
    """Get eclair's password from stdin."""
    while True:
        data = getpass('Insert eclair password (cannot be empty): ')
        if data:
            more_data = getpass('Insert eclair password again: ')
            if data != more_data:
                die('Passwords do not match')
            return data.encode()


def _get_electrum_password():
    """Get electrum's password from stdin."""
    while True:
        data = getpass('Insert electrum password (cannot be empty): ')
        if data:
            more_data = getpass('Insert electrum password again: ')
            if data != more_data:
                die('Passwords do not match')
            return data.encode()


def _get_lnd_macaroon(mac_path=None):
    """Get lnd's macaroon from file."""
    def _read_macaroon(mac_path):
        print('Reading lnd macaroon from the provided path...')
        try:
            with open(mac_path, 'rb') as file:
                return file.read()
        except OSError as err:
            return die('Cannot read macaroon file: ' + str(err))

    if mac_path:
        return _read_macaroon(mac_path)
    mac_path = input('If your lnd instance requires a macaroon for '
                     'authorization, provide its path\nhere (filename included'
                     ', overrides current one if any) or just press enter to\n'
                     'provide none (skip) ')
    if mac_path:
        return _read_macaroon(mac_path)
    print('You have not provided a path, usage of lnd without macaroon '
          '(insecure)')
    return None


def _get_lnd_password():
    """Get lnd's password from stdin."""
    data = getpass('Insert lnd password or press enter to skip '
                   '(node unlocking will not be available): ')
    if data:
        more_data = getpass('Insert lnd password again: ')
        if data != more_data:
            die('Passwords do not match')
        return data.encode()
    return None


def _set_eclair_password(secret):
    """Handle storage of eclair's password."""
    data = None
    activate_secret = 1
    if not secret:
        data = _get_eclair_password()
    else:
        data = secret
        rm_sec = input("A password for eclair is already stored, "
                       "do you want to update it? [y/N] ")
        if str2bool(rm_sec):
            data = _get_eclair_password()
    return data, activate_secret, 'password'


def _set_electrum_password(secret):
    """Handle storage of electrum's password."""
    data = None
    activate_secret = 1
    if not secret:
        data = _get_electrum_password()
    else:
        data = secret
        rm_sec = input("A password for electrum is already stored, "
                       "do you want to update it? [y/N] ")
        if str2bool(rm_sec):
            data = _get_electrum_password()
    return data, activate_secret, 'password'


def _set_lnd_macaroon(secret):
    """Handle storage of lnd's macaroon."""
    data = None
    activate_secret = 1
    if not secret:
        data = _get_lnd_macaroon()
    else:
        data = secret
        rm_sec = input("A macaroon for lnd is already stored, "
                       "do you want to update it? [y/N] ")
        if str2bool(rm_sec):
            data = _get_lnd_macaroon()
    if data:
        res = input("Connect to lnd using its macaroon "
                    "(warning: insecure without)? [Y/n] ")
        if not str2bool(res, force_true=True):
            activate_secret = 0
    else:
        activate_secret = 0
    return data, activate_secret, 'macaroon'


def _set_lnd_password(secret):
    """Handle storage of lnd's password."""
    data = None
    activate_secret = 0
    if not secret:
        data = _get_lnd_password()
    else:
        data = secret
        rm_sec = input("A password for lnd is already stored, "
                       "do you want to update it? [y/N] ")
        if str2bool(rm_sec):
            data = _get_lnd_password()
    if data:
        activate_secret = 1
    return data, activate_secret, 'password'


def _save_token(session, password, scrypt_params):
    """Encrypt token and save it into the DB to verify password correctness."""
    derived_key = Crypter.gen_derived_key(password, scrypt_params)
    encrypted_token = Crypter.crypt(sett.ACCESS_TOKEN, derived_key)
    save_token_to_db(session, encrypted_token, scrypt_params.serialize())
    LOGGER.info('Encrypted token stored in the DB')


# pylint: disable=too-many-arguments
def _save_secret(session,
                 password,
                 scrypt_params,
                 sec_type,
                 secret,
                 activate_secret,
                 implementation=None):
    """Encrypt implementation secret and save it into the DB."""
    encrypted_secret = None
    if not implementation:
        implementation = sett.IMPLEMENTATION
    if secret:
        derived_key = Crypter.gen_derived_key(password, scrypt_params)
        encrypted_secret = Crypter.crypt(secret, derived_key)
    save_secret_to_db(session, implementation, sec_type, activate_secret,
                      encrypted_secret, scrypt_params.serialize())


# pylint: enable=too-many-arguments


def _recover_secrets(session, password):
    """Recover secrets from DB, making sure password is correct."""
    ecl_pass = lnd_mac = lnd_pass = None
    try:
        ecl_pass = get_secret(FakeContext(), session, password, 'eclair',
                              'password')
        ele_pass = get_secret(FakeContext(), session, password, 'electrum',
                              'password')
        lnd_mac = get_secret(FakeContext(), session, password, 'lnd',
                             'macaroon')
        lnd_pass = get_secret(FakeContext(), session, password, 'lnd',
                              'password')
    except RuntimeError as err:
        die(err)
    return ecl_pass, ele_pass, lnd_mac, lnd_pass


def _create_macaroons(session, password, scrypt_params):
    """Create the macaroon files."""
    print('Creating macaroons...')
    sett.MAC_ROOT_KEY = Crypter.gen_derived_key(password, scrypt_params)
    save_mac_params_to_db(session, scrypt_params.serialize())
    baker = get_baker(sett.MAC_ROOT_KEY)
    for file_name, permitted_ops in MACAROONS.items():
        macaroon_file = path.join(sett.MACAROONS_DIR, file_name)
        expiration_time = datetime.now(tz=timezone.utc) + timedelta(days=365)
        caveats = None
        mac = baker.oven.macaroon(MAC_VERSION, expiration_time, caveats,
                                  permitted_ops)
        serialized_macaroon = mac.macaroon.serialize()
        with open(macaroon_file, 'wb') as file:
            file.write(serialized_macaroon.encode())
        LOGGER.info('%s written to %s', file_name, sett.MACAROONS_DIR)


def _get_entropy():
    """Get the available entropy."""
    with open('/proc/sys/kernel/random/entropy_avail', 'r',
              encoding='utf-8') as entropy:
        entropy_available = int(entropy.read())
        return entropy_available


def _input():
    """Get an input asynchronously."""
    read_list = [sys.stdin]
    sett.FIRST_WORK_TIME = time()
    while read_list and sett.COLLECTING_INPUT:
        ready = select(read_list, [], [], 0.2)[0]
        if not ready and sett.COLLECTING_INPUT:
            _idle()
        else:
            for file in ready:
                line = file.readline()
                if not line:  # EOF, remove file from input list
                    read_list.remove(file)
                elif line.rstrip():
                    return line.rstrip()


def _idle():
    """Print periodic messages during input idling."""
    idle_msg = sett.IDLE_MESSAGES[sett.IDLE_COUNTER]
    if time() - sett.FIRST_WORK_TIME > idle_msg['delay']:
        print(idle_msg['msg'])
        if sett.IDLE_COUNTER == 3:
            idle_msg['delay'] = idle_msg['delay'] + 15
        else:
            sett.IDLE_COUNTER += 1


def _read(source, num_bytes):
    """Get entropy from /dev/random asynchronously."""
    try:
        while _get_entropy() < num_bytes * 8 * 1.2:
            if not sett.SEARCHING_ENTROPY:
                return None
            sleep(1)
        random_bytes = source.read(num_bytes)
        return random_bytes
    except IOError:
        if not sett.SEARCHING_ENTROPY:
            return None
        use_urand = input("Cannot retrieve available entropy, do you want to "
                          "use whatever your os provides\nto python's "
                          "os.urandom? [Y/n] ")
        if str2bool(use_urand, force_true=True):
            return None
        return die("No way to retrieve the amount of available entropy")


def _gen_random_data(num_bytes):  # pylint: disable=too-many-branches
    """Generate random data of key_len length."""
    unsafe_secrets = environ.get('unsafe_secrets', 0)
    if unsafe_secrets:
        return urandom(num_bytes)
    print('Trying to collect entropy...')
    future_input = None
    try:
        with open("/dev/random", "rb") as source:
            with ThreadPoolExecutor(max_workers=2) as executor:
                future_read = executor.submit(_read, source, num_bytes)
                data = future_read.result(timeout=1)
                if data:
                    return data
    except FileNotFoundError:
        use_urand = input("The blocking '/dev/random' entropy source is "
                          "not available, do you want to use\nwhatever "
                          "your os provides to python's os.urandom? "
                          "[Y/n] ")
        if str2bool(use_urand, force_true=True):
            return urandom(num_bytes)
        die("No Random Numbers Generator available")
    except TimeoutErrFut:
        print("This call might take long depending on the "
              "available entropy.\nIf this happens you can:\n"
              " - type randomly on the keyboard or move the mouse\n"
              " - install entropy collecting tools like haveged\n"
              " - install a hardware TRNG\n"
              " - type 'unsafe' and press enter to use a non-blocking "
              "entropy source; this choice will NOT be remembered for "
              "later\n")
        while future_read.running():
            if not future_input:
                future_input = executor.submit(_input)
            if future_input.done():
                if future_input.result() == 'unsafe':
                    sett.SEARCHING_ENTROPY = False
                    sett.COLLECTING_INPUT = False
                    print('Unsafe mode selected')
                    return urandom(num_bytes)
                future_input = None
            sleep(1)
        sett.COLLECTING_INPUT = False
        print("\nEnough entropy was collected, thanks for waiting")
        result = future_read.result()
        if result:
            return result
    finally:
        if source:
            source.close()
        if executor:
            executor.shutdown(wait=False)
    # should never get here
    return urandom(num_bytes)


def _gen_password(seed):
    """Generate a safe random password from a 64-char alphabet."""
    # base58 charset plus some symbols up to 64
    alpha = r'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz+/\&-_'
    assert 256 % len(alpha) == 0
    return ''.join(alpha[i % len(alpha)] for i in seed)


def _get_req_salt_len(new, interactive=True):
    """Determine the maximum bytes of salt that will be needed."""
    secrets = 1  # for boltlight's macaroons
    if sett.IMPLEMENTATION == 'eclair':
        secrets += 1  # for eclair password
    elif sett.IMPLEMENTATION == 'lnd':
        secrets += 2  # for lnd password and macaroon
    for_password = 0
    if new:
        secrets += 1  # for access token
        if interactive:
            for_password = sett.PASSWORD_LEN  # for auto-generated password
    return sett.SALT_LEN * secrets + for_password


def _db_exists():
    """Check if DB exists."""
    return path.exists(sett.DB_PATH)


def _keep_db(interactive):
    """Decide whether to keep the DB or delete it.

    In interactive mode, ask the user if he wants to delete the DB.
    Return True if the DB has been kept, False otherwise.
    """
    if not interactive:
        return True
    delete = input('Db already exists, do you want to override it? (note '
                   'this will also delete\nmacaroon files) [y/N] ')
    if str2bool(delete):
        _remove_files()
        return False
    return True


def db_config_interactive(session, new):  # pylint: disable=too-many-branches
    """Configure a new or existing database interactively."""
    ecl_pass = ele_pass = lnd_mac = lnd_pass = None
    if new:
        print('Boltlight is about to ask for a new password! As humans are '
              'really bad at\ngenerating entropy, we suggest using a password '
              'manager to generate and store\nthe password on your behalf. '
              'Refer to doc/security.md for more details.')
        gen_psw = input('Do you want boltlight to generate a safe random '
                        'password for you? (new password\nwill be printed to '
                        'stdout) [Y/n] ')
        salts_len = _get_req_salt_len(new)
        if str2bool(gen_psw, force_true=True):
            seed = _gen_random_data(sett.PASSWORD_LEN + salts_len)
            password = _gen_password(_consume_bytes(seed, sett.PASSWORD_LEN))
            print("Here is your new password:")
            print(password)
        else:
            seed = _gen_random_data(salts_len)
            password = getpass('Insert a safe password for boltlight: ')
        password_check = getpass('Save the password and then enter it '
                                 'for verification: ')
        if password != password_check:
            _remove_files()
            die("Passwords do not match")
        scrypt_params = ScryptParams(_consume_bytes(seed, sett.SALT_LEN))
        _save_token(session, password, scrypt_params)
    else:
        if not is_db_ok(session, configuring=True):
            die('Detected an incomplete configuration. Delete database.')
        password = getpass("Insert boltlight's password: ")
        try:
            check_password(FakeContext(), session, password)
        except RuntimeError:
            die('Wrong password')
        ecl_pass, ele_pass, lnd_mac, lnd_pass = _recover_secrets(
            session, password)
        seed = _gen_random_data(_get_req_salt_len(new))
    create_mac = input('Do you want to create macaroons (warning: generated '
                       'files should not be kept in\nthis host)? [y/N] ')
    if str2bool(create_mac):
        scrypt_params = ScryptParams(_consume_bytes(seed, sett.SALT_LEN))
        _create_macaroons(session, password, scrypt_params)
    secrets = []
    if sett.IMPLEMENTATION == 'eclair':
        secrets = [_set_eclair_password(ecl_pass)]
    if sett.IMPLEMENTATION == 'electrum':
        secrets = [_set_electrum_password(ele_pass)]
    if sett.IMPLEMENTATION == 'lnd':
        secrets = [_set_lnd_macaroon(lnd_mac), _set_lnd_password(lnd_pass)]
    if secrets:  # user gave us secrets to encrypt and save
        for secret in secrets:
            scrypt_params = ScryptParams(_consume_bytes(seed, sett.SALT_LEN))
            _save_secret(session, password, scrypt_params, secret[2],
                         secret[0], secret[1])


def db_config_non_interactive(session, new, password):
    """Configure a new or existing database in batch-mode."""
    ecl_pass = ele_pass = lnd_mac = lnd_pass = None
    if new:
        salts_len = _get_req_salt_len(new, interactive=False)
        seed = _gen_random_data(salts_len)
        scrypt_params = ScryptParams(_consume_bytes(seed, sett.SALT_LEN))
        _save_token(session, password, scrypt_params)
    else:
        if not is_db_ok(session):
            die('Detected an incomplete configuration. Delete database.')
        try:
            check_password(FakeContext(), session, password)
        except RuntimeError:
            die('Wrong password')
        ecl_pass, ele_pass, lnd_mac, lnd_pass = \
            _recover_secrets(session, password)
        seed = _gen_random_data(_get_req_salt_len(new, interactive=False))
    create_mac = environ.get('create_macaroons', 0)
    if create_mac:
        scrypt_params = ScryptParams(_consume_bytes(seed, sett.SALT_LEN))
        _create_macaroons(session, password, scrypt_params)
    secrets = []
    ecl_pass = environ.get('eclair_password')
    ele_pass = environ.get('electrum_password')
    lnd_mac = environ.get('lnd_macaroon')
    lnd_pass = environ.get('lnd_password')
    if ecl_pass:
        secrets.append([ecl_pass.encode(), 1, 'password', 'eclair'])
    if ele_pass:
        secrets.append([ele_pass.encode(), 1, 'password', 'electrum'])
    if lnd_mac:
        secrets.append([_get_lnd_macaroon(lnd_mac), 1, 'macaroon', 'lnd'])
    if lnd_pass:
        secrets.append([lnd_pass.encode(), 1, 'password', 'lnd'])
    if secrets:  # user gave us secrets to encrypt and save
        for secret in secrets:
            scrypt_params = ScryptParams(_consume_bytes(seed, sett.SALT_LEN))
            _save_secret(session,
                         password,
                         scrypt_params,
                         secret[2],
                         secret[0],
                         secret[1],
                         implementation=secret[3])


def secure():
    """Secure entrypoint."""
    try:
        _secure()
    except ImportError as err:
        handle_importerror(err)
    except RuntimeError as err:
        die(str(err))
    except ConfigError as err:
        err_msg = ''
        if str(err):
            err_msg = str(err)
        die('Configuration error: ' + err_msg)
    except SQLAlchemyError as err:
        err_msg = ''
        if str(err):
            err_msg = str(err)
        die('DB error: ' + err_msg)
    except InterruptException:
        sett.COLLECTING_INPUT = False
        sett.SEARCHING_ENTROPY = False
        if not sett.DONE and sett.NEW_DB:
            _remove_files()
        die()


@handle_keyboardinterrupt
def _secure():
    """Handle boltlight and implementation secrets."""
    getLogger(sett.PKG_NAME + '.errors').setLevel(CRITICAL)
    boltlight_password = environ.get('boltlight_password')
    try:
        if boltlight_password:
            # pylint: disable=consider-using-with
            sys.stdout = open(devnull, 'w', encoding='utf-8')
            # pylint: enable=consider-using-with
        init_common("Start boltlight's secure procedure", write_perms=True)
        if not _db_exists():
            sett.NEW_DB = True
        elif not _keep_db(not boltlight_password):
            sett.NEW_DB = True
        init_db(new_db=sett.NEW_DB)
        with session_scope(FakeContext()) as session:
            if boltlight_password:
                db_config_non_interactive(session, sett.NEW_DB,
                                          boltlight_password)
            else:
                db_config_interactive(session, sett.NEW_DB)
        sett.DONE = True
        print('All done!')
    finally:
        if boltlight_password:
            sys.stdout.close()
