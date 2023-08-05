# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datacon']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'datacon',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'limonyellow',
    'author_email': 'lemon@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/limonyellow/data_connector',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
