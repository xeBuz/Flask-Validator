from flask_validator import ValidateString, ValidateInteger, ValidateBoolean, ValidateLength, ValidateNumeric, \
    ValidateEmail, ValidateRegex
import unittest
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


class ConstraintTest(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db = SQLAlchemy(app)

        class DummyModel(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            integer = db.Column(db.Integer())
            numeric = db.Column(db.Float())
            string = db.Column(db.String(80))
            int_exception = db.Column(db.Integer())
            boolean = db.Column(db.Boolean())
            email = db.Column(db.String(80))
            email_valid = db.Column(db.String(80))
            regex = db.Column(db.String(10))

            def __init__(self, integer, numeric, string, int_exception, boolean, email, regex):
                self.integer = integer
                self.numeric = numeric
                self.string = string
                self.int_exception = int_exception
                self.boolean = boolean
                self.email = email
                self.regex = regex

            @classmethod
            def __declare_last__(cls):
                ValidateInteger(DummyModel.integer)
                ValidateInteger(DummyModel.int_exception, True, True)
                ValidateNumeric(DummyModel.numeric)
                ValidateString(DummyModel.string)
                ValidateBoolean(DummyModel.boolean)
                ValidateLength(DummyModel.string, 10, 2)
                ValidateEmail(DummyModel.email)
                ValidateRegex(DummyModel.regex, "[A-Z][a-z]+")

        db.create_all()

        self.DummyModel = DummyModel
        self.dummy = self.DummyModel(1, 3.1, "aaa", 42, True, "this@email.com", "Hello")
        self.app = app
        self.db = db

    def test_creation(self):

        """
        Basic test to validate Flask app

        """
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

    def test_numeric(self):

        """
        Testing NumericValidator

        """

        default_value = self.dummy.numeric
        new_value = 1.1111

        self.dummy.numeric = new_value
        self.assertEqual(self.dummy.numeric, new_value)

        self.dummy.numeric = "bad_string"
        self.assertEqual(self.dummy.numeric, new_value)

        new_value = -10
        self.dummy.numeric = new_value
        self.assertEqual(self.dummy.numeric, new_value)

        new_value = complex(1, 1)-complex(1, 1)
        self.dummy.numeric = new_value
        self.assertEqual(self.dummy.numeric, new_value)

        self.dummy.numeric = default_value
        self.assertNotEquals(self.dummy.numeric, new_value)

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

    def test_boolean(self):

        """
        Testing BooleanValidator

        """

        default_value = self.dummy.boolean
        new_value = False

        self.dummy.boolean = new_value
        self.assertEqual(self.dummy.boolean, new_value)

        self.dummy.boolean = "Not-a-Bool"
        self.assertNotEquals(self.dummy.boolean, "Not-a-Bool")
        self.assertEquals(self.dummy.boolean, new_value)

        self.dummy.boolean = default_value
        self.assertNotEquals(self.dummy.boolean, new_value)

    def test_length(self):

        """
        Testing Max Length Validator
        """
        default_value = self.dummy.string
        new_value = "Magnolia"

        self.dummy.string = new_value
        self.assertEqual(self.dummy.string, new_value)

        self.dummy.string = new_value*10
        self.assertEqual(self.dummy.string, new_value)

        self.dummy.string = default_value
        self.assertNotEquals(self.dummy.string, new_value)

        self.dummy.string = '-'  # min 2
        self.assertEquals(self.dummy.string, default_value)

    def test_email(self):

        """
        Testing EmailConstraint()

        """
        default_value = self.dummy.email
        new_value = "test@gmail.com"

        self.dummy.email = new_value
        self.assertEqual(self.dummy.email, new_value)

        self.dummy.email = "not@"
        self.assertEqual(self.dummy.email, new_value)

        self.dummy.email = default_value
        self.assertNotEquals(self.dummy.email, new_value)

    def test_regex(self):

        """
        Testing Regex Validator
        """
        default_value = self.dummy.regex
        new_value = "Testing"

        self.dummy.regex = new_value
        self.assertEqual(self.dummy.regex, new_value)

        self.dummy.regex = "  "
        self.assertEqual(self.dummy.regex, new_value)

        self.dummy.regex = default_value
        self.assertNotEquals(self.dummy.regex, new_value)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ConstraintTest))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
