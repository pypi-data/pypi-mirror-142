# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bible_cli']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27.1,<3.0.0', 'rich>=12.0.0,<13.0.0', 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['bible-cli = bible_cli.app:app']}

setup_kwargs = {
    'name': 'bible-cli',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Ian Kollipara',
    'author_email': 'ian.kollipara@cune.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
