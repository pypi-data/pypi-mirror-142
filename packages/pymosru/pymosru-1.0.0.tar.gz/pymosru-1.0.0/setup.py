# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['mosru']
setup_kwargs = {
    'name': 'pymosru',
    'version': '1.0.0',
    'description': '',
    'long_description': None,
    'author': 'yer7700',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
