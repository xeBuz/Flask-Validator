""" Comparision Types 

- ValidateInteger
- ValidateNumeric
- ValidateString
- ValidateBoolean
"""

import sys
from flask_validator import Validator


class ValidateInteger(Validator):
    """ Validate Integer type.

    Check if the new value is a integer or a long integer

    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values. Default True
        throw_exception: (bool) Throw a ValidateError if the validation fails

    """

    def check_value(self, value):
        if sys.version_info >= (3, 0):
            return isinstance(value, int)
        else:
            return isinstance(value, (int, long))


class ValidateNumeric(Validator):
    """ Validate Numeric type.

    Check if the new value is a integer, long, complex or float type

    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails

    """

    def check_value(self, value):
        if sys.version_info >= (3, 0):
            return isinstance(value, (int, float, complex))
        else:
            return isinstance(value, (int, long, float, complex))


class ValidateString(Validator):
    """ Validate String type.

    Check if the new value is a string

    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails

    """

    def check_value(self, value):
        return isinstance(value, str)


class ValidateBoolean(Validator):
    """ Validate Boolean type.

    Check if the new value is a boolean

    Args:
        field: SQLAlchemy column to validate
        throw_exception: (bool) Throw a ValidateError if the validation fails
    """
    def __init__(self, field):
        Validator.__init__(self, field, False)

    def check_value(self, value):
        return isinstance(value, bool)
