
class Constraint:
    params = {
        'allow_null': True
    }

    def __init__(self, params=None):
        """
        Create a base Constraint Object

        :param params: Extra options / payload
        """
        if params:
            self.params = self._merge_params(params)

    def _merge_params(self, params):
        temp = self.params.copy()
        temp.update(params)
        return temp

    def check(self, value):
        pass


class TypeConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class BooleanConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class IntegerConstraint(Constraint):

    def check(self, value):
        return isinstance(value, (int, long))


class StringConstraint(Constraint):

    def check(self, value):
        return isinstance(value, str)


class NotNullConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class NullConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class EmailConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class LengthConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class URLConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class RegexConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class IPConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class UUIDConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class LessThanConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class LessThanOrEqualConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class GreaterThanConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class GreaterThanOrEqualConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class RangeConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class DateConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class TimeConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class DateTimeConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class LenguageConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class LocaleConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class CountryConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class CardConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class CurrencyConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class LuhnConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class IbanConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class IsbnConstraint(Constraint):
    # TODO
    def check(self, value):
        pass


class IssnConstraint(Constraint):
    # TODO
    def check(self, value):
        pass
