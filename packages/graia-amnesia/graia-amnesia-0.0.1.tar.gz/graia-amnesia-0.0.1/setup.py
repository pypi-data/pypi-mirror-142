# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['graia', 'graia.amnesia', 'graia.amnesia.builtins']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'rich>=12.0.0,<13.0.0']

setup_kwargs = {
    'name': 'graia-amnesia',
    'version': '0.0.1',
    'description': 'a collection of shared components for graia',
    'long_description': None,
    'author': 'GreyElaina',
    'author_email': 'GreyElaina@outlook.com',
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
