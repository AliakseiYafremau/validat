banned = {"!", "#", "$", "%", "^", "&", "*", "(", ")"}


def validate_email(email: str) -> bool:
    at_sign_count = email.count("@")

    if at_sign_count != 1:
        return False

    if len(email) > 254:
        return False

    if banned.intersection(set(email)):
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
