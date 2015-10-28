
class Constraint:
    params = None
    exception = None

    def __init__(self, params=[], exception=False):
        self.params = params
        self.exception = exception

    def check(self, value):
        return value


class IntegerConstraint(Constraint):

    def check(self, value):
        return isinstance(value, (int, long))


class StringConstraint(Constraint):

    def check(self, value):
        return isinstance(value, str)