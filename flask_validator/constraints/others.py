import re
from flask_validator import Validator


class ValidateRegex(Validator):
    """ Validate Regex

    Compare a value against a regular expresion

    Args:
        field: SQLAlchemy column to validate
        regex: Regular expresion
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    regex = None

    def __init__(self, field, regex, throw_exception=False):
        try:
            self.regex = regex
            re.compile(regex)
        except re.error:
            raise AttributeError('Invalid Regex')

        Validator.__init__(self, field, throw_exception)

    def check_value(self, value):
        if re.match(self.regex, value):
            return True
        else:
            return False


class ValidateUUID(Validator):
    # TODO
    def check_value(self, value):
        pass
