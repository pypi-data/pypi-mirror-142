# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['abi_ds_utils']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.21.14,<2.0.0']

setup_kwargs = {
    'name': 'abi-ds-utils',
    'version': '0.1.1',
    'description': 'Utility modules for working with mlflow, containers, aws and many more.',
    'long_description': None,
    'author': 'Martin Matousek',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.8',
}


setup(**setup_kwargs)
