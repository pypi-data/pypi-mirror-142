# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dockerensure']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dockerensure',
    'version': '0.0.1',
    'description': 'Ensure that Docker images are ready for use',
    'long_description': 'todo',
    'author': 'ubuntom',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ubuntom/dockerensure',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
