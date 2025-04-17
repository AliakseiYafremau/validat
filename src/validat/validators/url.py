from validat.exceptions.base import (
    URLValidationError,
)


def validate_url(
    url: str,
    protocol: str | None = None,
    authority: str | None = None,
) -> bool:
    """Validate url.

    Args:
        **url** (str): Url \n

    Returns:
        **bool**: True if url is valid. False if not.

    """

    if not url:
        raise URLValidationError("Url cannot be empty")

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
        raise URLValidationError("Url must contain protocol")

    if protocol_url not in available_protocols:
        raise URLValidationError(f"Protocol '{protocol_url}' is not supported")

    if "." not in authority_url and authority_url != "localhost":
        raise URLValidationError("Invalid domain")

    if protocol is not None and protocol != protocol_url:
        raise URLValidationError("URL has different protocol")

    if authority is not None and authority != authority_url:
        raise URLValidationError("URL has different authority")

    return True
