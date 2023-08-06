# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['noname_backend',
 'noname_backend.cfg',
 'noname_backend.db',
 'noname_backend.flask']

package_data = \
{'': ['*']}

install_requires = \
['Flask', 'peewee', 'pysqlite3']

setup_kwargs = {
    'name': 'noname-backend-common',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'andre',
    'author_email': 'andre@void.fyi',
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
