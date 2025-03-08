from validat.validators.phone import validate_phone


def test_correct_phones():
    assert validate_phone("1234567890") == True
    assert validate_phone("123-456-7890") == True
    assert validate_phone("(123) 456-7890") == True
    assert validate_phone("+1 (123) 456-7890") == True
    assert validate_phone("123.456.7890") == True
    assert validate_phone("123 456 7890") == True
    assert validate_phone("123((456))7890") == True


def test_incorrect_phones():
    assert validate_phone("abcdefgeh") == False
    assert validate_phone("123/456/7890") == False
    assert validate_phone("111222333444555666777888999") == False
    assert validate_phone("") == False


def test_length():
    assert validate_phone("123456789", min_length=15) == False
    assert validate_phone("12345678910111213", max_length=5) == False
