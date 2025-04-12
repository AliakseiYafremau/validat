Contributing
============

We welcome contributions to validat! This document provides guidelines and instructions for contributing to the project.

Getting Started
---------------

1. Fork the repository
2. Clone your fork::

    git clone https://github.com/your-username/validat.git
    cd validat

3. Create a virtual environment and activate it::

    uv venv

4. Install development dependencies::

    uv sync --all-groups

Testing and Linting
-------------------

You can lint and run pytest using tox::

    tox

or do it separately::

    # Linting
    ruff check
    ruff format --check

    # Run tests
    pytest

Writing Tests
~~~~~~~~~~~~~

* Place test files in the ``tests/`` directory
* Name test files with prefix ``test_``
* Use descriptive test names
* Include both positive and negative test cases
* Add docstrings to test functions

Documentation
-------------

We use Sphinx for documentation. To build the documentation::

    make html -C docs

License
-------

By contributing to validat, you agree that your contributions will be licensed under the MIT License. 