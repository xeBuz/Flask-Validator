from flask_validator import Validator


class ValidateCreditCard(Validator):
    """ Validate Credit Card Number

    Check if the new value is valida credit card number.
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
        n = str(value).translate(None, ' -')
        r = [int(ch) for ch in str(n)][::-1]
        return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0


class CurrencyConstraint(Validator):
    # TODO
    def check_value(self, value):
        pass


class LuhnConstraint(Validator):
    # TODO
    def check_value(self, value):
        pass


class IbanConstraint(Validator):
    # TODO
    def check_value(self, value):
        pass


class IsbnConstraint(Validator):
    # TODO
    def check_value(self, value):
        pass


class IssnConstraint(Validator):
    # TODO
    def check_value(self, value):
        pass