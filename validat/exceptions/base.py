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


class ErrorRaiser:
    def __init__(self, raise_exception: bool, exception_type: ValidatError):
        self.raise_exception = raise_exception
        self.exception_type = exception_type

    def __call__(self, message) -> bool:
        if self.raise_exception:
            raise self.exception_type(message)
        return False
