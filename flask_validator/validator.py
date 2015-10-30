from sqlalchemy import event

__version__ = '0.1'

class Validator:
    field = None
    constrain = None

    def __init__(self, field, constraint):
        self.field = field
        self.constraint = constraint
        self.create_event()

    def validate(self, target, value, oldvalue, initiator):
        if self.constraint.check(value):
            return value
        else:
            return oldvalue

    def create_event(self):
        if not event.contains(self.field, 'set', self.validate):
            event.listen(self.field, 'set', self.validate, retval=True)
