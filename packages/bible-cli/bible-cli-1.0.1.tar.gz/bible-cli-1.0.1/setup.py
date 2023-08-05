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
    'version': '1.0.1',
    'description': 'A Bible query command line tool',
    'long_description': "# Bible Cli\n\n## Description\n\nThis simple CLI tool allows the user to query 5-6 translations of the Bible. It is built on \nTim Morgan's [Bible API](https://bible-api.com/). The primary packages used are:\n- Typer\n- Rich\n- Requests\n\n## Usage\n\n```\nUsage: bible-cli [OPTIONS] BOOK CHAPTER\n\nArguments:\n  BOOK     The book of the bible  [required]\n  CHAPTER  The chapter(s) to select. Ex: 1; 1-2  [required]\n\nOptions:\n  --verses TEXT                   The verse range. Ex: 1-10\n  --translation [cherokee|bbe|kjv|web|oeb-cw|webbe|oeb-us|clementine|almeida|rccv]\n                                  Translation to use  [default:\n                                  Translation.WEB]\n  --install-completion [bash|zsh|fish|powershell|pwsh]\n                                  Install completion for the specified shell.\n  --show-completion [bash|zsh|fish|powershell|pwsh]\n                                  Show completion for the specified shell, to\n                                  copy it or customize the installation.\n  --help                          Show this message and exit.\n  ```\n\n### Example\n\n```\nbible-cli john 3 --verses 3 --translation kjv\n\nReference: John 3:15\nTranslation: King James Version\n 15 ┃ That whosoever believeth in him should not perish, but have eternal life. \n```",
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
