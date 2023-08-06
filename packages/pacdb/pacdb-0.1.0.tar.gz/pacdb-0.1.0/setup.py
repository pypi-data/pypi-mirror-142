# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pacdb']
install_requires = \
['zstandard']

setup_kwargs = {
    'name': 'pacdb',
    'version': '0.1.0',
    'description': 'Pure-python module to parse and read pacman sync dbs.',
    'long_description': '# pacdb\nPure-python module to parse and read pacman sync dbs\n',
    'author': 'Jeremy Drake',
    'author_email': 'github@jdrake.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jeremyd2019/pacdb',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
