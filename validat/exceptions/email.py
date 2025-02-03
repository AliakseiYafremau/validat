from validat.exceptions.base import ValidatError


class AtSignNotFoundError(ValidatError):
    pass


class ManyAtSignFoundError(ValidatError):
    pass
