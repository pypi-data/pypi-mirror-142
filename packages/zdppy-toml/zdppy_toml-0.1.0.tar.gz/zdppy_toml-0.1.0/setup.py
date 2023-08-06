# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zdppy_toml', 'zdppy_toml.libs', 'zdppy_toml.libs.toml']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'zdppy-toml',
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
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
