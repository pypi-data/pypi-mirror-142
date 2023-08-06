# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyroll_wusatowski_spreading']

package_data = \
{'': ['*']}

install_requires = \
['pyroll>=0.5.0,<0.6.0']

setup_kwargs = {
    'name': 'pyroll-wusatowski-spreading',
    'version': '0.2.0',
    'description': 'Plugin for PyRoll providing the Wusatowski spreading model.',
    'long_description': None,
    'author': 'Max Weiner',
    'author_email': 'max.weiner@imf.tu-freiberg.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pyroll-project.github.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
