from validat.exceptions.base import PhoneValidationError, get_exception_raiser


def validate_phone(
    phone: str, raise_exception: bool = False, min_length: int = 7, max_length: int = 15
) -> bool:
    """Validate phone number.

    Args:
        phone (str): Phone number
        raise_exception (bool, optional): Raise exception if validation fails. Defaults to False.

    Returns:
        bool: True if phone is valid. False if not.
    """
    error = get_exception_raiser(raise_exception)

    if not phone:
        return error(PhoneValidationError, "Phone number cannot be empty")

    allowed_chars = set("0123456789+-(). ")
    phone_with_only_digits = "".join([char for char in phone if char.isdigit()])

    if (
        len(phone_with_only_digits) < min_length
        or len(phone_with_only_digits) > max_length
    ):
        return error(
            PhoneValidationError,
            f"Phone number must be between {min_length} and {max_length} digits",
        )

    if set(phone).difference(set(phone).intersection(allowed_chars)):
        return error(
            PhoneValidationError,
            "Phone number must contain only digits, +, -, (, ), ., and spaces",
        )

    return True
