# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zdppy_yaml']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0']

setup_kwargs = {
    'name': 'zdppy-yaml',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'zhangdapeng',
    'author_email': 'pygosuperman@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
