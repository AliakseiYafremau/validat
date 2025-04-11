Usage
=====

This section provides comprehensive examples of using validat in various scenarios.

Basic Usage
-----------

Email Validation
~~~~~~~~~~~~~~~~

The email validator checks if an email address follows the standard format and can optionally validate specific parts of the email.

.. code-block:: python

    import validat

    # Simple email validation
    email = "user@example.com"
    if validat.validate_email(email):
        print("Valid email")
    else:
        print("Invalid email")

    # Email validation with custom domain
    # This ensures the email is from a specific domain
    email = "user@company.com"
    if validat.validate_email(email, domain_name="company.com"):
        print("Valid company email")
    else:
        print("Invalid company email")

    # Email validation with TLD check
    # This ensures the email has a specific top-level domain
    email = "user@example.com"
    if validat.validate_email(email, tld="com"):
        print("Valid .com email")
    else:
        print("Invalid .com email")

Phone Number Validation
~~~~~~~~~~~~~~~~~~~~~~~

The phone number validator checks if a phone number follows international standards and can validate length constraints.

.. code-block:: python

    import validat

    # Simple phone validation
    # Checks if the phone number follows international format
    phone = "+1234567890"
    if validat.validate_phone(phone):
        print("Valid phone number")
    else:
        print("Invalid phone number")

    # Phone validation with length constraints
    # Ensures the phone number has a specific length range
    phone = "+1234567890"
    if validat.validate_phone(phone, min_length=10, max_length=15):
        print("Valid phone number length")
    else:
        print("Invalid phone number length")

URL Validation
~~~~~~~~~~~~~~

The URL validator checks if a URL follows the standard format and can validate specific parts of the URL.

.. code-block:: python

    import validat

    # Simple URL validation
    # Checks if the URL follows standard format
    url = "https://example.com"
    if validat.validate_url(url):
        print("Valid URL")
    else:
        print("Invalid URL")

    # URL validation with protocol check
    # Ensures the URL uses a specific protocol (e.g., HTTPS)
    url = "https://example.com"
    if validat.validate_url(url, protocol="https"):
        print("Valid HTTPS URL")
    else:
        print("Invalid HTTPS URL")

    # URL validation with authority check
    # Ensures the URL has a specific domain
    url = "https://example.com"
    if validat.validate_url(url, authority="example.com"):
        print("Valid domain")
    else:
        print("Invalid domain")

Advanced Usage
--------------

Error Handling
~~~~~~~~~~~~~~

When working with validation in production environments, it's often better to handle exceptions rather than just checking boolean results. This allows for more detailed error reporting.

.. code-block:: python

    import validat
    from validat.exceptions import (
        EmailValidationError,
        PhoneValidationError,
        URLValidationError
    )

    def validate_user_data(email, phone, url):
        """
        Validate user data with detailed error handling.
        
        This function demonstrates how to use exception handling
        to provide detailed feedback about validation failures.
        """
        try:
            # Validate email
            validat.validate_email(email, raise_exception=True)
            print("Email is valid")

            # Validate phone
            validat.validate_phone(phone, raise_exception=True)
            print("Phone is valid")

            # Validate URL
            validat.validate_url(url, raise_exception=True)
            print("URL is valid")

        except EmailValidationError as e:
            print(f"Email validation failed: {e}")
        except PhoneValidationError as e:
            print(f"Phone validation failed: {e}")
        except URLValidationError as e:
            print(f"URL validation failed: {e}")

    # Example usage
    validate_user_data(
        email="user@example.com",
        phone="+1234567890",
        url="https://example.com"
    )

Custom Validation Rules
~~~~~~~~~~~~~~~~~~~~~~~

You can create custom validation functions that wrap the base validators with specific business rules for your application.

.. code-block:: python

    import validat

    def validate_company_email(email):
        """
        Validate company email with specific rules.
        
        This function ensures that the email is from the company domain
        and raises an exception if validation fails.
        """
        return validat.validate_email(
            email,
            domain_name="company.com",
            raise_exception=True
        )

    def validate_international_phone(phone):
        """
        Validate international phone number.
        
        This function ensures that the phone number follows
        international format with specific length constraints.
        """
        return validat.validate_phone(
            phone,
            min_length=10,
            max_length=15,
            raise_exception=True
        )

    def validate_secure_url(url):
        """
        Validate secure HTTPS URL.
        
        This function ensures that the URL uses the HTTPS protocol
        for secure communication.
        """
        return validat.validate_url(
            url,
            protocol="https",
            raise_exception=True
        )

    # Example usage
    try:
        validate_company_email("user@company.com")
        validate_international_phone("+1234567890")
        validate_secure_url("https://example.com")
        print("All validations passed")
    except Exception as e:
        print(f"Validation failed: {e}") 