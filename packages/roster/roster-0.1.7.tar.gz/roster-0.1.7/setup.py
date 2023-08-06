# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['roster']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'roster',
    'version': '0.1.7',
    'description': 'Python object registers. Keep track of your classes, functions and data.',
    'long_description': "# roster\nPython object registers. Keep track of your classes, functions and data.\n\n## Installation\n```console\npip install roster\n```\n\n## Usage:\n\n### `Record`\n\n#### Example: Standard Record\n```python\nimport roster\n\nnumbers = roster.Record()\n\nnumbers(1)\nnumbers(2)\nnumbers(3)\n```\n\n```python\n>>> numbers\n[1, 2, 3]\n```\n\n#### Example: Hooked Record\n```python\nimport roster\n\nsquare_numbers = roster.Record(hook=lambda n: n ** 2)\n\nsquare_numbers(1)\nsquare_numbers(2)\nsquare_numbers(3)\n```\n\n```python\n>>> square_numbers\n[1, 4, 9]\n```\n\n#### Example: Decorator\n```python\nimport roster\n\nclasses = roster.Record()\n\n@classes\nclass Foo: pass\n\n@classes\nclass Bar: pass\n```\n\n##### Usage\n```python\n>>> classes\n[<class '__main__.Foo'>, <class '__main__.Bar'>]\n```\n\n### `Register`\n\n#### Example: Standard Register\n```python\nimport roster\n\nfunctions = roster.Register()\n\n@functions(author = 'Sam')\ndef foo(): ...\n\n@functions(author = 'Robbie')\ndef bar(): ...\n```\n\n```python\n>>> functions\n{\n    <function foo at 0x7fa9110a50d0>: Context(author='Sam'),\n    <function bar at 0x7fa9110a5160>: Context(author='Robbie')\n}\n```\n\n#### Example: Hooked Register\n```python\nimport roster\nimport dataclasses\n\n@dataclasses.dataclass\nclass Route:\n    path: str\n    method: str = 'GET'\n\nroutes = roster.Register(hook=Route)\n\n@routes('/user', method = 'POST')\ndef create_user(name: str) -> str:\n    return f'Created user: {name!r}'\n```\n\n```python\n>>> routes\n{<function create_user at 0x7f2f9d775ee0>: Route(path='/user', method='POST')}\n```\n",
    'author': 'Tom Bulled',
    'author_email': '26026015+tombulled@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tombulled/roster',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
