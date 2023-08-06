# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pyconfmanager']
setup_kwargs = {
    'name': 'pyconfmanager',
    'version': '1.0.0',
    'description': 'Simple lib to read configs',
    'long_description': None,
    'author': 'Xenely',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
