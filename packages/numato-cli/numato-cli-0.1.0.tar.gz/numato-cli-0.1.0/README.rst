Numato CLI
==========

A command-line interface for Numato GPIO Expanders.

Install
-------

    pip install numato-cli

or even better

    pipx install numato-cli

With pipx you can also ensure that the `numato` executable's binary directory is in the PATH variable:

    pipx ensurepath


Use
---

Discover all numato devices from a list of Linux/Windows devices::

    numato discover


Develop
-------

Best practice is to use ``poetry`` installed with ``pipx``::

    pip install pipx
    pipx install poetry
    poetry shell

In the poetry shell you can also run an IDE like VSCode::

    code .

Install the dependencies and run the Numato CLI::

    poetry install
    numato --help

Build packages::

    poetry build
