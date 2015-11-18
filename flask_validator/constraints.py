from flask_validator import FlaskValidator
import sys
from email_validator import validate_email, EmailNotValidError

THROW_EXCEPTION = False


class Validator(FlaskValidator):

    def __init__(self, field, throw_exception):
        """
        Validator Interface initialization

        :param field:  Flask Column to validate
        """

        FlaskValidator.__init__(self, field, throw_exception)

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
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values. Default True
        throw_exception: (bool) Throw a ValueError if the validation fails

    """
    allow_null = True

    def __init__(self, field, allow_null=True, throw_exception=THROW_EXCEPTION):
        self.allow_null = allow_null

        Validator.__init__(self, field, throw_exception)

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
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    allow_null = True

    def __init__(self, field, allow_null=True, throw_exception=THROW_EXCEPTION):
        self.allow_null = allow_null

        Validator.__init__(self, field, throw_exception)

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
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    allow_null = True

    def __init__(self, field, allow_null=True, throw_exception=THROW_EXCEPTION):
        self.allow_null = allow_null

        Validator.__init__(self, field, throw_exception)

    def check_value(self, value):
        if self.allow_null and value is None:
            return True

        return isinstance(value, str)


class ValidateBoolean(Validator):
    """ Validate Boolean type.

    Check if the new value is a boolean

    Args:
        field: SQLAlchemy column to validate
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    def __init__(self, field, allow_null=True, throw_exception=THROW_EXCEPTION):
        self.allow_null = allow_null

        Validator.__init__(self, field, throw_exception)

    def check_value(self, value):
        return isinstance(value, bool)


class ValidateLength(Validator):
    """ Validate Length type.

    Check if the new value has a proper length

    Args:
        field: SQLAlchemy column to validate
        max_length: (int) Maximum value length
        min_lenght: (int) Minimum value length
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    max_length = None
    min_lenght = 0

    def __init__(self, field, max_length=None, min_length=0, throw_exception=THROW_EXCEPTION):
        self.max_length = max_length
        self.min_lenght = min_length

        Validator.__init__(self, field, throw_exception)

    def check_value(self, value):

        if not self.max_length:
            raise Warning("Argument max_length should't be null")

        return int(self.max_length) >= len(value) >= int(self.min_lenght)


class ValidateLessThan(Validator):

    def check_value(self, value):
        return value < self.va


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


class ValidateEmail(Validator):
    """ Validate Email type.

    Check if the new value is a valid e-mail.
    Using this library to validate https://github.com/JoshData/python-email-validator

    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        allow_smtputf8: (bool) Set to False to prohibit internationalized addresses that would require the SMTPUTF8.
        check_deliverability: (bool) Set to False to skip the domain name resolution check.
        allow_empty_local (bool) Set to True to allow an empty local part (i.e. @example.com),
            e.g. for validating Postfix aliases.
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    allow_smtputf8 = True
    check_deliverability = True
    allow_empty_local = False
    allow_null = True

    def __init__(self, field, allow_smtputf8=True,check_deliverability=True, allow_empty_local=False,
                 allow_null=True, throw_exception=THROW_EXCEPTION):

        self.allow_smtputf8 = allow_smtputf8
        self.check_deliverability = check_deliverability
        self.allow_empty_local = allow_empty_local
        self.allow_null = allow_null

        Validator.__init__(self, field, throw_exception)

    def check_value(self, value):

        if self.allow_null and value is None:
            return True

        try:
            validate_email(value,
                           allow_smtputf8=self.allow_smtputf8,
                           check_deliverability=self.check_deliverability,
                           allow_empty_local=self.allow_empty_local
                           )
            return True
        except EmailNotValidError:
            return False


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
