# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qlligraphy', 'qlligraphy.core', 'qlligraphy.core.base']

package_data = \
{'': ['*']}

install_requires = \
['astunparse>=1.6.3,<2.0.0',
 'graphql-core>=3.2.0,<4.0.0',
 'pydantic>=1.9.0,<2.0.0']

entry_points = \
{'console_scripts': ['qlligraphy = qlligraphy.main:app']}

setup_kwargs = {
    'name': 'qlligraphy',
    'version': '0.1.0',
    'description': 'graphql-schema -> pydantic models',
    'long_description': None,
    'author': 'kuchichan',
    'author_email': 'pawel.kucharski@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
