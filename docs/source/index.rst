.. validat documentation master file, created by
   sphinx-quickstart on Fri Feb  7 00:24:15 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

validat documentation
=====================

Overview
--------
validat - A lightweight, small library for validating different types of data like: mail, phone, url address and etc.


Installation
------------
**validat** requires Python 3.10+.

.. code-block:: bash
   
   pip install validat


Example
-------
Here’s a simple example demonstrating how to use **validat**:

.. code-block:: python

   import validat

   correct_email = "username@example.com"
   is_valid = validat.validate_email(correct_email)
   print(is_valid) # True

   wrong_email = "username@@example.com"
   is_valid = validat.validate_email(wrong_email)
   print(is_valid) # False


License
-------
**validat** is released under the MIT license.


.. toctree::
   :maxdepth: 2
   :hidden:

   api_reference