# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['urdf2casadi', 'urdf2casadi.geometry']

package_data = \
{'': ['*']}

install_requires = \
['casadi==3.5.5',
 'numpy>=1.15.0,<2.0.0',
 'pytest>=6.2.5,<7.0.0',
 'urdf_parser_py>=0.0.3']

setup_kwargs = {
    'name': 'urdf2casadi',
    'version': '1.2.0',
    'description': 'Module for tuning a chain in a URDF to a casadi function.',
    'long_description': None,
    'author': 'Mathias Hauan Arbo',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.0',
}


setup(**setup_kwargs)
