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
"""Miscellaneous utils module."""

import sys
from argparse import ArgumentParser
from configparser import ConfigParser
from contextlib import contextmanager
from distutils.util import strtobool
from functools import wraps
from importlib import import_module
from importlib.resources import files
from logging import CRITICAL, NOTSET, disable, getLogger
from logging.config import dictConfig
from os import R_OK, W_OK, access, mkdir, path
from pathlib import Path
from shutil import copyfile
from threading import current_thread

from .. import __version__
from .. import settings as sett
from ..migrate import migrate
from .exceptions import InterruptException

LOGGER = getLogger(__name__)


def handle_keyboardinterrupt(func):
    """Handle KeyboardInterrupt by raising an InterruptException."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            print('\nKeyboard interrupt detected.')
            raise InterruptException from None

    return wrapper


def handle_thread(func):
    """Add and remove async threads from global list."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        sett.THREADS.append(current_thread())
        try:
            res = func(*args, **kwargs)
            sett.THREADS.remove(current_thread())
            return res
        except Exception as exc:
            sett.THREADS.remove(current_thread())
            raise exc

    return wrapper


@contextmanager
def disable_logger():
    """Disable logging.

    Warning: do not nest calls to this method.
    """
    disable(CRITICAL)
    try:
        yield
    finally:
        disable(NOTSET)


def copy_config_sample(interactive):
    """Copy (or ask to copy) config.sample and exit."""
    if interactive:
        copy = str2bool(input(
            'Missing configuration file, do you want a copy of '
            'config.sample in the specified location '
            f'({sett.CONFIG})? [Y/n] '),
                        force_true=True)
        if not copy:
            die("You'll need to manually create a configuration file")
    else:
        LOGGER.error(
            "Missing config file, copying sample to '%s', "
            'read doc/configuring.md for details', sett.CONFIG)
    sample = files(sett.PKG_NAME).joinpath('share/config.sample')
    try:
        copyfile(sample, sett.CONFIG)
    except OSError as err:
        die('Error copying sample file: ' + str(err))
    die('Please configure boltlight')


def die(message=None, exit_code=1):
    """Print message to stderr and exit with the requested error code."""
    if message:
        sys.stderr.write(message + '\n')
    sys.exit(exit_code)


def get_config_parser(interactive=False):
    """Read config file, set default values and return a config parser.

    When config is missing, copy config.sample in its expected location and
    terminate.
    """
    sett.CONFIG = path.join(sett.DATA, sett.CONFIG_NAME)
    if not path.exists(sett.CONFIG):
        copy_config_sample(interactive)
    config = ConfigParser()
    config.read(sett.CONFIG)
    l_values = [
        'INSECURE_CONNECTION', 'PORT', 'SERVER_KEY', 'SERVER_CRT', 'LOGS_DIR',
        'LOGS_LEVEL', 'DB_DIR', 'MACAROONS_DIR', 'DISABLE_MACAROONS'
    ]
    set_defaults(config, l_values)
    return config


def get_path(ipath, base_path=None):
    """Get absolute posix path.

    By default relative paths are calculated from boltlightdir.
    """
    ipath = Path(ipath).expanduser()
    if ipath.is_absolute():
        return ipath.as_posix()
    if not base_path:
        base_path = sett.DATA
    return Path(base_path, ipath).as_posix()


def handle_importerror(err):
    """Handle an ImportError."""
    LOGGER.debug('Import error: %s', str(err))
    LOGGER.error("Implementation '%s' is not supported", sett.IMPLEMENTATION)
    die()


def handle_sigterm(_signo, _stack_frame):
    """Handle a SIGTERM by raising an InterruptException."""
    raise InterruptException


def init_common(help_msg, core=True, write_perms=False, runtime=False):
    """Initialize common entrypoints calls."""
    _update_logger()
    _parse_args(help_msg, write_perms)  # updates sett.DATA
    if write_perms:
        if not access(sett.DATA, W_OK):
            raise RuntimeError('Permission denied on ' + sett.DATA)
    _init_tree()
    config = get_config_parser()  # updates sett.CONFIG
    _update_logger(config)
    _get_start_options(config, runtime)
    if core:
        migrate()
        # reupdating logger as migrate overrides configuration
        _update_logger(config)


