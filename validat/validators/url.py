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

    available_protocols = ["http://", "https://"]

    if "://" not in url:
        return error(URLValidationError, "Url must contain protocol")

    domain_index_start = url.find("://") + 3
    domain_index_end = url[domain_index_start:].find("/")
    if domain_index_end == -1:
        domain_index_end = len(url)
    else:
        domain_index_end = domain_index_start + url[domain_index_start:].find("/")
    protocol = url[:domain_index_start]

    if protocol not in available_protocols:
        return error(URLValidationError, f"Protocol '{protocol}' is not supported")

    authority_url = url[domain_index_start:domain_index_end]

    if "." not in authority_url and authority_url != "localhost":
        print(authority_url)
        return error(URLValidationError, "Invalid domain")

    return True
