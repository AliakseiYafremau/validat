API Reference
=============

This section provides detailed information about the validat API.

Validation
----------

Email Address
~~~~~~~~~~~~~
.. automodule:: validat.validators.email
    :members:
    :undoc-members:
    :show-inheritance:

The email validator provides comprehensive email address validation with the following features:

* Validates email format according to RFC 5322
* Supports custom domain validation
* Allows TLD (Top-Level Domain) validation
* Provides detailed error messages
* Supports exception raising on validation failure

Parameters
^^^^^^^^^^

* **email** (str): The email address to validate
* **raise_exception** (bool, optional): If True, raises an exception on validation failure. Defaults to False.
* **username** (str, optional): Specific username to validate against. If provided, the email's username part must match this value.
* **domain_name** (str, optional): Specific domain to validate against. If provided, the email's domain part must match this value.
* **tld** (str, optional): Specific TLD to validate against. If provided, the email's TLD part must match this value.

Returns
^^^^^^^

* **bool**: True if the email is valid according to the specified criteria, False otherwise.

Example usage:

.. code-block:: python

    import validat

    # Basic email validation
    is_valid = validat.validate_email("user@example.com")

    # With custom domain validation
    is_valid = validat.validate_email(
        "user@example.com",
        domain_name="example.com"
    )

    # With TLD validation
    is_valid = validat.validate_email(
        "user@example.com",
        tld="com"
    )

    # With exception raising
    try:
        validat.validate_email("invalid@email", raise_exception=True)
    except validat.exceptions.EmailValidationError as e:
        print(f"Validation failed: {e}")

Phone Number
~~~~~~~~~~~~
.. automodule:: validat.validators.phone
    :members:
    :undoc-members:
    :show-inheritance:

The phone number validator provides comprehensive phone number validation with the following features:

* Supports international phone number formats
* Validates number length
* Handles various country formats
* Provides detailed error messages
* Supports exception raising on validation failure

Parameters
^^^^^^^^^^

* **phone** (str): The phone number to validate
* **min_length** (int, optional): Minimum length of the phone number. Defaults to 7.
* **max_length** (int, optional): Maximum length of the phone number. Defaults to 15.

Returns
^^^^^^^

* **bool**: True if the phone number is valid according to the specified criteria, False otherwise.

Example usage:

.. code-block:: python

    import validat

    try:
        validat.validate_phone("+1234567890")
    except validat.exceptions.PhoneValidationError as e:
        print(f"Validation failed: {e}")

    try:
        validat.validate_phone("123")
    except validat.exceptions.PhoneValidationError as e:
        print(f"Validation failed: {e}")

URL
~~~
.. automodule:: validat.validators.url
    :members:
    :undoc-members:
    :show-inheritance:

The URL validator provides comprehensive URL validation with the following features:

* Validates URL format according to RFC 3986
* Supports protocol validation
* Allows authority validation
* Provides detailed error messages
* Supports exception raising on validation failure

Parameters
^^^^^^^^^^

* **url** (str): The URL to validate
* **raise_exception** (bool, optional): If True, raises an exception on validation failure. Defaults to False.
* **protocol** (str, optional): Specific protocol to validate against. If provided, the URL's protocol part must match this value (e.g., "http", "https", "ftp").
* **authority** (str, optional): Specific authority to validate against. If provided, the URL's authority part must match this value.

Returns
^^^^^^^

* **bool**: True if the URL is valid according to the specified criteria, False otherwise.

Example usage:

.. code-block:: python

    import validat

    # Basic URL validation
    is_valid = validat.validate_url("https://example.com")

    # With protocol validation
    is_valid = validat.validate_url(
        "https://example.com",
        protocol="https"
    )

    # With authority validation
    is_valid = validat.validate_url(
        "https://example.com",
        authority="example.com"
    )

    # With exception raising
    try:
        validat.validate_url("invalid-url", raise_exception=True)
    except validat.exceptions.URLValidationError as e:
        print(f"Validation failed: {e}")

Exceptions
----------

.. automodule:: validat.exceptions.base
    :members:
    :undoc-members:
    :show-inheritance:
    :exclude-members: ErrorRaiser

The exceptions module provides specific exception classes for each validation type:

* ``EmailValidationError`` - Raised when email validation fails
* ``PhoneValidationError`` - Raised when phone number validation fails
* ``URLValidationError`` - Raised when URL validation fails
* ``ValidatError`` - Base exception class for all validat exceptions

Example usage:

.. code-block:: python

    import validat
    from validat.exceptions import (
        EmailValidationError,
        PhoneValidationError,
        URLValidationError
    )

    try:
        validat.validate_email("invalid@email", raise_exception=True)
    except EmailValidationError as e:
        print(f"Email validation failed: {e}")

    try:
        validat.validate_phone("123", raise_exception=True)
    except PhoneValidationError as e:
        print(f"Phone validation failed: {e}")

    try:
        validat.validate_url("invalid-url", raise_exception=True)
    except URLValidationError as e:
        print(f"URL validation failed: {e}")