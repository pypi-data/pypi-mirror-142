# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['skytop']
install_requires = \
['requests==2.27.1']

setup_kwargs = {
    'name': 'skytop',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'SkyTop',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.sky.top/',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
