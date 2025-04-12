import pytest

from validat.exceptions.base import URLValidationError
from validat.validators.url import validate_url


def test_exception_correct_protocol() -> None:
    """Check for protocols."""
    incorrect_protocol_url = "incorrect://example.com"

    with pytest.raises(URLValidationError):
        validate_url(incorrect_protocol_url, raise_exception=True)


def test_exception_domain() -> None:
    """Check for domain."""
    one_word_domain = "https://example"
    no_domain = "https://"

    with pytest.raises(URLValidationError):
        validate_url(one_word_domain, raise_exception=True)
        validate_url(no_domain, raise_exception=True)


def test_exact_protocol() -> None:
    """Check for exact protocol in url."""
    url = "https://example.com"

    incorrect_protocol = "http://"

    with pytest.raises(URLValidationError):
        validate_url(url, raise_exception=True, protocol=incorrect_protocol)


def test_exact_authority() -> None:
    """Check for exact authority in url."""
    url = "https://example.com"

    incorrect_authority = "elpmaxe.com"

    with pytest.raises(URLValidationError):
        validate_url(url, raise_exception=True, authority=incorrect_authority)
