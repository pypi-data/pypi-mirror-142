# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['boltlight',
 'boltlight.migrations',
 'boltlight.migrations.versions',
 'boltlight.utils']

package_data = \
{'': ['*'], 'boltlight': ['share/*']}

install_requires = \
['alembic>=1.5.5,<2.0.0',
 'click>=8.0.4,<9.0.0',
 'googleapis-common-protos>=1.53.0,<2.0.0',
 'grpcio>=1.43.0,<2.0.0',
 'lnd-proto==0.13.3-beta.0',
 'macaroonbakery>=1.3.1,<2.0.0',
 'protobuf>=3.19.1,<4.0.0',
 'pylibscrypt>=1.8.0,<2.0.0',
 'pyln-client==0.10.1',
 'pymacaroons>=0.13.0,<0.14.0',
 'pynacl>=1.3.0,<2.0.0',
 'qrcode>=6.1,<7.0',
 'requests>=2.25.1,<3.0.0',
 'sqlalchemy>=1.3.23,<1.4.0']

entry_points = \
{'console_scripts': ['blink = boltlight.blink:entrypoint',
                     'boltlight = boltlight.boltlight:start',
                     'boltlight-pairing = boltlight.pairing:start',
                     'boltlight-secure = boltlight.secure:secure']}

setup_kwargs = {
    'name': 'boltlight',
    'version': '2.1.0',
    'description': 'Lightning Network node wrapper',
    'long_description': '# Boltlight - a BOLT-on interface to the Lightning Network\n\nBoltlight is a Lightning Network node wrapper.\n\nIt is not a LN node itself and connects to an existing node of one of the\nsupported implementations, providing a uniform interface and set of features.\nClient code that uses boltlight can thus be agnostic on which node is running\nunder the hood.\n\nThis means that the underlying LN node implementation can be\nchanged anytime with minimal intervention and no effects on client code.\n\nEach underlying implementation implements some features with "little"\ndifferences. Boltlight strives to keep a uniform interface at all times,\ndrawing a common line where implementations differ and always choosing to stay\nBOLT-compliant as much as possible.\n\nLAPP developers should be free to code, without the need to lock-in to any\nparticular implementation.\n\n\n### Supported LN implementations :zap:\n\nCurrently, the main LN implementations <sup>1</sup> are supported:\n\n- [c-lightning](https://github.com/ElementsProject/lightning)\n  (v0.10.1) by Blockstream\n- [eclair](https://github.com/ACINQ/eclair) (v0.6.1) by Acinq\n- [electrum](https://github.com/spesmilo/electrum) (v4.1.5)\n  by Thomas Voegtlin\n- [lnd](https://github.com/lightningnetwork/lnd) (v0.13.3-beta) by Lightning\n  Labs\n\n### How it works\n\nOn the client side, boltlight exposes a gRPC client interface, by default on\nport 1708. On the node side, it proxies all the received calls to the\nunderlying implementation, using the appropriate transport and authentication\nto connect and applying the appropriate format and data translations to each\nimplemented call.\n\nSee [Supported APIs](/doc/supported_apis.md) for a table of the supported calls\nfor each implementation.\n\nCalls that are not yet implemented return an `UNIMPLEMENTED` error.\n\nSoftware dependencies and configurations are the only significant differences\nbetween the supported implementations.\n\nSee [Implementation Specific](/doc/implementation_specific.md) for an\nincomplete list of configuration tips and nuances that are dependent on the\nparticular lightning implementation.\n\n\n#### Notes\n1. _at the moment, only the specified versions of the LN nodes are supported_\n\n\n## Requirements\n\nFirst of all, boltlight will need to connect to an existing and supported LN\nnode.\n\nIn order to run boltlight it needs to be configured and software dependencies\nhave to be met. Some dependencies and configuration choices are determined by\nthe implementation of choice. Availability of the required dependencies will be\nchecked at runtime.\n\nThe supported architectures are `amd64` and `arm32v7`. The latter may require\nadditional dependencies.\n\n\n### System dependencies\n\n- Linux <sup>1,2</sup>\n- Python 3.9+ <sup>3</sup>\n- [optional] libscrypt 1.8+ (_faster start_)\n\n### Resources\n\nResource demand should be pretty low:\n\n- CPU: 1 core\n- RAM: ~64MB when idling\n- disk: docker image weights ~350MB\n\n#### Notes\n\n1. _tested on Debian 10 Buster_\n2. _macOS should work but is not well tested, Windows may work but is not\n   actively supported_\n3. _tested with python 3.9+_\n\n\n## Installing\n\nBoltlight can be installed with:\n```\n$ pip install boltlight\n```\n\nUsage of a `virtualenv` is recommended.\n\n\n## Configuring and securing\n\nBoltlight needs to be configured before it can connect to a LN node and make\nitself useful. [Configuring](/doc/configuring.md) contains all the instructions\non how to configure boltlight.\n\nOne last step is necessary after configuration is complete: security.\n\nOn the node side, as with configuration, this partially depends on the chosen\nimplementation. On the client side, authorization is handled with gRPC\nmacaroons.\n\nFor faster setup and execution, TLS and macaroons can be turned off. This is\nnot suitable for production use but can be useful for testing or development.\n\nTo configure the necessary secrets and set a password to manage and protect\nthem run:\n```bash\n$ boltlight-secure\n```\n\nIt can be run interactively or unattended and will create or update boltlight\'s\ndatabase and macaroon files.\n\nAll secrets will be encrypted and stored in the database, so they won\'t be\naccessible at rest. Secrets are decrypted with boltlight\'s password as part\nof the unlocking process, will only be available to boltlight at runtime and\nare never written to disk in plaintext.\n\nPlease read [Security](/doc/security.md) for all the details.\n\n\n## Using\n\n### Running\n\nTo start boltlight run:\n```bash\n$ boltlight\n```\n\nThis will start its gRPC server, through which Boltlight can be operated.\n\nThe `boltlight.proto` defines the structure for the data to be serialized\nand can be found [here](/boltlight/boltlight.proto).\ngRPC client libraries for supported languages can be generated from this file.\nSee the [Generation instructions](/doc/client_libraries.md) for more\ninformation.\n\nThe proto file contains three services: _Unlocker_, _Lightning_ and _Locker_.\nThe first does not require macaroon authorization and can only unlock\nboltlight, the other two start after boltlight is unlocked, require\nauthorization and provide all the supported operations, locking included.\n\n### API documentation\n\nDocumentation for the gRPC APIs along with example code in Python, Go,\nNode.js and Bash can be found at\n[API page](https://hashbeam.gitlab.io/boltlight/).\n\n### CLI\n\nA CLI named `blink`, with bash and zsh completion support, is available for\ninteractive usage, maintenance or testing.\n\nTo activate completion support add the appropriate line to your shell\'s RC\nfile:\n- `~/.bashrc`: `. /path/to/installed/boltlight/share/complete-blink.bash`\n- `~/.zshrc`: `. /path/to/installed/boltlight/share/complete-blink.zsh`\n\nFor a full list of the available CLI commands use the `--help` option:\n```bash\n$ blink --help\n```\n\n### Pairing\n\nTo **pair** boltlight with a client, run:\n```bash\n$ boltlight-pairing\n```\n\nThis will generate two URIs that allow easy retrieval of connection data\n(`boltlightconnect://<host>:<port>[?cert=<PEM certificate>]`)\nand macaroon (`macaroon:<chosen macaroon>`).\nThe URIs can be displayed as QR codes, suitable for easy reading from client\napps, or as text for easy copying.\n\nThe [Globular](https://gitlab.com/hashbeam/globular) Android wallet is an\nexample app that supports pairing with boltlight.\n\n\n## The fork\n\nBoltlight has been forked from [Lighter](https://gitlab.com/inbitcoin/lighter)\nand continues on the same path, aiming to:\n- make it easier to get started\n- add support for more implementations\n- keep the existing support up-to-date\n- add more features\n\nBoltlight is not 100% backwards-compatible with Lighter because of the name\nchange, so a re-configuration is needed in order to upgrade.\n\n\n## Contributing\n\nAll contributions are welcome!\n\nIf you\'re a developer and want to get involved, see\n[CONTRIBUTING.md](/CONTRIBUTING.md) for info on how to join the effort.\n\nIf boltlight is missing that key feature you need, please get in touch.\nFeel free to open issues to request new features or report bugs, or send an\nemail to `hashbeam@protonmail.com`.\n\n',
    'author': 'Hashbeam',
    'author_email': 'hashbeam@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://hashbeam.gitlab.io/boltlight',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
