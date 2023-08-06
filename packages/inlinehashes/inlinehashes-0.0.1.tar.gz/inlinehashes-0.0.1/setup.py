# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['inlinehashes']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.10.0,<5.0.0', 'requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['inlinehashes = inlinehashes.app:run_cli']}

setup_kwargs = {
    'name': 'inlinehashes',
    'version': '0.0.1',
    'description': 'Hash generator for HTML inline styles and scripts',
    'long_description': None,
    'author': 'Gonçalo Valério',
    'author_email': 'gon@ovalerio.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dethos/inlinehashes',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
