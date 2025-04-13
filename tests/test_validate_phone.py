import pytest

from validat.exceptions.base import PhoneValidationError
from validat.validators.phone import validate_phone


def test_correct_phones() -> None:
    """Check for correct phone numbers."""
    assert validate_phone("1234567890") == True
    assert validate_phone("123-456-7890") == True
    assert validate_phone("(123) 456-7890") == True
    assert validate_phone("+1 (123) 456-7890") == True
    assert validate_phone("123.456.7890") == True
    assert validate_phone("123 456 7890") == True
    assert validate_phone("123((456))7890") == True


def test_incorrect_phones() -> None:
    """Check for incorrect phone numbers."""
    with pytest.raises(PhoneValidationError):
        validate_phone("abcdefgeh")
        validate_phone("123/456/7890")
        validate_phone("111222333444555666777888999")
        validate_phone("")


def test_length() -> None:
    """Check for length of phone number."""
    with pytest.raises(PhoneValidationError):
        validate_phone("123456789", min_length=15)
        validate_phone("12345678910111213", max_length=5)
