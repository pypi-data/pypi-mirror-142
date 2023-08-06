# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zdppy_redis']

package_data = \
{'': ['*']}

install_requires = \
['aioredis[hiredis]>=2.0.1,<3.0.0',
 'redis>=4.1.4,<5.0.0',
 'zdppy-log>=0.1.5,<0.2.0']

setup_kwargs = {
    'name': 'zdppy-redis',
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
