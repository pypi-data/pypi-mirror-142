# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['byugrid']
setup_kwargs = {
    'name': 'byugrid',
    'version': '0.1.1',
    'description': '2D grid, used for teaching people how to program',
    'long_description': None,
    'author': 'Daniel Zappala',
    'author_email': 'daniel.zappala@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
