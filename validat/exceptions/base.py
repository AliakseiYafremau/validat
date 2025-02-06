class ValidatError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class EmailValidationError(ValidatError):
    pass
