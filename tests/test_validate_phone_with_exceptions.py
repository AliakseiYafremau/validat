import pytest

from validat.exceptions.base import PhoneValidationError
from validat.validators.phone import validate_phone


def test_incorrect_phones() -> None:
    """Check for incorrect phone numbers."""
    with pytest.raises(PhoneValidationError):
        assert validate_phone("abcdefgeh", raise_exception=True)
        assert validate_phone("123/456/7890", raise_exception=True)
        assert validate_phone("111222333444555666777888999", raise_exception=True)
        assert validate_phone("", raise_exception=True)


def test_length() -> None:
    """Check for length of phone number."""
    with pytest.raises(PhoneValidationError):
        assert validate_phone("123456789", raise_exception=True, min_length=15)
        assert validate_phone("12345678910111213", raise_exception=True, max_length=5)
