""" Financial Validators

- ValidateCreditCard
- ValidateCurrency
- ValidateIBAN
"""

import re
import sys
from moneyed import get_currency, CurrencyDoesNotExist
from schwifty import IBAN, BIC
from flask_validator import Validator


class ValidateCreditCard(Validator):

    """ Validate Credit Card Number

    Check if the new value is a valid credit card number.
    Allowed formats:
       - XXXXYYYYWWWWZZZ
       - "XXXXYYYYWWWWZZZ"
       - "XXXX YYYY WWWW ZZZ"
       - "XXXX-YYYY-WWWW-ZZZ"
    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails
    """

    def check_value(self, value):
        n = re.sub(r'[\s-]', '', str(value))
        r = [int(ch) for ch in str(n)][::-1]
        return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0


class ValidateCurrency(Validator):

    """ Validate Currency

    Check if the new value is a valid Currency
    Validation provided by: https://github.com/limist/py-moneyed

    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails
    """

    def check_value(self, value):
        value = str(value)
        try:
            get_currency(value.upper())
            return True
        except CurrencyDoesNotExist:
            return False


class ValidateIBAN(Validator):

    """ Validate IBAN

    Check if the new value is a valid IBAN

    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails
    """

    def check_value(self, value):
        try:
            value = IBAN(value)
            return True
        except ValueError:
            return False

class ValidateBIC(Validator):

    """ Validate BIC (Bank Identifier Code)

    Check if the new value is a valid Bank Identifier Code

    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails
    """

    def check_value(self, value):
        try:
            value = BIC(str(value))
            return True
        except ValueError:
            return False