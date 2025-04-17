import pytest

from validat.exceptions.base import URLValidationError
from validat.validators.url import validate_url


def test_correct_protocol() -> None:
    """Check for protocols."""
    http_url = "http://example.com"
    https_url = "https://example.com"
    incorrect_protocol_url = "incorrect://example.com"

    assert validate_url(http_url) == True
    assert validate_url(https_url) == True

    with pytest.raises(URLValidationError):
        validate_url(incorrect_protocol_url)


def test_domain() -> None:
    """Check for domain."""
    domain_url = "https://example.com"
    one_word_domain = "https://example"
    no_domain = "https://"
    localhost_url = "http://localhost"

    assert validate_url(domain_url) == True
    assert validate_url(localhost_url) == True

    with pytest.raises(URLValidationError):
        validate_url(one_word_domain)
    with pytest.raises(URLValidationError):
        validate_url(no_domain)


def test_exact_protocol() -> None:
    """Check for exact protocol in url."""
    url = "https://example.com"

    correct_protocol = "https://"
    incorrect_protocol = "http://"

    assert validate_url(url, protocol=correct_protocol) == True

    with pytest.raises(URLValidationError):
        validate_url(url, protocol=incorrect_protocol)


def test_exact_authority() -> None:
    """Check for exact authority in url."""
    url = "https://example.com"

    correct_authority = "example.com"
    incorrect_authority = "elpmaxe.com"

    assert validate_url(url, authority=correct_authority) == True

    with pytest.raises(URLValidationError):
        validate_url(url, authority=incorrect_authority)
