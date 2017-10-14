""" Numbers Validators 

- ValidateLength
- ValidateLessThanOrEqual
- ValidateGreaterThan
- ValidateGreaterThanOrEqual
"""

import math
from flask_validator import Validator


class ValidateLength(Validator):
    """ Validate Length type.

    Check if the new value has a proper length

    Args:
        field: SQLAlchemy column to validate
        max_length: (int) Maximum value length
        min_length: (int) Minimum value length
        throw_exception: (bool) Throw a ValidateError if the validation fails

    """

    max_length = None
    min_length = 0

    def __init__(self, field, max_length=None, min_length=0, throw_exception=False, message=None):
        self.max_length = max_length
        self.min_length = min_length

        Validator.__init__(self, field, False, throw_exception, message)

    def check_value(self, value):

        if not self.max_length:
            raise Warning("Argument max_length should't be null")

        return int(self.max_length) >= len(value) >= int(self.min_length)


class ValidateNumber(Validator):
    """ Validate if is a Number

    Check if the value is a number or not (NaN)

    Args:
        field: SQLAlchemy column to validate
        throw_exception: (bool) Throw a ValidateError if the validation fails
    """

    def check_value(self, value):
        return not math.isnan(value)
