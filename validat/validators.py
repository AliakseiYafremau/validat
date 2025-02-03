from validat.exceptions.base import EmailValidationError


def validate_email(email: str, raise_exception: bool = False) -> bool:
    forbidden = set("!#$%^&*()")
    at_sign_count = email.count("@")

    def error(error_type: Exception, message: str):
        if raise_exception:
            raise error_type(message)
        return False

    if at_sign_count != 1:
        return error(EmailValidationError, "Email must have exactly one @ sign")

    if len(email) > 254:
        return False

    if forbidden.intersection(set(email)):
        return False

    if ".." in email:
        return False

    if " " in email:
        return False

    at_index = email.find("@")
    username = email[:at_index]
    domain = email[at_index + 1 :]

    if not username:
        return False

    if "." == username[0]:
        return False

    if "." == username[-1]:
        return False

    if not domain:
        return False

    if "." == domain[0]:
        return False

    if "." == domain[-1]:
        return False

    return True
