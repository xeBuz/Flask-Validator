from flask_validator import FlaskValidator
import sys
import re
from validate_email import validate_email


class Validator(FlaskValidator):
    throw_exception = False

    def __init__(self, field, **kwargs):
        """
        Validator Interface initialization

        :param field:  Flask Column to validate
        :param kwargs: Valiable Parameter list
        """

        for key, value in kwargs.items():
            setattr(self, key, value)

        FlaskValidator.__init__(self, field, self.throw_exception)

    def check_value(self, value):
        """
        Validate the new value

        :param value:
        """
        pass


class ValidateInteger(Validator):
    """ Validate Integer type.

    Check if the new value is a integer or a long integer

    Args:
        value: new value
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    allow_null = True

    def check_value(self, value):

        if self.allow_null and value is None:
            return True

        if sys.version_info >= (3, 0):
            return isinstance(value, int)
        else:
            return isinstance(value, (int, long))


class ValidateNumeric(Validator):
    """ Validate Numeric type.

    Check if the new value is a integer, long, complex or float type

    Args:
        value: new value
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    allow_null = True

    def check_value(self, value):

        if self.allow_null and value is None:
            return True

        if sys.version_info >= (3, 0):
            return isinstance(value, (int, float, complex))
        else:
            return isinstance(value, (int, long, float, complex))


class ValidateString(Validator):
    """ Validate String type.

    Check if the new value is a string

    Args:
        value: new value
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    allow_null = True

    def check_value(self, value):
        if self.allow_null and value is None:
            return True

        return isinstance(value, str)


class ValidateBoolean(Validator):
    """ Validate Boolean type.

    Check if the new value is a boolean

    Args:
        value: new value
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    def check_value(self, value):
        return isinstance(value, bool)


class ValidateLength(Validator):
    """ Validate Length type.

    Check if the new value has a proper length

    Args:
        value: new value
        max_length: (int) Maximum value length
        min_lenght: (int) Minimum value length
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    max_length = None
    min_lenght = 0

    def check_value(self, value):

        if not self.max_length:
            raise Warning("Argument max_length should't be null")

        return int(self.max_length) >= len(value) >= int(self.min_lenght)


class ValidateEmail(Validator):
    """ Validate Email type.

    Check if the new value is a valid e-mail.
    Using this library to validate https://github.com/syrusakbary/validate_email

    Args:
        value: new value
        check_mx: (bool) Check if the host has SMTP Server
        verify: (bool) Check if the host has SMTP Server and the email really exists
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    check_mx = False
    verify = False

    def check_value(self, value):
        return validate_email(value, check_mx=self.check_mx, verify=self.verify)


class URLConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class RegexConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class IPConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class UUIDConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class LessThanConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class LessThanOrEqualConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class GreaterThanConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class GreaterThanOrEqualConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class RangeConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class DateConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class TimeConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class DateTimeConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class LenguageConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class LocaleConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class CountryConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class CardConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class CurrencyConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class LuhnConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class IbanConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class IsbnConstraint(Validator):
    # TODO
    def check(self, value):
        pass


class IssnConstraint(Validator):
    # TODO
    def check(self, value):
        pass
