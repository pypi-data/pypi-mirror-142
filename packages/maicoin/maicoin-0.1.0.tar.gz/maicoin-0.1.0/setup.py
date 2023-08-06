# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['maicoin']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'websockets>=10.2,<11.0']

setup_kwargs = {
    'name': 'maicoin',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'なるみ',
    'author_email': 'weaper@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
