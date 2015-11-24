import locale
from iso3166 import countries
from pytz import all_timezones
from flask_validator import Validator


class LenguageConstraint(Validator):
    # TODO
    def check_value(self, value):
        pass


class ValidateLocale(Validator):
    """ Validate Country

    Validate if the new value is a valid locale

    Args:
        field: SQLAlchemy column to validate
        value: Value to check
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    allow_null = True

    def __init__(self, field, allow_null=True, throw_exception=False):
        self.allow_null = allow_null
        self.all_locates = locale.locale_alias

        Validator.__init__(self, field, throw_exception)

    def check_value(self, value):
        if self.allow_null and value is None:
            return True

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
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    allow_null = True

    def __init__(self, field, allow_null=True, throw_exception=False):
        self.allow_null = allow_null

        Validator.__init__(self, field, throw_exception)

    def check_value(self, value):
        if self.allow_null and value is None:
            return True

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
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    allow_null = True

    def __init__(self, field, allow_null=True, throw_exception=False):
        self.allow_null = allow_null

        Validator.__init__(self, field, throw_exception)

    def check_value(self, value):
        return value in all_timezones
        #     return True
        # else:
        #     return False

