Custom Validators
=================


You will be able to create customs validator implementing the class Validator.

You must define your own method ``check_value()`` and if you are receiving any argument, you also must call the parent ``__init__()``


.. code-block:: python

    from flask_validator import Validator

    class ValidateAorB(Validator)
        def __init__(self, field, useless, allow_null=True, throw_exception=False, message=None):
            self.useless = useless

            Validator.__init__(self, field, allow_null, throw_exception, message):

        def check_value(self, value):
            retunr if value in ['A', 'B']


    validator = ValidateAorB('yadayada')

