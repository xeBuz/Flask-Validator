from flask_validator import Validator, Constraint, IntegerConstraint, StringConstraint
import unittest
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


class ConstraintTest(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        db = SQLAlchemy(app)

        class DummyModel(db.Model):
            __tablename__ = 'dummy'
            id = db.Column(db.Integer, primary_key=True)
            integer = db.Column(db.Integer())
            string = db.Column(db.String(80))

            def __init__(self, integer, string):
                self.integer = integer
                self.string = string

            @classmethod
            def __declare_last__(cls):
                Validator(DummyModel.integer, IntegerConstraint())
                Validator(DummyModel.string, StringConstraint())

        db.create_all()

        self.DummyModel = DummyModel
        self.app = app
        self.db = db

    def test_creation(self):

        # Create a basic model
        self.dummy = self.DummyModel(1, "aaa")

        # Test the values
        assert self.dummy.integer == 1
        assert self.dummy.string == "aaa"

        # Persist
        self.db.session.add(self.dummy)
        self.db.session.commit()

        # Validate Again
        assert self.dummy.integer == 1
        assert self.dummy.string == "aaa"




def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ConstraintTest))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
