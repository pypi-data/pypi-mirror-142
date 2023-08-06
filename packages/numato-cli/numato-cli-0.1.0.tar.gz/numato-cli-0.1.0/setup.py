# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['numato_cli']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.4,<0.5.0',
 'numato-gpio>=0.10.0,<0.11.0',
 'shellingham>=1.4.0,<2.0.0',
 'typer[all]>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['numato = numato_cli.__main__:app']}

setup_kwargs = {
    'name': 'numato-cli',
    'version': '0.1.0',
    'description': 'Command-line interface for Numato GPIO expanders',
    'long_description': "Numato CLI\n==========\n\nA command-line interface for Numato GPIO Expanders.\n\nInstall\n-------\n\n    pip install numato-cli\n\nor even better\n\n    pipx install numato-cli\n\nWith pipx you can also ensure that the `numato` executable's binary directory is in the PATH variable:\n\n    pipx ensurepath\n\n\nUse\n---\n\nDiscover all numato devices from a list of Linux/Windows devices::\n\n    numato discover\n\n\nDevelop\n-------\n\nBest practice is to use ``poetry`` installed with ``pipx``::\n\n    pip install pipx\n    pipx install poetry\n    poetry shell\n\nIn the poetry shell you can also run an IDE like VSCode::\n\n    code .\n\nInstall the dependencies and run the Numato CLI::\n\n    poetry install\n    numato --help\n\nBuild packages::\n\n    poetry build\n",
    'author': 'Henning Claßen',
    'author_email': 'code@clssn.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
