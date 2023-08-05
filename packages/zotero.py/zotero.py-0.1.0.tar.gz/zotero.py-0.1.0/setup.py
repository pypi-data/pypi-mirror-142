# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['zotero']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'zotero.py',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Tiago Vilela',
    'author_email': 'tiagovla@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
