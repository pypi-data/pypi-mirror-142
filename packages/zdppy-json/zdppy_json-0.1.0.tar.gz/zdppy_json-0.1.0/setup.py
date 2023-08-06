# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zdppy_json']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'zdppy-json',
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
