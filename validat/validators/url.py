from validat.exceptions.base import URLValidationError, get_exception_raiser


def validate_url(
    url: str, raise_exception: bool = False, protocol: str = None, authority: str = None
) -> bool:
    """Validate url.

    Args:
        url (str): Url
        raise_exception (bool, optional): Raise exception if validation fails. Defaults to False.

    Returns:
        bool: True if url is valid. False if not.
    """
    error = get_exception_raiser(raise_exception)

    available_protocols = ["http://", "https://"]
    domain_index_start = url.find("://") + 3
    domain_index_end = url[domain_index_start:].find("/")

    if domain_index_end == -1:
        domain_index_end = len(url)
    else:
        domain_index_end = domain_index_start + url[domain_index_start:].find("/")

    protocol_url = url[:domain_index_start]
    authority_url = url[domain_index_start:domain_index_end]

    if "://" not in url:
        return error(URLValidationError, "Url must contain protocol")

    if protocol_url not in available_protocols:
        return error(URLValidationError, f"Protocol '{protocol_url}' is not supported")

    if "." not in authority_url and authority_url != "localhost":
        print(authority_url)
        return error(URLValidationError, "Invalid domain")

    if protocol is not None and protocol != protocol_url:
        return error(URLValidationError, "URL has different protocol")

    if authority is not None and authority != authority_url:
        return error(URLValidationError, "URL has different authority")

    return True
