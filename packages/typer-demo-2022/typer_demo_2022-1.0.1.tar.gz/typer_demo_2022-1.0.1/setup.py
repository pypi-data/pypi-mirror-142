# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['typer_demo_2022']

package_data = \
{'': ['*']}

install_requires = \
['typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['hola-mundo = typer_demo_2022.main:app']}

setup_kwargs = {
    'name': 'typer-demo-2022',
    'version': '1.0.1',
    'description': 'Demo de typer para gulag',
    'long_description': '# typer_demo_2022\nTyper demo para GULAG\n',
    'author': 'Alex Pineda',
    'author_email': 'alejandro.deathscythe@google.com',
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
