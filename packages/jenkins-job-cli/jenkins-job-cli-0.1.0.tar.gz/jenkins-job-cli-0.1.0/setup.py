# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jcli']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'api4jenkins>=1.9,<2.0',
 'appdirs>=1.4.4,<2.0.0',
 'click>=8.0.4,<9.0.0',
 'rich>=12.0.0,<13.0.0']

entry_points = \
{'console_scripts': ['jcli = jcli.cli:main']}

setup_kwargs = {
    'name': 'jenkins-job-cli',
    'version': '0.1.0',
    'description': 'Jcli: list, run, and check jenkins jobs',
    'long_description': '# Jcli\n\nSmall cli to list, run, and check jenkins jobs\n\n## Installation\n\n`pip install jenkins-job-cli`\n\n## Usage\n\n* `config`: setup the `jcli` configuration\n\n* `jobs`:\n  * `list`: list all jenkins jobs (default deep = 1)\n  * `run`: run a specific jenkins job\n\n* `jenkins`: show jenkins server info like version (`version`) and security options (`info`)\n',
    'author': 'Brokenpip3',
    'author_email': 'brokenpip3@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/brokenpip3/jcli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
