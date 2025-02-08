import pytest

from validat.validators.email import validate_email
from validat.exceptions.base import EmailValidationError


def test_exception_at_sign():
    """
    Check for the number of @ signs
    """
    multiple_at_email = "@testemail@domain.com"
    zero_at_email = "testemaildomain.com"

    with pytest.raises(EmailValidationError):
        validate_email(multiple_at_email, raise_exception=True)
        validate_email(zero_at_email, raise_exception=True)


def test_exception_double_dot():
    """
    Check for two dots in a row
    """
    double_dot_in_username_in_the_start = "..testexample@domain.com"
    double_dot_in_username_in_the_middle = "test..example@domain.com"
    double_dot_in_username_in_the_end = "testexample..@domain.com"

    double_dot_in_domain_in_the_start = "testexample@..domain.com"
    double_dot_in_domain_in_the_middle = "testexample@doma..in.com"
    double_dot_in_domain_in_the_end = "testexample@domain.com.."

    with pytest.raises(EmailValidationError):
        validate_email(double_dot_in_username_in_the_start, raise_exception=True)
        validate_email(double_dot_in_username_in_the_middle, raise_exception=True)
        validate_email(double_dot_in_username_in_the_end, raise_exception=True)

        validate_email(double_dot_in_domain_in_the_start, raise_exception=True)
        validate_email(double_dot_in_domain_in_the_middle, raise_exception=True)
        validate_email(double_dot_in_domain_in_the_end, raise_exception=True)


def test_exception_single_dot_position():
    """
    Check for point position
    """
    dot_in_username_in_the_start = ".testexample@domain.com"
    dot_in_username_in_the_end = "testexample.@domain.com"

    dot_in_domain_in_the_start = "testexample@.domain.com"
    dot_in_domain_in_the_end = "testexample@domain.com."

    with pytest.raises(EmailValidationError):
        validate_email(dot_in_username_in_the_start, raise_exception=True)
        validate_email(dot_in_username_in_the_end, raise_exception=True)

        validate_email(dot_in_domain_in_the_start, raise_exception=True)
        validate_email(dot_in_domain_in_the_end, raise_exception=True)


def test_exception_not_dot_in_domain():
    """
    Check for dot in domain
    """
    email_without_dot_in_domain = "testexample@domaincom"

    with pytest.raises(EmailValidationError):
        validate_email(email_without_dot_in_domain, raise_exception=True)


def test_exception_incomplete_email():
    """
    Check for complete email adress
    """
    email_without_username = "@domain.com"
    email_without_domain = "testexample@"

    with pytest.raises(EmailValidationError):
        validate_email(email_without_username, raise_exception=True)
        validate_email(email_without_domain, raise_exception=True)


def test_exception_spaces():
    """
    Check for spaces
    """
    email_with_space_in_username = "test example@domain.com"
    email_with_space_in_domain = "testexample@dom ain.com"
    email_with_space_in_the_start = " testexample@domain.com"
    email_with_space_in_the_end = "testexample@domain.com "

    with pytest.raises(EmailValidationError):
        validate_email(email_with_space_in_username, raise_exception=True)
        validate_email(email_with_space_in_domain, raise_exception=True)
        validate_email(email_with_space_in_the_start, raise_exception=True)
        validate_email(email_with_space_in_the_end, raise_exception=True)


def test_exception_tld_lenght():
    """
    Check lenght of TLD(Top-Level-Domain)
    """
    email_with_insufficient_tld = "testexample@domain.c"

    with pytest.raises(EmailValidationError):
        validate_email(email_with_insufficient_tld, raise_exception=True)


def test_exact_username():
    """
    Check for exact username in email
    """
    email = "testexample@domain.com"
    incorrect_username = "exampletest"

    with pytest.raises(EmailValidationError):
        validate_email(email, raise_exception=True, username=incorrect_username)


def test_exact_domain():
    """
    Check for exact domain in email
    """
    email = "testexample@domain.com"
    incorrect_domain = "aindom"

    with pytest.raises(EmailValidationError):
        validate_email(email, raise_exception=True, domain_name=incorrect_domain)


def test_exact_tld():
    """
    Check for exact tld in email
    """
    email = "testexample@domain.com"
    incorrect_tld = "net"

    with pytest.raises(EmailValidationError):
        validate_email(email, raise_exception=True, tld=incorrect_tld)
