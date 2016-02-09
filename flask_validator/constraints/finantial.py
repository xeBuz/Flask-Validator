import re
import sys
from moneyed import get_currency, CurrencyDoesNotExist
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
        if sys.version_info >= (3, 0):
            n = str(value).replace(' ', '').replace('-', '')
        else:
            n = str(value).translate(None, ' -')

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

    Check if the new value is valid IBAN
    Logic by: http://rosettacode.org/wiki/IBAN#Python

    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails
    """

    _country2length = {'AL': 28, 'AD': 24, 'AT': 20, 'AZ': 28, 'BE': 16, 'BH': 22, 'BA': 20, 'BR': 29, 'BG': 22,
                       'CR': 21, 'HR': 21, 'CY': 28, 'CZ': 24, 'DK': 18, 'DO': 28, 'EE': 20, 'FO': 18, 'FI': 18,
                       'FR': 27, 'GE': 22, 'DE': 22, 'GI': 23, 'GR': 27, 'GL': 18, 'GT': 28, 'HU': 28, 'IS': 26,
                       'IE': 22, 'IL': 23, 'IT': 27, 'KZ': 20, 'KW': 30, 'LV': 21, 'LB': 28, 'LI': 21, 'LT': 20,
                       'LU': 20, 'MK': 19, 'MT': 31, 'MR': 27, 'MU': 30, 'MC': 27, 'MD': 24, 'ME': 22, 'NL': 18,
                       'NO': 15, 'PK': 24, 'PS': 29, 'PL': 28, 'PT': 25, 'RO': 24, 'SM': 27, 'SA': 24, 'RS': 22,
                       'SK': 24, 'SI': 19, 'ES': 24, 'SE': 24, 'CH': 21, 'TN': 24, 'TR': 26, 'AE': 23, 'GB': 22,
                       'VG': 24}

    def check_value(self, value):
        # Ensure upper alphanumeric input.
        iban = value.replace(' ', '').replace('\t', '')
        if not re.match(r'^[\dA-Z]+$', iban):
            return False
        # Validate country code against expected length.
        if len(iban) != self._country2length[iban[:2]]:
            return False
        # Shift and convert.
        iban = iban[4:] + iban[:4]
        digits = int(''.join(str(int(ch, 36)) for ch in iban))  # BASE 36: 0..9,A..Z -> 0..35
        return digits % 97 == 1
