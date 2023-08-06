# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wordle_cheater']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=4.2,<5.0']}

entry_points = \
{'console_scripts': ['wordle-cheater = wordle_cheater.cli:wordle_cheat']}

setup_kwargs = {
    'name': 'wordle-cheater',
    'version': '0.2.1',
    'description': 'Utilities for cheating on Wordle :(',
    'long_description': '# wordle-cheater\n\n[![PyPI](https://img.shields.io/pypi/v/wordle-cheater.svg)](https://pypi.org/project/wordle-cheater/)\n[![Documentation Status](https://readthedocs.org/projects/wordle-cheater/badge/?version=latest)](https://wordle-cheater.readthedocs.io/en/latest/?badge=latest)\n[![Tests](https://github.com/edsq/wordle-cheater/workflows/Tests/badge.svg)](https://github.com/edsq/wordle-cheater/actions?workflow=Tests)\n[![codecov](https://codecov.io/gh/edsq/wordle-cheater/branch/main/graph/badge.svg?token=5G6XN19YDV)](https://codecov.io/gh/edsq/wordle-cheater)\n\n![interactive-screenshot](https://github.com/edsq/wordle-cheater/raw/main/docs/_static/wordle-cheater_interactive.png)\n\nUtitlities for cheating on Wordle :(\n\nI created `wordle-cheater` because I often like to do a post-mortem on the day\'s Wordle\nand see how the possible solutions changed with my guesses.  If you use this to\nactually cheat on Wordle, you go straight to the naughty list.\n\n[Read the documentation here.](https://wordle-cheater.readthedocs.io/en/latest/)\n\n## Installation\n\nInstall with pip or [pipx](https://pypa.github.io/pipx/):\n```console\n$ pipx install wordle-cheater\n```\n\nRequires Python >=3.7, <4.0.\n\n## Usage\n\nInvoked without arguments, `wordle-cheater` allows you to interactively enter your\nguesses.  Alternatively, you can specify your guesses on the command line like so:\n\n![cli-screenshot](https://github.com/edsq/wordle-cheater/raw/main/docs/_static/wordle-cheater_cli.png)\n\nNote that we use "b" (for "black") for letters that don\'t appear in the solution - not\n"w" for "white".  Throughout this project, we assume you are using dark mode.\n\nSee\n```console\n$ wordle-cheater --help\n```\nfor more information and options.\n',
    'author': 'Edward Eskew',
    'author_email': 'eeskew@gatech.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/edsq/wordle-cheater',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
