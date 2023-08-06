# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['proto', 'proto.message']

package_data = \
{'': ['*']}

install_requires = \
['PySocks>=1.7.1,<2.0.0',
 'base58>=2.1.1,<3.0.0',
 'bitstring>=3.1.9,<4.0.0',
 'coincurve>=17.0.0,<18.0.0',
 'cryptography>=36.0.1,<37.0.0']

setup_kwargs = {
    'name': 'pyln-proto',
    'version': '0.10.2.post1',
    'description': 'This package implements some of the Lightning Network protocol in pure python. It is intended for protocol testing and some minor tooling only. It is not deemed secure enough to handle any amount of real funds (you have been warned!).',
    'long_description': None,
    'author': 'Christian Decker',
    'author_email': 'decker.christian@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
