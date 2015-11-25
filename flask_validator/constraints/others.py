import re
from uuid import UUID
from flask_validator import Validator


class ValidateRegex(Validator):
    """ Validate Regex

    Compare a value against a regular expresion

    Args:
        field: SQLAlchemy column to validate
        regex: Regular expresion
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails

    """

    regex = None

    def __init__(self, field, regex, allow_null=False, throw_exception=False):
        try:
            self.regex = regex
            re.compile(regex)
        except re.error:
            raise AttributeError('Invalid Regex')

        Validator.__init__(self, field, allow_null, throw_exception)

    def check_value(self, value):
        if re.match(self.regex, value):
            return True
        else:
            return False


class ValidateUUID(Validator):
    """ Validate UUID

    Validate if the value is a valida UUID

    Args:
        field: SQLAlchemy column to validate
        version: UUUID version. Default 4
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails

    """
    varsion = 4

    def __init__(self, field, version=4, allow_null=True, throw_exception=False):
        self.version = version

        Validator.__init__(self, field, allow_null, throw_exception)

    def check_value(self, value):
        try:
            val = UUID(value, version=self.version)
            if val:
                return True
            else:
                return False
        except (ValueError, TypeError):
            return False
