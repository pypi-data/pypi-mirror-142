# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['torch_persistency']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'torch-model-persistency',
    'version': '0.1.6',
    'description': 'Module Persistency manager for PyTorch',
    'long_description': None,
    'author': 'Oguz Vuruskaner',
    'author_email': 'ovuruska@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
