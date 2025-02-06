from validat.exceptions.base import EmailValidationError


def validate_email(email: str, raise_exception: bool = False) -> bool:
    forbidden = set("!#$%^&*()")
    at_sign_count = email.count("@")

    def error(error_type: Exception, message: str):
        if raise_exception:
            raise error_type(message)
        return False

    if at_sign_count != 1:
        return error(EmailValidationError, "Email address must have exactly one @ sign")

    if len(email) > 254:
        return error(
            EmailValidationError, "Email address cannot have more than 254 characters"
        )

    if forbidden.intersection(set(email)):
        return error(
            EmailValidationError, "Email address contains unreadable characters."
        )

    if ".." in email:
        return error(
            EmailValidationError, "Email address cannot contain two dots together"
        )

    if " " in email:
        return error(EmailValidationError, "Email adress cannot contain spaces")

    at_index = email.find("@")
    username = email[:at_index]
    domain = email[at_index + 1 :]

    if not username:
        return error(EmailValidationError, "Email address must contain a username")

    if "." == username[0]:
        return error(EmailValidationError, "Email address cannot begin with a dot")

    if "." == username[-1]:
        return error(EmailValidationError, "Username cannot end with a dot")

    if not domain:
        return error(EmailValidationError, "Email address must contain a domain")

    if "." == domain[0]:
        return error(EmailValidationError, "Domain cannot begin with a dot")

    if "." == domain[-1]:
        return error(EmailValidationError, "Email address cannot end with a dot")

    return True
