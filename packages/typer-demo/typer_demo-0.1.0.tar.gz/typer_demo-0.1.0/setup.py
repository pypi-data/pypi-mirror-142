# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['typer_demo', 'typer_demo.utils']

package_data = \
{'': ['*']}

install_requires = \
['typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['rick-portal-gun = typer_demo.main:app']}

setup_kwargs = {
    'name': 'typer-demo',
    'version': '0.1.0',
    'description': 'typer cli demo',
    'long_description': '# gulag-demo-typer-cli\nDemo of typer, poetry, github actions, and deployment.\n',
    'author': 'Alex Pineda',
    'author_email': 'alehpineda@google.com',
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
