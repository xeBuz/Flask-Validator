Basic Usage
====================


Basic usage. I strongly recomment the validation



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
         Validator(User.integer, IntegerConstraint())
         # The third parameter throw a ValidError exception
         Validator(User.string, StringConstraint(), True)

