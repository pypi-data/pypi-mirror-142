# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bike']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'bike',
    'version': '0.2.0',
    'description': 'A lightweight model validator for modern projects.',
    'long_description': '# bike\nA lightweight model validator for modern projects.\n\n## Instalation\n```shell\npip install bike\n```\n\n## First Pedals\n\nLets define a simple model to represent a person.\n\n```python hl_lines="1"\nimport bike\n\n@bike.model()\nclass Person:\n    name: str\n    height: float\n    weight: float\n\n```\nA Person instance can be created passing the attributes.\n```python\nperson = Person(name=\'Patrick Love\', height=75, weight=180)\n```\nAlso can be instatiated by a dict data.\n```python\ndata = {\n    \'name\': \'Patrick Love\',\n    \'height\': 75,\n    \'weight\': 180\n}\n\nperson = Person(**data)\n\n```\n\n\n\n',
    'author': 'Manasses Lima',
    'author_email': 'manasseslima@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/manasseslima/bike',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
