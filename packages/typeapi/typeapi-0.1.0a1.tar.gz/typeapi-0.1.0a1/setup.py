# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['typeapi']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=3.0.0']

setup_kwargs = {
    'name': 'typeapi',
    'version': '0.1.0a1',
    'description': '',
    'long_description': "# typeapi\n\nTypeapi provides a sane and stable API to introspect Python type hints.\n\n## Installation\n\n    $ pip install typeapi\n\n## Quickstart\n\n```py\nimport typing\nfrom typeapi import parse_type_hint\n\nprint(parse_type_hint(typing.Any))                  # Type(object)\nprint(parse_type_hint(typing.List))                 # Type(list)\nprint(parse_type_hint(typing.Mapping[str, int]))    # Type(collections.abc.Mapping, (Type(str), Type(int)))\nprint(parse_type_hint(typing.Union[str, int]))      # Union(int, str)\nprint(parse_type_hint(str | int))                   # Union(int, str)\nprint(parse_type_hint(str | int | None))            # Optional(Union[int, str])\nprint(parse_type_hint(typing.Annotated[int, 42]))   # Annotated(int, 42)\nprint(parse_type_hint(typing.Annotated[int, 42]))   # Annotated(int, 42)\nprint(parse_type_hint('str', __name__))             # Type(str)\n```\n",
    'author': 'Niklas Rosenstein',
    'author_email': 'rosensteinniklas@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
