import pytest
from validat.exceptions.base import EmailValidationError
from validat.validators.email import validate_email


def test_at_sign() -> None:
    """Check for the number of @ signs."""
    multiple_at_email = "@testemail@domain.com"
    zero_at_email = "testemaildomain.com"
    one_at_email = "testemail@domain.com"

    assert validate_email(one_at_email) == True
    with pytest.raises(EmailValidationError):
        validate_email(multiple_at_email)
        validate_email(zero_at_email)


def test_double_dot() -> None:
    """Check for two dots in a row."""
    double_dot_in_username_in_the_start = "..testexample@domain.com"
    double_dot_in_username_in_the_middle = "test..example@domain.com"
    double_dot_in_username_in_the_end = "testexample..@domain.com"

    double_dot_in_domain_in_the_start = "testexample@..domain.com"
    double_dot_in_domain_in_the_middle = "testexample@doma..in.com"
    double_dot_in_domain_in_the_end = "testexample@domain.com.."

    with pytest.raises(EmailValidationError):
        validate_email(double_dot_in_username_in_the_start)
        validate_email(double_dot_in_username_in_the_middle)
        validate_email(double_dot_in_username_in_the_end)

        validate_email(double_dot_in_domain_in_the_start)
        validate_email(double_dot_in_domain_in_the_middle)
        validate_email(double_dot_in_domain_in_the_end)


def test_single_dot_position() -> None:
    """Check for point position."""
    dot_in_username_in_the_start = ".testexample@domain.com"
    dot_in_username_in_the_middle = "test.example@domain.com"
    dot_in_username_in_the_end = "testexample.@domain.com"

    dot_in_domain_in_the_start = "testexample@.domain.com"
    dot_in_domain_in_the_middle = "testexample@doma.in.com"
    dot_in_domain_in_the_end = "testexample@domain.com."

    assert validate_email(dot_in_username_in_the_middle) == True
    assert validate_email(dot_in_domain_in_the_middle) == True
    with pytest.raises(EmailValidationError):
        validate_email(dot_in_username_in_the_start)
        validate_email(dot_in_username_in_the_end)

        validate_email(dot_in_domain_in_the_start)
        validate_email(dot_in_domain_in_the_end)


def test_not_dot_in_domain() -> None:
    """Check for dot in domain."""
    email_without_dot_in_domain = "testexample@domaincom"

    with pytest.raises(EmailValidationError):
        validate_email(email_without_dot_in_domain)


def test_incomplete_email() -> None:
    """Check for complete email address."""
    email_without_username = "@domain.com"
    email_without_domain = "testexample@"

    with pytest.raises(EmailValidationError):
        validate_email(email_without_username)
        validate_email(email_without_domain)


def test_spaces() -> None:
    """Check for spaces."""
    email_with_space_in_username = "test example@domain.com"
    email_with_space_in_domain = "testexample@dom ain.com"
    email_with_space_in_the_start = " testexample@domain.com"
    email_with_space_in_the_end = "testexample@domain.com "

    with pytest.raises(EmailValidationError):
        validate_email(email_with_space_in_username)
        validate_email(email_with_space_in_domain)
        validate_email(email_with_space_in_the_start)
        validate_email(email_with_space_in_the_end)


def test_tld_length() -> None:
    """Check length of TLD(Top-Level-Domain)."""
    email_with_insufficient_tld = "testexample@domain.c"
    email_with_normal_tld = "testexample@domain.co"

    assert validate_email(email_with_normal_tld) == True
    with pytest.raises(EmailValidationError):
        validate_email(email_with_insufficient_tld)


def test_exact_username() -> None:
    """Check for exact username in email."""
    email = "testexample@domain.com"

    correct_username = "testexample"
    incorrect_username = "exampletest"

    assert validate_email(email, username=correct_username) == True
    with pytest.raises(EmailValidationError):
        validate_email(email, username=incorrect_username)


def test_exact_domain() -> None:
    """Check for exact domain in email."""
    email = "testexample@domain.com"

    correct_domain = "domain"
    incorrect_domain = "aiondom"

    assert validate_email(email, domain_name=correct_domain) == True
    with pytest.raises(EmailValidationError):
        validate_email(email, domain_name=incorrect_domain)


def test_exact_tld() -> None:
    """Check for exact TLD(Top-Level-Domain) in email."""
    email = "testexample@domain.com"

    correct_tld = "com"
    incorrect_tld = "net"

    assert validate_email(email, tld=correct_tld) == True
    with pytest.raises(EmailValidationError):
        validate_email(email, tld=incorrect_tld)
