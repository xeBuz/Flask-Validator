from flask_validator import Validator, Constraint, IntegerConstraint, StringConstraint
import unittest
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


class ConstraintTest(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/tes1t.db'
        db = SQLAlchemy(app)

        class DummyModel(db.Model):
            __tablename__ = 'dummy'
            id = db.Column(db.Integer, primary_key=True)
            integer = db.Column(db.Integer())
            string = db.Column(db.String(80))
            int_exception = db.Column(db.Integer())

            def __init__(self, integer, string, int_exception):
                self.integer = integer
                self.string = string
                self.int_exception = int_exception

            @classmethod
            def __declare_last__(cls):
                Validator(DummyModel.integer, IntegerConstraint())
                Validator(DummyModel.string, StringConstraint())
                Validator(DummyModel.int_exception, IntegerConstraint(), True)

        db.create_all()

        self.DummyModel = DummyModel
        self.dummy = self.DummyModel(1, "aaa", 42)

        self.app = app
        self.db = db

    def test_creation(self):

        """
        Basic test to validate Flask app

        """
        self.dummy = self.DummyModel(1, "aaa", 42)

        # Test the values
        assert self.dummy.integer == 1
        assert self.dummy.string == "aaa"

        # Persist
        self.db.session.add(self.dummy)
        self.db.session.commit()

        # Validate Again
        assert self.dummy.integer == 1
        assert self.dummy.string == "aaa"

    def test_integer(self):

        """
        Testing IntegerConstraint()

        """
        default_value = self.dummy.integer
        new_value = 42

        self.dummy.integer = new_value
        self.assertEqual(self.dummy.integer, new_value)

        self.dummy.integer = "bad_string"
        self.assertEqual(self.dummy.integer, new_value)

        self.dummy.integer = default_value
        self.assertNotEquals(self.dummy.integer, new_value)

    def test_string(self):

        """
        Testing StringConstraint()

        """
        default_value = self.dummy.string
        new_value = "Magnolia"

        self.dummy.string = new_value
        self.assertEqual(self.dummy.string, new_value)

        self.dummy.string = 3.141592
        self.assertEqual(self.dummy.string, new_value)

        self.dummy.string = default_value
        self.assertNotEquals(self.dummy.string, new_value)

    def test_exception(self):

        """
        Testing IntegerConstraint() with exceptions

        """
        default_value = self.dummy.int_exception
        with self.assertRaises(ValueError):
            self.dummy.int_exception = "Doctor"
            self.assertEqual(self.dummy.int_exception, default_value)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ConstraintTest))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
