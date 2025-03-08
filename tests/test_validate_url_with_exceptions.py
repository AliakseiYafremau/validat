import pytest

from validat.validators.url import validate_url
from validat.exceptions.base import URLValidationError


def test_exception_correct_protocol():
    """
    Check for protocols
    """
    incorrect_protocol_url = "incorrect://example.com"

    with pytest.raises(URLValidationError):
        validate_url(incorrect_protocol_url, raise_exception=True)


def test_exception_domain():
    """
    Check for domain
    """
    one_word_domain = "https://example"
    no_domain = "https://"

    with pytest.raises(URLValidationError):
        validate_url(one_word_domain, raise_exception=True)
        validate_url(no_domain, raise_exception=True)
