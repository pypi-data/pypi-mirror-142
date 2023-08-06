# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asynced']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.10"': ['typing-extensions>4.1.0']}

setup_kwargs = {
    'name': 'asynced',
    'version': '0.1.0',
    'description': 'Async python for Event-Driven applications',
    'long_description': "# AsyncED\n\nAsync python for Event-Driven applications\n\n## High-level API\n\n*Coming soon...*\n\n## Low-level API\n\n### Perpetual\n\nWhere asyncio futures are the bridge between low-level events and a\ncoroutines, perpetuals are the bridge between event streams and async\niterators.\n\nIn it's essence, a perpetual is an asyncio.Future that can have its result\n(or exception) set multiple times, at least until it is stopped. Besides\na perpetual being awaitable just like a future, it is an async iterator as\nwell.\n\n\n### ensure_future\n\nWrap an async iterable in a perpetual, and automatically starts iterating. \n\nSee [perpetual_drumkit.py](examples/perpetual_drumkit.py) for an example.\n\n~\n\n*More docs and examples coming soon...*\n",
    'author': 'Joren Hammudoglu',
    'author_email': 'jhammudoglu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jorenham/asynced',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4',
}


setup(**setup_kwargs)
