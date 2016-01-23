Basic Usage
====================


The most performant way to set up your validations is uring the SQLAlchemy special  directive_ ``__declare_last__``, it occurs after mappings are assumed to be completed and the ‘configure’ step has finished.
With this method, you will create the event one tine, just before the class creation.

The only required argument is the Column to validate.


.. code-block:: python

    # import ...
    from flask_validator import ValidateInteger, ValidateString, ValidateEmail

    class User(db.Model):
      _tablename__ = 'user'
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(80))
      code = db.Column(db.Integer())
      email = db.Column(db.String(125))

      def __init__(self, string, integer):
          self.string = string
          self.integer = integer

      @classmethod
      def __declare_last__(cls):
          ValidateString(User.name)
          ValidateInteger(User.code)
          ValidateEmail(User.email, true, true, "The e-mail is not valid. Please check it")


With that code, the Validator will execute an ORM event_ listening each field modification

.. _directive: http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/api.html#declare-last
.. _event: http://docs.sqlalchemy.org/en/latest/orm/events.html