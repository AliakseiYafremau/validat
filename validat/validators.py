def validate_email(email: str) -> bool:
    at_sign_count = email.count("@")
    if at_sign_count != 1:
        return False
    return True
