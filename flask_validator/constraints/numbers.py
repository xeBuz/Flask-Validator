from flask_validator import Validator


class ValidateLength(Validator):
    """ Validate Length type.

    Check if the new value has a proper length

    Args:
        field: SQLAlchemy column to validate
        max_length: (int) Maximum value length
        min_lenght: (int) Minimum value length
        throw_exception: (bool) Throw a ValidateError if the validation fails

    """

    max_length = None
    min_lenght = 0

    def __init__(self, field, max_length=None, min_length=0, throw_exception=False):
        self.max_length = max_length
        self.min_lenght = min_length

        Validator.__init__(self, field, False, throw_exception)

    def check_value(self, value):

        if not self.max_length:
            raise Warning("Argument max_length should't be null")

        return int(self.max_length) >= len(value) >= int(self.min_lenght)
