""" ValidateError class user for Exceptions """

class ValidateError(ValueError):
    """ Exception class for Validations """
    def __init__(self, message):

        super(ValidateError, self).__init__(message)
