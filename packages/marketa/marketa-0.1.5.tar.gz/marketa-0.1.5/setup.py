# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['marketa',
 'marketa.data',
 'marketa.entities',
 'marketa.services',
 'marketa.shared']

package_data = \
{'': ['*']}

install_requires = \
['PyQt5>=5.15.6,<6.0.0',
 'PyYAML>=6.0,<7.0',
 'SQLAlchemy-Utils>=0.38.2,<0.39.0',
 'SQLAlchemy>=1.4.31,<2.0.0',
 'daemonize>=2.5.0,<3.0.0',
 'diskcache>=5.2.1,<6.0.0',
 'docopt>=0.6.2,<0.7.0',
 'exitstatus>=2.2.0,<3.0.0',
 'financedatabase>=1.0.0,<2.0.0',
 'humanize>=3.13.1,<4.0.0',
 'lagom>=1.7.0,<2.0.0',
 'matplotlib>=3.5.1,<4.0.0',
 'mplfinance>=0.12.8-beta.9,<0.13.0',
 'numpy>=1.20.2,<2.0.0',
 'pandas>=1.2.4,<2.0.0',
 'purl>=1.5,<2.0',
 'sequential-uuids>=1.0.0,<2.0.0',
 'tqdm>=4.62.3,<5.0.0',
 'yfinance>=0.1.63,<0.2.0']

entry_points = \
{'console_scripts': ['linter = poetry:lint']}

setup_kwargs = {
    'name': 'marketa',
    'version': '0.1.5',
    'description': '',
    'long_description': None,
    'author': 'illiak',
    'author_email': 'ilichpost@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
