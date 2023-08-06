# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exports']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'python-exports',
    'version': '1.0.0',
    'description': '@export decorator that adds a function or class to __all__',
    'long_description': "# Explicit module exports\n\n\n\n## Installation\n\n*Requires python>=3.8*\n\n`pip install exports`\n\n\n## Usage\n\n```pycon\n>>> from exports import export\n```\n\nNow you can use it to add to `__all__` as\n\n- function decorator\n\n    ```pycon\n    >>> @export\n    ... def spam():\n    ...     ...\n    ```\n\n- class decorator:\n\n    ```pycon\n    >>> @export\n    ... class Ham:\n    ...     ...\n    ```\n\n- by name:\n\n    ```pycon\n    >>> from functools import reduce as fold\n    >>> export('fold')\n    ```\n\n## Behaviour\n\nIf the module has no __all__, it is created. \nOtherwise, `__all__` is converted to a list, and the export is appended.\n\n## Caveats\n\nExporting a function or class directly relies on the __name__ attribute,\nso consider the following example:\n\n```pycon\n>>> def eggs():\n...     ...\n>>> fake_eggs = eggs\n```\n\nIf we want to export fake_eggs, then this **will not work**:\n\n```pycon\n>>> export(fake_eggs)  # BAD: this will add 'eggs' to __all__\n```\n\nIn such cases, use the name instead:\n\n```pycon\n>>> export('fake_eggs')  # GOOD\n```\n\nYou'll be safe if you either\n\n- decorate a function or a class directly with `@export`,\n- pass the name string when using plain `export('...')` calls.\n",
    'author': 'Joren Hammudoglu',
    'author_email': 'jhammudoglu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jorenham/exports',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
