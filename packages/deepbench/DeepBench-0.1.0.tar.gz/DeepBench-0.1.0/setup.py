# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deepbench', 'deepbench.src.deepbench', 'deepbench.tests']

package_data = \
{'': ['*'], 'deepbench': ['src/*']}

install_requires = \
['pytest-cov>=3.0.0,<4.0.0']

setup_kwargs = {
    'name': 'deepbench',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'AeRabelais',
    'author_email': 'pantagruelspendulum@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
