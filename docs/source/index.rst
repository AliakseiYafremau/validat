.. validat documentation master file, created by
   sphinx-quickstart on Fri Feb  7 00:24:15 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

validat documentation
=====================

Overview
--------
validat - A lightweight Python library for data validation. It provides simple and flexible ways to validate various types of data such as email addresses, phone numbers, and URLs.

Features
--------
* Simple and intuitive API
* Comprehensive validation rules
* Detailed error messages
* Customizable validation parameters
* Exception handling support

Installation
------------
**validat** requires Python 3.10+.

.. code-block:: bash
   
   pip install validat

Quick Start
-----------
Here's a simple example demonstrating how to use **validat**:

.. code-block:: python

   import validat

   try:
      # returns True 
      correct_email = "username@example.com"
      is_valid = validat.validate_email(correct_email)
   except validat.EmailValidationError as e:
      print(f"Email validation error: {e.message}")

   try:
      # raises EmailValidationError
      wrong_email = "username@@example.com"
      is_valid = validat.validate_email(wrong_email) 
   except validat.EmailValidationError as e:
      print(f"Email validation error: {e.message}")

Documentation Contents
----------------------
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   api_reference
   contributing

License
-------
**validat** is released under the `MIT <https://github.com/AliakseiYafremau/validat/blob/main/LICENSE>`_ license.