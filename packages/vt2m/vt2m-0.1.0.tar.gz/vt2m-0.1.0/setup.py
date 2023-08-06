# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vt2m']

package_data = \
{'': ['*']}

install_requires = \
['pymisp>=2.4.155,<3.0.0', 'requests>=2.27.1,<3.0.0', 'vt-py>=0.14.0,<0.15.0']

entry_points = \
{'console_scripts': ['vt2m = vt2m.vt2m:cli']}

setup_kwargs = {
    'name': 'vt2m',
    'version': '0.1.0',
    'description': 'Automatically import results from VirusTotal queries into MISP objects',
    'long_description': None,
    'author': '3c7',
    'author_email': '3c7@posteo.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
