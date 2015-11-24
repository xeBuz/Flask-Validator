

class ValidateError(ValueError):
    def __init__(self, message):

        super(ValidateError, self).__init__(message)
