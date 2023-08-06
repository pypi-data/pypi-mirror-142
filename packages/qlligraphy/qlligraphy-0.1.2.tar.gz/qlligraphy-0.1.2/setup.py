# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qlligraphy', 'qlligraphy.core', 'qlligraphy.core.base']

package_data = \
{'': ['*']}

install_requires = \
['astunparse>=1.6.3,<2.0.0',
 'black>=22.1.0,<23.0.0',
 'graphql-core>=3.2.0,<4.0.0',
 'isort>=5.10.1,<6.0.0',
 'pydantic>=1.9.0,<2.0.0']

entry_points = \
{'console_scripts': ['qlligraphy = qlligraphy.main:app']}

setup_kwargs = {
    'name': 'qlligraphy',
    'version': '0.1.2',
    'description': 'graphql-schema -> pydantic models',
    'long_description': '# Qlligraphy. GraphQL Schema -> Pydantic models \n\nQlligraphy is a simple CLI tool, that generates pydantic models based on graphQL schema. \n\n## Installation\n\n``` shell\npip install qlligraphy\n```\n\n## Usage:\nConsider the following schema written in `example.gql` \n\n``` graphQL \nenum Episode {\n NEWHOPE\n EMPIRE\n JEDI\n}\n\ntype Character {\n  name: String!\n  appearsIn: [Episode]!\n}\n```\n\nRunning:\n\n``` shell\nqlligraphy example.gql -o example.py\n```\n\nResults in the following python file: \n\n``` python\nfrom enum import Enum\nfrom typing import List, Optional\n\nfrom pydantic import BaseModel\n\n\nclass Episode(str, Enum):\n    NEWHOPE = "NEWHOPE"\n    EMPIRE = "EMPIRE"\n    JEDI = "JEDI"\n\n\nclass Character(BaseModel):\n    name: str\n    appearsIn: List[Optional[Episode]]\n\n```\n\nNOTE: This package in WIP state\n\n',
    'author': 'kuchichan',
    'author_email': 'pawel.kucharski@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kuchichan/QLligraphy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
