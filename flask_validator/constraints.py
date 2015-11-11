from flask_validator import FlaskValidator


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

        return isinstance(value, (int, long))


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
    """ Validate String type.

    Check if the new value is a string

    Args:
        value: new value
        max_length: (bool) Maximum value Length
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    max_length = None

    def check_value(self, value):

        if not self.max_length:
            raise Warning("Argument max_length should't be null")

        return len(value) <= int(self.max_length)


class EmailConstraint(Validator):
    # TODO
    def check(self, value):
        pass


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
