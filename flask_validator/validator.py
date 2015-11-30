from sqlalchemy import event
from .exceptions import ValidateError

__version__ = '0.9'


class FlaskValidator:
    field = None
    allow_null = True
    throw_exception = False

    def __init__(self, field, allow_null, throw_exception):
        """ Initialize a Validator object.

        :type throw_exception: Throw a ValidateError exception
        :param field: Model.field | Column to listen
        """
        self.field = field
        self.allow_null = allow_null
        self.throw_exception = throw_exception

        self.__create_event()

    def __validate(self, target, value, oldvalue, initiator):
        """ Method executed when the event 'set' is triggered.

        :param target: Object triggered
        :param value: New value
        :param oldvalue: Previous value
        :param initiator: Column modified

        :return: :raise ValidateError:
        """
        if value == oldvalue:
            return value

        if self.check_value(value):
            return value
        else:
            if self.allow_null and value is None:
                return value

            if self.throw_exception:
                raise ValidateError('Value %s from column %s is not valid' % (value, initiator.key))

            return oldvalue

    def __create_event(self):
        """ Create an SQLAlchemy event listening the 'set' in a particular column.

        :rtype : object
        """
        if not event.contains(self.field, 'set', self.__validate):
            event.listen(self.field, 'set', self.__validate, retval=True)

    def _merge_params(self, allowed_params):
        """ Merge default parameters with the specific parameter validator.

        :param allowed_params: array with valid parameters
        :return:  array with a merge without duplicated values
        """
        return list(set(self.default_params + allowed_params))

    def check_value(self, value):
        """ Realize the proper validation, int the new value as parameter

        :rtype: Boolean
        :param value:
        """
        pass


class Validator(FlaskValidator):

    def __init__(self, field, allow_null=True, throw_exception=False):
        """
        Validator Interface initialization

        :param field:  Flask Column to validate
        """

        FlaskValidator.__init__(self, field, allow_null, throw_exception)

    def check_value(self, value):
        """
        Validate the new value

        :param value:
        """
        pass