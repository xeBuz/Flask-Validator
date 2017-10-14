""" Location Validators

- ValidateLocale
- ValidateCountry
-ValidateTimezone
"""

import locale
from iso3166 import countries
from pytz import all_timezones
from flask_validator import Validator


class ValidateLocale(Validator):
    """ Validate Country

    Validate if the new value is a valid locale

    Args:
        field: SQLAlchemy column to validate
        value: Value to check
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails

    """

    def __init__(self, field, allow_null=True, throw_exception=False, message=None):
        self.all_locates = locale.locale_alias

        Validator.__init__(self, field, allow_null, throw_exception, message)

    def check_value(self, value):
        return bool(self.all_locates.get(str(value).lower()))


class ValidateCountry(Validator):

    """ Validate Country

    Check if the new values is a valid country name.
    Allowed names:
       - Name
       - Alpha2
       - Alpha3
       - Numeric
       - Apolitic Name

    Args:
        field: SQLAlchemy column to validate
        value: Value to check
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails

    """

    def check_value(self, value):
        try:
            countries.get(value)
            return True
        except KeyError:
            return False


class ValidateTimezone(Validator):

    """ Validate Country

    Validate if the new value is a valid Timezone

    Args:
        field: SQLAlchemy column to validate
        value: Value to check
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails

    """

    def check_value(self, value):
        return value in all_timezones
