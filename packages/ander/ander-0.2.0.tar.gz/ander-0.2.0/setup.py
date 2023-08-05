# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ander']

package_data = \
{'': ['*']}

install_requires = \
['fire']

entry_points = \
{'console_scripts': ['ander = ander.cli:main']}

setup_kwargs = {
    'name': 'ander',
    'version': '0.2.0',
    'description': 'A CLI tool to identify elements that are contained in both file',
    'long_description': '# ander: A CLI tool to identify elements that are contained in both file\n\n![PyPi ver](https://img.shields.io/pypi/v/ander?style=flat-square)\n![LICENSE budge](https://img.shields.io/github/license/joe-yama/ander?style=flat-square)\n\n## Basic Usage\n\n```bash\n$ cat file1.txt\nduplicated\nnotduplicated\n\n$ cat file2.txt\nduplicated\nnot duplicated\n\n$ ander file1.txt file2.txt\nduplicated\n```\n\n## Installation\n\n```bash\n$ pip install ander\n```\n\n### Requirements\n\n- Python >= 3.6\n- Some Python Libraries (see `pyproject.toml`)\n\n## License\n\nThis software is released under the MIT License, see LICENSE.\n',
    'author': 'Josuke Yamane',
    'author_email': 's1r0mqme@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/joe-yama/ander',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4',
}


setup(**setup_kwargs)
