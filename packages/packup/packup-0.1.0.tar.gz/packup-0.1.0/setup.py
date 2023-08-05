# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['docs', 'packup', 'tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'packup',
    'version': '0.1.0',
    'description': 'A full-fledged Python/C-Extension packaging frontend for humans',
    'long_description': None,
    'author': 'Adam Hendry',
    'author_email': 'adam.grant.hendry@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
