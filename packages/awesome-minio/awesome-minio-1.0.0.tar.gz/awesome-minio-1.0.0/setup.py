# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['awesome_minio']

package_data = \
{'': ['*']}

install_requires = \
['minio>=7.1.1,<8.0.0', 'pandas>=1.4.1,<2.0.0', 'starlette>=0.19.0,<0.20.0']

setup_kwargs = {
    'name': 'awesome-minio',
    'version': '1.0.0',
    'description': 'minio wrapper to perform task like pandas dataframe upload, download',
    'long_description': '[![Stable Version](https://img.shields.io/pypi/v/awesome-minio?label=stable)](https://pypi.org/project/awesome-minio/)\n[![tests](https://github.com/MoBagel/awesome-minio/workflows/ci/badge.svg)](https://github.com/MoBagel/awesome-minio)\n[![Coverage Status](https://coveralls.io/repos/github/MoBagel/awesome-minio/badge.svg?branch=develop)](https://coveralls.io/github/MoBagel/awesome-minio)\n\n# Awesome Minio\n\nA library that extends minio python client to perform more complex task like read/write pandas DataFrame, json file, ...etc\n',
    'author': 'Schwannden Kuo',
    'author_email': 'schwannden@mobagel.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MoBagel/awesome-minio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
