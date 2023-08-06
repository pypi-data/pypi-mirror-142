# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blitskrieg_proto']

package_data = \
{'': ['*']}

install_requires = \
['grpcio>=1.43.0,<2.0.0', 'protobuf>=3.19.1,<4.0.0']

setup_kwargs = {
    'name': 'blitskrieg-proto',
    'version': '0.2.0',
    'description': 'Protobuf generated libraries for Blitskrieg',
    'long_description': None,
    'author': 'Hashbeam',
    'author_email': 'hashbeam@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/hashbeam/blitskrieg-proto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
