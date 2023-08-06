# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['composer']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=4.1.1,<5.0.0']

setup_kwargs = {
    'name': 'class-composer',
    'version': '0.1.0',
    'description': 'A library for making dataclasses',
    'long_description': None,
    'author': 'andy',
    'author_email': 'andy.development@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
