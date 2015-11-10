Basic Usage
====================


Basic usage. I strongly recommend the validation


    from flask_validator import ValidateInteger, ValidateString

    class User(db.Model):
      _tablename__ = 'user'
      id = db.Column(db.Integer, primary_key=True)
      string = db.Column(db.String(80))
      integer = db.Column(db.Integer())

      def __init__(self, string, integer):
         self.string = string
         self.integer = integer

      @classmethod
      def __declare_last__(cls):
         ValidateInteger(User.integer)
         ValidateString(User.string, throw_exception=True)

