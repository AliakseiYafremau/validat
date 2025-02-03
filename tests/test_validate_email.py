from validat.validators import validate_email


def test_at_sign():
    multiple_at_email = "@testemail@domain.com"
    zero_at_email = "testemaildomain.com"
    one_at_email = "testemail@domain.com"

    assert validate_email(multiple_at_email) == False
    assert validate_email(zero_at_email) == False
    assert validate_email(one_at_email) == True


def test_dot_sign():
    double_dot_email = "test..example@domain.com"
    one_dot_email = "test.example@domain.com"

    assert validate_email(double_dot_email) == False
    assert validate_email(one_dot_email) == True