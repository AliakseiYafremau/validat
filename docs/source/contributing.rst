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

Code Style
----------

We follow PEP 8 style guide for Python code. To ensure your code meets our standards:

1. Install development tools::

    pip install ruff black

2. Format your code::

    black .
    ruff check .

Testing
-------

We use pytest for testing. To run tests:

1. Install test dependencies::

    pip install pytest

2. Run tests::

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

We use Sphinx for documentation. To build the documentation:

.. code-block:: bash
    
    make html -C docs

License
-------

By contributing to validat, you agree that your contributions will be licensed under the MIT License. 