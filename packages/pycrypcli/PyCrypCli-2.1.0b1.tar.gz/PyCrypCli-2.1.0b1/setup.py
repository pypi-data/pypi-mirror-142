# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['PyCrypCli',
 'PyCrypCli.commands',
 'PyCrypCli.context',
 'PyCrypCli.models',
 'PyCrypCli.models.hardware_config',
 'PyCrypCli.models.network',
 'PyCrypCli.models.service',
 'PyCrypCli.models.shop',
 'PyCrypCli.models.wallet']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.0,<2.0.0',
 'pypresence>=4.2.1,<5.0.0',
 'pyreadline>=2.1,<3.0',
 'requests>=2.27.1,<3.0.0',
 'sentry-sdk>=1.5.7,<2.0.0',
 'websocket-client>=1.3.1,<2.0.0']

entry_points = \
{'console_scripts': ['pycrypcli = PyCrypCli.pycrypcli:main']}

setup_kwargs = {
    'name': 'pycrypcli',
    'version': '2.1.0b1',
    'description': 'Python Cryptic Game Client',
    'long_description': '<p>\n\n  [![CI](https://github.com/Defelo/PyCrypCli/actions/workflows/ci.yml/badge.svg)](https://github.com/Defelo/PyCrypCli/actions/workflows/ci.yml)\n  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n  [![Maintainability](https://api.codeclimate.com/v1/badges/87ffbaa8a2f8bdde057c/maintainability)](https://codeclimate.com/github/Defelo/PyCrypCli/maintainability)\n  [![PyPI](https://badge.fury.io/py/PyCrypCli.svg)](https://pypi.org/project/PyCrypCli/)\n  [![PyPI Downloads](https://img.shields.io/pypi/dm/pycrypcli.svg)](https://pypi.org/project/PyCrypCli/)\n\n</p>\n\n\n# PyCrypCli\nPython [Cryptic Game](https://github.com/cryptic-game/cryptic) Client\n\n## Prerequisites\n- [Python 3.10+](https://www.python.org/downloads/)\n\n## Install via [pip](https://pypi.org/project/PyCrypCli/)\n```\n$ python -m pip install -U PyCrypCli\n$ pycrypcli [<server>]\n```\n\n## Or clone from [GitHub](https://github.com/Defelo/PyCrypCli)\n```\n$ git clone https://github.com/Defelo/PyCrypCli.git\n$ cd PyCrypCli/\n$ python -m pip install -r requirements.txt\n$ python -m PyCrypCli [<server>]\n```\n\n## Or pull the [Docker Image](https://ghcr.io/defelo/pycrypcli)\n```\n# docker run -it --rm ghcr.io/defelo/pycrypcli\n```\n',
    'author': 'Defelo',
    'author_email': 'elodef42@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Defelo/PyCrypCli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
