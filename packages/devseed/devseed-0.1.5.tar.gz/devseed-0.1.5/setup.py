# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['devseed']

package_data = \
{'': ['*']}

install_requires = \
['PyPika>=0.48.8,<0.49.0',
 'PyYAML>=6.0,<7.0',
 'environs>=9.5.0,<10.0.0',
 'funcy>=1.17,<2.0',
 'pendulum>=2.1.2,<3.0.0',
 'pg8000>=1.24.1,<2.0.0',
 'rich>=11.2.0,<12.0.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['devseed = devseed.devseed:app']}

setup_kwargs = {
    'name': 'devseed',
    'version': '0.1.5',
    'description': 'Tool to seed database using YAML files',
    'long_description': None,
    'author': 'Edvard Majakari',
    'author_email': 'edvard@majakari.net',
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
