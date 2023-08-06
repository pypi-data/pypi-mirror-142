# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['abi_pyspark_utils']

package_data = \
{'': ['*']}

install_requires = \
['pyarrow>=7.0.0,<8.0.0', 'pyspark==3.1.1']

setup_kwargs = {
    'name': 'abi-pyspark-utils',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'PVH',
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
