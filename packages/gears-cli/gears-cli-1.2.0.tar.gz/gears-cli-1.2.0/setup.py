# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gears_cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1,<9.0.0', 'redis>=4.1.4,<5.0.0']

entry_points = \
{'console_scripts': ['gears-cli = gears_cli.__main__:main']}

setup_kwargs = {
    'name': 'gears-cli',
    'version': '1.2.0',
    'description': 'RedisGears cli',
    'long_description': '[![license](https://img.shields.io/github/license/RedisGears/gears-cli.svg)](https://github.com/RedisGears/gears-cli)\n[![PyPI version](https://badge.fury.io/py/gears-cli.svg)](https://badge.fury.io/py/gears-cli)\n[![CircleCI](https://circleci.com/gh/RedisGears/gears-cli/tree/master.svg?style=svg)](https://circleci.com/gh/RedisGears/gears-cli/tree/master)\n[![Releases](https://img.shields.io/github/release/RedisGears/gears-cli.svg)](https://github.com/RedisGears/gears-cli/releases/latest)\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/RedisGears/gears-cli.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/RedisGears/gears-cli/context:python)\n [![Known Vulnerabilities](https://snyk.io/test/github/RedisGears/gears-cli/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/RedisGears/gears-cli?targetFile=requirements.txt) \n\n# gears-cli\nSimple cli that allows the send python code to RedisGears\n\n## Install\n```python\npip install gears-cli\n```\n\n## Install latest code \n\n```python\npip install git+https://github.com/RedisGears/gears-cli.git\n```\n\n## Usage\n```\n> gears-cli --help\nUsage: gears-cli [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  export-requirements   Export requirements from RedisGears\n  import-requirements   Import requirements to RedisGears\n  install-requirements  Install give requirements\n  run                   Run gears function\n\n\n> gears-cli run --help\nUsage: gears-cli run [OPTIONS] FILEPATH [EXTRA_ARGS]...\n\n  Run gears function\n\nOptions:\n  --host TEXT               Redis host to connect to\n  --port INTEGER            Redis port to connect to\n  --user TEXT               Redis acl user\n  --password TEXT           Redis password\n  --ssl BOOLEAN             Use ssl\n  --ssl-password TEXT       Passphrase for ssl key\n  --ssl-keyfile TEXT        Path to ssl key file\n  --ssl-certfile TEXT       Path to ssl certificate file\n  --ssl-ca-certs TEXT       Path to ssl ca certificate file\n  --ssl-verify-ca BOOLEAN   Whether or not to us CA to verify certs\n  --requirements TEXT       Path to requirements.txt file\n  --help                    Show this message and exit.\n\n> gears-cli export-requirements --help\nUsage: gears-cli export-requirements [OPTIONS]\n\n  Export requirements from RedisGears\n\nOptions:\n  --host TEXT             Redis host to connect to\n  --port INTEGER          Redis port to connect to\n  --user TEXT             Redis acl user\n  --password TEXT         Redis password\n  --ssl BOOLEAN           Use ssl\n  --ssl-password TEXT     Passphrase for ssl key\n  --ssl-keyfile TEXT      Path to ssl key file\n  --ssl-certfile TEXT     Path to ssl certificate file\n  --ssl-ca-certs TEXT     Path to ssl ca certificate file\n  --ssl-verify-ca BOOLEAN Whether or not to us CA to verify certs\n  --save-directory TEXT   Directory for exported files\n  --output-prefix TEXT    Prefix for the requirement zip file\n  --registration-id TEXT  Regisrations ids to extract their requirements\n  --requirement TEXT      Requirement to export\n  --all                   Export all requirements\n  --help                  Show this message and exit.\n\n> gears-cli import-requirements --help\nUsage: gears-cli import-requirements [OPTIONS] [REQUIREMENTS]...\n\n  Import requirements to RedisGears\n\nOptions:\n  --host TEXT               Redis host to connect to\n  --port INTEGER            Redis port to connect to\n  --user TEXT               Redis acl user\n  --password TEXT           Redis password\n  --ssl BOOLEAN             Use ssl\n  --ssl-password TEXT       Passphrase for ssl key\n  --ssl-keyfile TEXT        Path to ssl key file\n  --ssl-certfile TEXT       Path to ssl certificate file\n  --ssl-ca-certs TEXT       Path to ssl ca certificate file\n  --ssl-verify-ca BOOLEAN   Whether or not to us CA to verify certs\n  --requirements-path TEXT  Path of requirements directory containing\n                            requirements zip files, could also be a zip file\n                            contains more requirements zip files\n  --all                     Import all requirements in zip file\n  --bulk-size INTEGER       Max bulk size to send to redis in MB\n  --help                    Show this message and exit.\n\n> gears-cli install-requirements --help\nUsage: gears-cli install-requirements [OPTIONS] [REQUIREMENTS]...\n\n  Install give requirements\n\nOptions:\n  --host TEXT               Redis host to connect to\n  --port INTEGER            Redis port to connect to\n  --user TEXT               Redis acl user\n  --password TEXT           Redis password\n  --ssl BOOLEAN             Use ssl\n  --ssl-password TEXT       Passphrase for ssl key\n  --ssl-keyfile TEXT        Path to ssl key file\n  --ssl-certfile TEXT       Path to ssl certificate file\n  --ssl-ca-certs TEXT       Path to ssl ca certificate file\n  --ssl-verify-ca BOOLEAN   Whether or not to us CA to verify certs\n  --requirements-file TEXT  Path to requirements.txt file\n  --help                    Show this message and exit.\n```\n',
    'author': 'RedisLabs',
    'author_email': 'oss@redislabs.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
