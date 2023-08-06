# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['molting']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'molting',
    'version': '0.1.0',
    'description': 'Automatically bump your python project files to the latest version.',
    'long_description': None,
    'author': 'Lucas Melin',
    'author_email': 'lucas.melin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
