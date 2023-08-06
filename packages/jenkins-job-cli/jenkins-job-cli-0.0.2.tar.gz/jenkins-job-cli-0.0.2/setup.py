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
    'version': '0.0.2',
    'description': 'Jcli: list, run, and check jenkins jobs',
    'long_description': '# Jcli\n\nList, run, and check jenkins jobs\n',
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
