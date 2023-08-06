# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['criptam']

package_data = \
{'': ['*']}

install_requires = \
['ipwndfu>=2.0.0b5,<2.1.0',
 'kimg4>=0.1.1,<0.2.0',
 'mwclient>=0.10.1,<0.11.0',
 'pyusb>=1.2.1,<2.0.0',
 'remotezip>=0.9.3,<0.10.0',
 'requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['criptam = criptam.__main__:main']}

setup_kwargs = {
    'name': 'criptam',
    'version': '1.0b3',
    'description': 'iOS firmware key decrypter',
    'long_description': '# Criptam\nCriptam is a tool written in Python to easily fetch decrypted [iOS bootchain](https://www.theiphonewiki.com/wiki/Bootchain) [firmware keys](https://www.theiphonewiki.com/wiki/Firmware_Keys) (excluding SEPOS) from a connected device.\n\n## Features\n- Automatically fetch decrypted bootchain firmware keys for any iOS version, no IPSW download required.\n\n## Requirements\n- A UNIX-like OS\n- An internet connection\n- A 64-bit device connected in DFU mode vulnerable to [checkm8](https://github.com/hack-different/ipwndfu)\n\n## Installation\nCriptam can be installed from [PyPI](https://pypi.org/project/criptam/), or locally (requires [poetry](https://python-poetry.org/)):\n\n    ./install.sh\n\n\n## Usage\n| Option (short) | Option (long) | Description |\n|----------------|---------------|-------------|\n| `-h` | `--help` | Shows all options avaiable |\n| `-b BUILDID` | `--buildid BUILDID` | iOS build to decrypt firmware keys for |\n| `-m MAJOR` | `--major MAJOR` | Major iOS version to decrypt all firmware keys for |\n| `-a` | `--all` | Decrypt firmware keys for all versions |\n',
    'author': 'm1stadev',
    'author_email': 'adamhamdi31@gmail.com',
    'maintainer': 'm1stadev',
    'maintainer_email': 'adamhamdi31@gmail.com',
    'url': 'https://github.com/m1stadev/Criptam',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
