# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['invoke_common_tasks']

package_data = \
{'': ['*']}

install_requires = \
['invoke>=1.6.0,<2.0.0']

setup_kwargs = {
    'name': 'invoke-common-tasks',
    'version': '0.1.0',
    'description': 'Some common tasks for PyInvoke to bootstrap your code quality and testing workflows.',
    'long_description': '# Invoke Common Tasks\n\nSome common tasks for PyInvoke to bootstrap your code quality and testing workflows.\n\n\n## Getting Started\n\n```sh\npip install invoke-common-tasks\n```\n\n### Invoke Setup\n\n`tasks.py`\n\n```python\nfrom invoke_common_tasks import *\n```\n\nOnce your `tasks.py` is setup like this `invoke` will have the extra commands:\n\n```sh\nλ invoke --list\nAvailable tasks:\n\n  build    Build wheel.\n  ci       Run linting and test suite for Continuous Integration.\n  format   Autoformat code for code style.\n  lint     Linting and style checking.\n  test     Run test suite.\n```\n\n\n## The Tasks\n\n### build\n\nAssuming you are using `poetry` this will build a wheel.\n\n### format\n\nThis will apply code formatting tools `black` and `isort`.\n\nThese are only triggers for these commands, the specifics of configuration are up to you.\n\n### lint\n\nThis will run checks for `black`, `isort` and `flake8`.\n\nUp to you to specify your preferences of plugins for `flake8` and its configuration.\n\n### test\n\nThis will simply run `python3 -m pytest`. This is important to run as a module instead of `pytest` since it resolves\na lot of import issues.\n\nYou can simply not import this task if you prefer something else. But all config and plugins are left flexible for your own desires, this simply triggers the entrypoint.\n\n### ci\n\nThis is a task with no commands but chains together `lint` and `test`. \n\n## TODO\n\n - typechecking\n - test coverage\n\nAlso auto-initialisations of some default config.\n\n\n## All Together\n\nOnce all the tasks are imported, you can create a custom task as your default task with runs a few tasks chained together.\n\n```python\nfrom invoke import task\nfrom invoke_common_tasks import *\n\n@task(pre=[format, lint, test], default=True)\ndef all(c):\n  """Default development loop."""\n  ...\n```\n\nYou will notice a few things here:\n\n1. The method has no implementation `...`\n1. We are chaining a series of `@task`s in the `pre=[...]` argument\n1. The `default=True` on this root tasks means we could run either `invoke dev` or simply `invoke`.\n\nHow cool is that?\n\n# Contributing\n\nOpen an issue and lets have a chat to triage needs or concerns before you sink too much effort on a PR.\n\nOr if you\'re pretty confident your change is inline with the direction of this project then go ahead and open that PR.\n\nOr feel free to fork this project and rename it to your own variant. It\'s cool, I don\'t mind.\n\n# Resources\n\n - [`pyinvoke`](https://pyinvoke.org)\n\n# Prior Art\n\n - https://github.com/Smile-SA/invoke-sphinx\n - https://github.com/Dashlane/dbt-invoke\n - https://invocations.readthedocs.io/en/latest/index.html\n\n',
    'author': 'Josh Peak',
    'author_email': 'neozenith.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/neozenith/invoke-common-tasks',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
