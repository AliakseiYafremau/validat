from validat.exceptions.base import EmailValidationError


def validate_email(
    email: str,
    username: str | None = None,
    domain_name: str | None = None,
    tld: str | None = None,
) -> bool:
    """Validate email adress.

    Args:
        **email** (str): Email address \n
        **username** (str, optional): Username to validate. Defaults to None. \n
        **domain_name** (str, optional): Domain name to validate. Defaults to None. \n
        **tld** (str, optional): TLD(Top-Level-Domain) to validate. Defaults to None. \n

    Returns:
        **bool**: True if email is valid. False if not.

    """
    if not email:
        raise EmailValidationError("Email address cannot be empty")

    forbidden = set("!#$%^&*()")
    at_sign_count = email.count("@")

    if at_sign_count != 1:
        raise EmailValidationError("Email address must have exactly one @ sign")

    if len(email) > 254:
        raise EmailValidationError("Email address cannot have more than 254 characters")

    if forbidden.intersection(set(email)):
        raise EmailValidationError("Email address contains unreadable characters.")

    if ".." in email:
        raise EmailValidationError("Email address cannot contain two dots together")

    if " " in email:
        raise EmailValidationError("Email adress cannot contain spaces")

    at_index = email.find("@")
    splitted_username = email[:at_index]
    splitted_domain = email[at_index + 1 :]

    if not splitted_username:
        raise EmailValidationError("Email address must contain a username")

    if splitted_username[0] == ".":
        raise EmailValidationError("Email address cannot begin with a dot")

    if splitted_username[-1] == ".":
        raise EmailValidationError("Username cannot end with a dot")

    if not splitted_domain:
        raise EmailValidationError("Email address must contain a domain")

    if "." not in splitted_domain:
        raise EmailValidationError("Domain must have at least one dot")

    if splitted_domain[0] == ".":
        raise EmailValidationError("Domain cannot begin with a dot")

    if splitted_domain[-1] == ".":
        raise EmailValidationError("Email address cannot end with a dot")

    splitted_tld = splitted_domain[splitted_domain.find(".") + 1 :]
    splitted_domain_name = splitted_domain[: splitted_domain.find(".")]

    if len(splitted_tld) < 2:
        raise EmailValidationError("TLD must be no shorter than 2 characters")

    if username is not None and splitted_username != username:
        raise EmailValidationError("Email address has different username")

    if domain_name is not None and splitted_domain_name != domain_name:
        raise EmailValidationError("Email address has different domain name")

    if tld is not None and splitted_tld != tld:
        raise EmailValidationError("Email address has different top level domain")

    return True
