# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['adfpy', 'adfpy.activities']

package_data = \
{'': ['*']}

install_requires = \
['azure-mgmt-datafactory>=2.2.1,<3.0.0', 'azure-mgmt-resource>=20.1.0,<21.0.0']

extras_require = \
{'deploy': ['azure-identity>=1.7.1,<2.0.0']}

setup_kwargs = {
    'name': 'adfpy',
    'version': '0.0.1',
    'description': 'A Pythonic wrapper for Azure Data Factory',
    'long_description': None,
    'author': 'Daniel van der Ende',
    'author_email': 'daniel.vanderende@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
