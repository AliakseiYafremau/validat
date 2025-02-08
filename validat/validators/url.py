from validat.exceptions.base import URLValidationError, get_exception_raiser


def validate_url(url: str, raise_exception: bool = False) -> bool:
    """Validate url.

    Args:
        url (str): Url
        raise_exception (bool, optional): Raise exception if validation fails. Defaults to False.

    Returns:
        bool: True if url is valid. False if not.
    """
    error = get_exception_raiser(raise_exception)

    if not url:
        return error(URLValidationError, "Url cannot be empty")
    
    if not url.startswith("http://") and not url.startswith("https://"):
        return error(URLValidationError, "Url must start with http:// or https://")
    
    protocol = url.split("://")[0]
    body = url.split("://")[1]

    return True