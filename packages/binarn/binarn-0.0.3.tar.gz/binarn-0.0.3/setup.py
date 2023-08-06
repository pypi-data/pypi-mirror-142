# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['binarn']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'binarn',
    'version': '0.0.3',
    'description': 'Find arbitrary keys in deep dictionaries.',
    'long_description': '# binarn\n\n**binarn** is a small tool to find an arbitrary key in a deep dictionary. It returns the full path\nto that key (if any) as well as its value.\n\nIt is intended as a debugging/exploration tool only.\n\n## Install\n\n    pip install binarn\n\n## Usage\n\n```python3\nimport binarn\n\nbinarn.find_one(my_deep_dict, key="my_key")\n# => (("key1", "key2", "my_key"), "value")\n```\n\n## Origin of the name\n\n"binarn" may look like a random name, but it has a true meaning. It stands for "binarn is not a\nrandom name".\n',
    'author': 'Baptiste Fontaine',
    'author_email': 'b@ptistefontaine.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bfontaine/binarn',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
