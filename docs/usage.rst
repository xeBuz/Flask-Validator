Basic Usage
====================



.. code-block:: python
    class User(db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer, primary_key=True)
        string = db.Column(db.String(80))
        integer = db.Column(db.Integer())

        def __init__(self, string, integer):
            self.string = string
            self.integer = integer

        @classmethod
        def __declare_last__(cls):
            Validator(User.integer, IntegerConstraint())
            # The third parameter throw a ValidError exception
            Validator(User.string, StringConstraint(), True)

            .. note:: Markdown doesn't support a lot of the features of Sphinx,
          like inline markup and directives.
          However, it works for basic prose content.

