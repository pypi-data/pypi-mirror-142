# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['metabase_manager', 'metabase_manager.cli']

package_data = \
{'': ['*']}

install_requires = \
['metabase-python>=0.3.0,<0.4.0']

entry_points = \
{'console_scripts': ['metabase-manager = metabase_manager.cli.main:cli']}

setup_kwargs = {
    'name': 'metabase-manager',
    'version': '0.1.2',
    'description': 'Manage your Metabase instance programmatically.',
    'long_description': '# metabase-manager\n\nManage your Metabase instance programmatically.\n',
    'author': 'Charles Lariviere',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chasleslr/metabase-manager',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
