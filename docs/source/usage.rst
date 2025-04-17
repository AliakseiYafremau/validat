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
    try:
        validat.validate_email(email)
        print("Valid email")
    except validat.EmailValidationError as e:
        print(f"Email validation failed: {e}")

    # Email validation with custom domain
    # This ensures the email is from a specific domain
    email = "user@company.com"
    try:
        validat.validate_email(email, domain_name="company.com")
        print("Valid company email")
    except validat.EmailValidationError as e:
        print(f"Email validation failed: {e}")

    # Email validation with TLD check
    # This ensures the email has a specific top-level domain
    email = "user@example.com"
    try:
        validat.validate_email(email, tld="com")
        print("Valid .com email")
    except validat.EmailValidationError as e:
        print(f"Email validation failed: {e}")

Phone Number Validation
~~~~~~~~~~~~~~~~~~~~~~~

The phone number validator checks if a phone number follows international standards and can validate length constraints.

.. code-block:: python

    import validat

    # Simple phone validation
    # Checks if the phone number follows international format
    phone = "+1234567890"
    try:
        validat.validate_phone(phone)
    except validat.PhoneValidationError as e:
        print(f"Phone validation failed: {e}")

    # Phone validation with length constraints
    # Ensures the phone number has a specific length range
    phone = "+1234567890"
    try:
        validat.validate_phone(phone, min_length=10, max_length=15)
    except validat.PhoneValidationError as e:
        print(f"Phone validation failed: {e}")

URL Validation
~~~~~~~~~~~~~~

The URL validator checks if a URL follows the standard format and can validate specific parts of the URL.

.. code-block:: python

    import validat

    # Simple URL validation
    # Checks if the URL follows standard format
    url = "https://example.com"
    try:
        validat.validate_url(url)
        print("Valid URL")
    except validat.URLValidationError as e:
        print(f"URL validation failed: {e}")

    # URL validation with protocol check
    # Ensures the URL uses a specific protocol (e.g., HTTPS)
    url = "https://example.com"
    try:
        validat.validate_url(url, protocol="https")
        print("Valid HTTPS URL")
    except validat.URLValidationError as e:
        print(f"URL validation failed: {e}")

    # URL validation with authority check
    # Ensures the URL has a specific domain
    url = "https://example.com"
    try:
        validat.validate_url(url, authority="example.com")
        print("Valid domain")
    except validat.URLValidationError as e:
        print(f"URL validation failed: {e}")

Advanced Usage
--------------

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
            domain_name="company.com"
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
            max_length=15
        )

    def validate_secure_url(url):
        """
        Validate secure HTTPS URL.
        
        This function ensures that the URL uses the HTTPS protocol
        for secure communication.
        """
        return validat.validate_url(
            url,
            protocol="https"
        )

    # Example usage
    try:
        validate_company_email("user@company.com")
        validate_international_phone("+1234567890")
        validate_secure_url("https://example.com")
        print("All validations passed")
    except Exception as e:
        print(f"Validation failed: {e}") 