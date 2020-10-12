""" Validator and FlaskValidator classes """

import weakref
import abc
from sqlalchemy import event
from .exceptions import ValidateError

__version__ = '1.4.2'


class FlaskValidator(object):
    """ Main Flask Validator class

    It contains the validation methods related to Flask
    """

    field = None
    allow_null = True
    throw_exception = False
    message = None

    def __init__(self, field, allow_null, throw_exception, message,
                 interpolate_message, parent):
        """ Initialize a Validator object.

        :type throw_exception: Throw a ValidateError exception
        :param field: Model.field | Column to listen
        :param interpolate_message: Validator interpolates message with
            values from context if True, outputs original message otherwise
        """
        self.parent = weakref.ref(parent)
        self.field = field
        self.allow_null = allow_null
        self.throw_exception = throw_exception
        self.message = message
        self.interpolate_message = interpolate_message
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

        if self.allow_null and value is None:
            return value

        if self.check_value(value):
            return value
        else:
            if self.throw_exception:
                if self.message:
                    if self.interpolate_message:
                        self.message = self.message.format(field=self.field,
                                                           new_value=value,
                                                           old_value=oldvalue,
                                                           key=initiator.key)
                    raise ValidateError(self.message)
                else:
                    raise ValidateError('Value %s from column %s is not valid' % (value, initiator.key))

            return oldvalue

    def __create_event(self):
        """ Create an SQLAlchemy event listening the 'set' in a particular column.

        :rtype : object
        """
        if not event.contains(self.field, 'set', self.__validate):
            event.listen(self.field, 'set', self.__validate, retval=True)

    @abc.abstractmethod
    def check_value(self, value):
        """ Realize the proper validation, int the new value as parameter

        :rtype: Boolean
        :param value:
        """

    def stop(self):
        """ Remove the listener to stop the validation
        """
        if event.contains(self.field, 'set', self.__validate):
            event.remove(self.field, 'set', self.__validate)

    def start(self):
        """ Restart the listener
        """
        if not event.contains(self.field, 'set', self.__validate):
            self.__create_event()


class Validator(FlaskValidator):
    """ Main validotr class """

    def __init__(self, field, allow_null=True, throw_exception=False, message=None, interpolate_message=True):
        """
        Validator Interface initialization

        :param field:  Flask Column to validate
        """

        FlaskValidator.__init__(self, field, allow_null, throw_exception, message, interpolate_message, self)

    @abc.abstractmethod
    def check_value(self, value):
        """
        Validate the new value

        :param value:
        """
