.. _usage:

Usage Guide
===========

Import Example
--------------
After installing **validat**, you can start using it in your Python projects.

Import the library:

.. code-block:: python

    import validat

Example Usage
-------------
Here’s a simple example demonstrating how to use **validat**:

.. code-block:: python

    import validat
    
    email = "username@example.com"
    is_valid = validat.validate_email(email)
    print(is_valid) # True
