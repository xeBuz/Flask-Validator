Exception Message
=================


You will be able to create customs exception messages, with a few variables availables:

* ``field``: Object and property
* ``key``: property
* ``new_value``: New value changed
* ``old_value``: Previous value



.. code-block:: python

    from flask_validator import ValidateEmail

    validator = ValidateEmail(field, False, True, 'Message: Field {field}, Key {key}, New value {new_value}, Old value {old_value}')

