# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyorthanc']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'pyorthanc',
    'version': '0.2.16',
    'description': 'Orthanc REST API python wrapper with additional utilities',
    'long_description': None,
    'author': 'Gabriel Couture',
    'author_email': 'gacou54@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
