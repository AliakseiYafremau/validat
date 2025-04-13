from validat.exceptions.base import PhoneValidationError


def validate_phone(phone: str, min_length: int = 7, max_length: int = 15) -> bool:
    """Validate phone number.

    Args:
        **phone** (str): Phone number \n
        **raise_exception** (bool, optional): Raise exception if validation fails. Defaults to False. \n

    Returns:
        **bool**: True if phone is valid. False if not.

    """
    if not phone:
        raise PhoneValidationError("Phone number cannot be empty")

    allowed_chars = set("0123456789+-(). ")
    phone_with_only_digits = "".join([char for char in phone if char.isdigit()])

    if (
        len(phone_with_only_digits) < min_length
        or len(phone_with_only_digits) > max_length
    ):
        raise PhoneValidationError(
            f"Phone number must be between {min_length} and {max_length} digits",
        )

    if set(phone).difference(set(phone).intersection(allowed_chars)):
        raise PhoneValidationError(
            "Phone number must contain only digits, +, -, (, ), ., and spaces",
        )

    return True
