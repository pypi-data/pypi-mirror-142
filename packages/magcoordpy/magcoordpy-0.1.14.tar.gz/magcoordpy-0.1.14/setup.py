# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['magcoordpy']

package_data = \
{'': ['*'], 'magcoordpy': ['data/*']}

install_requires = \
['numpy>=1.22.2,<2.0.0', 'pymap3d>=2.7.2,<3.0.0', 'urllib3>=1.26.8,<2.0.0']

setup_kwargs = {
    'name': 'magcoordpy',
    'version': '0.1.14',
    'description': 'A python package for working with magnetic coordinate transformations',
    'long_description': None,
    'author': 'Giorgio Savastano',
    'author_email': 'giorgio.savastano@uniroma1.it',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
