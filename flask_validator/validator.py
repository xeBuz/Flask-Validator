from sqlalchemy import event

__version__ = '0.2'


class Validator:
    field = None
    constrain = None
    raise_exception = False

    def __init__(self, field, constraint, raise_exception=False):
        """
        Initialize a Validator object

        :param field: Model.field | Column to listen
        :param constraint:  A valid contraint to validate
        :param raise_exception: Throw an expection or fails silently
        """
        self.field = field
        self.constraint = constraint
        self.raise_exception = raise_exception

        self.create_event()

    def validate(self, target, value, oldvalue, initiator):
        """
        Method executed when the event 'set' is triggered

        :param target: Object triggered
        :param value: New value
        :param oldvalue: Previous value
        :param initiator: Column modified

        :return: :raise ValueError:
        """
        if self.constraint.check(value):
            return value
        else:
            if self.raise_exception:
                raise ValueError('Value %s from column %s is not valid' % (value, initiator.key))
            else:
                return oldvalue

    def create_event(self):
        """
        Create an SQLAlchemy event listening the 'set' in a particular column

        :rtype : object
        """
        if not event.contains(self.field, 'set', self.validate):
            event.listen(self.field, 'set', self.validate, retval=True)
