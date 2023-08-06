# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dunzo']

package_data = \
{'': ['*'], 'dunzo': ['sound_effects/*']}

install_requires = \
['ipython>=8.1.1,<9.0.0']

setup_kwargs = {
    'name': 'dunzo',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
