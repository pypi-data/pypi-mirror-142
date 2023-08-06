# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['s3pypi']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.9.211,<2.0.0']

entry_points = \
{'console_scripts': ['s3pypi = s3pypi.__main__:main']}

setup_kwargs = {
    'name': 's3pypi',
    'version': '1.0.0',
    'description': 'CLI for creating a Python Package Repository in an S3 bucket',
    'long_description': None,
    'author': 'Matteo De Wint',
    'author_email': 'matteo@gorilla.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