def _update_logger(config=None):
    """Activate console logs.

    When configuration is available, activate file logs and set configured log
    level.
    """
    if config:
        sec = 'boltlight'
        logs_level = config.get(sec, 'LOGS_LEVEL').upper()
        sett.LOGGING['handlers']['console']['level'] = logs_level
        sett.LOGGING['loggers']['']['handlers'].append('file')
        sett.LOGGING['handlers'].update(sett.LOGGING_FILE)
        sett.LOGS_DIR = get_path(config.get(sec, 'LOGS_DIR'))
        log_path = path.join(sett.LOGS_DIR, sett.LOGS_BOLTLIGHT)
        sett.LOGGING['handlers']['file']['filename'] = log_path
    try:
        dictConfig(sett.LOGGING)
    except (AttributeError, ImportError, TypeError, ValueError) as err:
        raise RuntimeError('Logging configuration error: ' +
                           str(err)) from None
    getLogger('urllib3').propagate = False


def _parse_args(help_msg, write_perms):
    """Parse command line arguments."""
    parser = ArgumentParser(description=help_msg)
    acc_mode = R_OK
    if write_perms:
        acc_mode = W_OK
    parser.add_argument('--boltlightdir',
                        metavar='PATH',
                        help="Path containing config file and other data")
    args = vars(parser.parse_args())
    if 'boltlightdir' in args and args['boltlightdir'] is not None:
        boltlightdir = args['boltlightdir']
        if not boltlightdir:
            raise RuntimeError('Invalid boltlightdir: empty path')
        if not path.isdir(boltlightdir):
            raise RuntimeError('Invalid boltlightdir: path is not a directory')
        if not access(boltlightdir, acc_mode):
            raise RuntimeError('Invalid boltlightdir: permission denied')
        sett.DATA = boltlightdir


def _init_tree():
    """Create data directory tree if missing."""
    _try_mkdir(sett.DATA)
    _try_mkdir(path.join(sett.DATA, 'certs'))
    _try_mkdir(path.join(sett.DATA, 'db'))
    _try_mkdir(path.join(sett.DATA, 'logs'))
    _try_mkdir(path.join(sett.DATA, 'macaroons'))


def _try_mkdir(dir_path):
    """Create a directory if it doesn't exist."""
    if not path.exists(dir_path):
        LOGGER.info('Creating dir %s', dir_path)
        mkdir(dir_path)


def _get_start_options(config, runtime):
    """Set boltlight and implementation start options."""
    sec = 'boltlight'
    sett.IMPLEMENTATION = config.get(sec, 'IMPLEMENTATION').lower()
    sett.INSECURE_CONNECTION = str2bool(config.get(sec, 'INSECURE_CONNECTION'))
    sett.DISABLE_MACAROONS = str2bool(config.get(sec, 'DISABLE_MACAROONS'))
    sett.PORT = config.get(sec, 'PORT')
    sett.LISTEN_ADDR = f'{sett.HOST}:{sett.PORT}'
    if sett.INSECURE_CONNECTION:
        sett.DISABLE_MACAROONS = True
    sett.SERVER_KEY = get_path(config.get(sec, 'SERVER_KEY'))
    sett.SERVER_CRT = get_path(config.get(sec, 'SERVER_CRT'))
    if sett.DISABLE_MACAROONS:
        LOGGER.warning('Disabling macaroons is not safe, '
                       'do not disable them in production')
    sett.MACAROONS_DIR = get_path(config.get(sec, 'MACAROONS_DIR'))
    sett.DB_DIR = get_path(config.get(sec, 'DB_DIR'))
    sett.DB_PATH = path.join(sett.DB_DIR, sett.DB_NAME)
    # Checks if implementation is supported, could throw an ImportError
    module = import_module(f'...light_{sett.IMPLEMENTATION}', __name__)
    if runtime:
        getattr(module, 'get_settings')(config, sett.IMPLEMENTATION)


def set_defaults(config, values):
    """Set configuration defaults."""
    defaults = {}
    for var in values:
        defaults[var] = getattr(sett, var)
    config.read_dict({'DEFAULT': defaults})


def str2bool(string, force_true=False):
    """Cast a string to boolean, forcing to a default value."""
    try:
        return strtobool(str(string).lower())
    except ValueError:
        return force_true
