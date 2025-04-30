# Validat

[![pypi](https://img.shields.io/pypi/v/validat?color=blue)](https://pypi.org/project/validat/)
[![versions](https://img.shields.io/pypi/pyversions/validat)](https://pypi.org/project/validat/)
[![license](https://img.shields.io/github/license/AliakseiYafremau/validat)](https://github.com/AliakseiYafremau/validat/blob/main/LICENSE)

Validat is a Python library for data validation. It provides a simple and flexible way to validate data structures, ensuring that your data meets the required criteria.

## Documentation

For more detailed information, please refer to the [official documentation](https://aliakseiyafremau.github.io/validat/).

## Features

- Easy to use and integrate
- Supports various data types and structures
- Detailed error messages

## Installation

You can install Validat using pip:

```bash
pip install validat
```

## Usage

Here's a basic example of how to use Validat:

```python
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
```
