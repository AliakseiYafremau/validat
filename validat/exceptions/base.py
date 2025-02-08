class ValidatError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class EmailValidationError(ValidatError):
    pass


class PhoneValidationError(ValidatError):
    pass


class URLValidationError(ValidatError):
    pass


def get_exception_raiser(raise_exception: bool = False):
    def error(error_type: Exception, message: str):
        if raise_exception:
            raise error_type(message)
        return False

    return error
