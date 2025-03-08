from validat.validators.email import validate_email


def test_at_sign():
    """
    Check for the number of @ signs
    """
    multiple_at_email = "@testemail@domain.com"
    zero_at_email = "testemaildomain.com"
    one_at_email = "testemail@domain.com"

    assert validate_email(multiple_at_email) == False
    assert validate_email(zero_at_email) == False
    assert validate_email(one_at_email) == True


def test_double_dot():
    """
    Check for two dots in a row
    """
    double_dot_in_username_in_the_start = "..testexample@domain.com"
    double_dot_in_username_in_the_middle = "test..example@domain.com"
    double_dot_in_username_in_the_end = "testexample..@domain.com"

    double_dot_in_domain_in_the_start = "testexample@..domain.com"
    double_dot_in_domain_in_the_middle = "testexample@doma..in.com"
    double_dot_in_domain_in_the_end = "testexample@domain.com.."

    assert validate_email(double_dot_in_username_in_the_start) == False
    assert validate_email(double_dot_in_username_in_the_middle) == False
    assert validate_email(double_dot_in_username_in_the_end) == False

    assert validate_email(double_dot_in_domain_in_the_start) == False
    assert validate_email(double_dot_in_domain_in_the_middle) == False
    assert validate_email(double_dot_in_domain_in_the_end) == False


def test_single_dot_position():
    """
    Check for point position
    """
    dot_in_username_in_the_start = ".testexample@domain.com"
    dot_in_username_in_the_middle = "test.example@domain.com"
    dot_in_username_in_the_end = "testexample.@domain.com"

    dot_in_domain_in_the_start = "testexample@.domain.com"
    dot_in_domain_in_the_middle = "testexample@doma.in.com"
    dot_in_domain_in_the_end = "testexample@domain.com."

    assert validate_email(dot_in_username_in_the_start) == False
    assert validate_email(dot_in_username_in_the_middle) == True
    assert validate_email(dot_in_username_in_the_end) == False

    assert validate_email(dot_in_domain_in_the_start) == False
    assert validate_email(dot_in_domain_in_the_middle) == True
    assert validate_email(dot_in_domain_in_the_end) == False


def test_not_dot_in_domain():
    """
    Check for dot in domain
    """
    email_without_dot_in_domain = "testexample@domaincom"

    assert validate_email(email_without_dot_in_domain) == False


def test_incomplete_email():
    """
    Check for complete email adress
    """
    email_without_username = "@domain.com"
    email_without_domain = "testexample@"

    assert validate_email(email_without_username) == False
    assert validate_email(email_without_domain) == False


def test_spaces():
    """
    Check for spaces
    """
    email_with_space_in_username = "test example@domain.com"
    email_with_space_in_domain = "testexample@dom ain.com"
    email_with_space_in_the_start = " testexample@domain.com"
    email_with_space_in_the_end = "testexample@domain.com "

    assert validate_email(email_with_space_in_username) == False
    assert validate_email(email_with_space_in_domain) == False
    assert validate_email(email_with_space_in_the_start) == False
    assert validate_email(email_with_space_in_the_end) == False


def test_tld_lenght():
    """
    Check lenght of TLD(Top-Level-Domain)
    """
    email_with_insufficient_tld = "testexample@domain.c"
    email_with_normal_tld = "testexample@domain.co"

    assert validate_email(email_with_insufficient_tld) == False
    assert validate_email(email_with_normal_tld) == True


def test_exact_username():
    """
    Check for exact username in email
    """
    email = "testexample@domain.com"

    correct_username = "testexample"
    incorrect_username = "exampletest"

    assert validate_email(email, username=correct_username) == True
    assert validate_email(email, username=incorrect_username) == False


def test_exact_domain():
    """
    Check for exact domain in email
    """
    email = "testexample@domain.com"

    correct_domain = "domain"
    incorrect_domain = "aiondom"

    assert validate_email(email, domain_name=correct_domain) == True
    assert validate_email(email, domain_name=incorrect_domain) == False


def test_exact_tld():
    """
    Check for exact TLD(Top-Level-Domain) in email
    """
    email = "testexample@domain.com"

    correct_tld = "com"
    incorrect_tld = "net"

    assert validate_email(email, tld=correct_tld) == True
    assert validate_email(email, tld=incorrect_tld) == False
