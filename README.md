# Validat

Validat is a Python library for data validation. It provides a simple and flexible way to validate data structures, ensuring that your data meets the required criteria.

## Features

- Easy to use and integrate
- Supports various data types and structures
- Customizable validation rules
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

correct_email = "username@example.com"
is_valid = validat.validate_email(correct_email)
print(is_valid) # True

wrong_email = "username@@example.com"
is_valid = validat.validate_email(wrong_email)
print(is_valid) # False
```

## Documentation

For more detailed information, please refer to the [official documentation](https://aliakseiyafremau.github.io/validat/).
