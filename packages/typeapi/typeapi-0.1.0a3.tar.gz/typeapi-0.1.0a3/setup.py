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
    'version': '0.1.0a3',
    'description': '',
    'long_description': "# typeapi\n\nTypeapi provides a stable and documented API to introspect Python `typing` type hints.\n\n## Installation\n\n    $ pip install typeapi\n\n## Quickstart\n\n```py\nimport typing\nimport typeapi\n\nprint(typeapi.of(typing.Any))                  # Type(object)\nprint(typeapi.of(typing.List))                 # Type(list)\nprint(typeapi.of(typing.Mapping[str, int]))    # Type(collections.abc.Mapping, (Type(str), Type(int)))\nprint(typeapi.of(typing.Union[str, int]))      # Union(int, str)\nprint(typeapi.of(str | int))                   # Union(int, str)\nprint(typeapi.of(str | int | None))            # Optional(Union[int, str])\nprint(typeapi.of(typing.Annotated[int, 42]))   # Annotated(int, 42)\nprint(typeapi.of(typing.Annotated[int, 42]))   # Annotated(int, 42)\nprint(typeapi.of('str', __name__))             # Type(str)\n```\n",
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
