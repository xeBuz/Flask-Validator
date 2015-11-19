from flask_validator import ValidateString, ValidateInteger, ValidateBoolean, ValidateLength, ValidateNumeric, \
    ValidateEmail, ValidateRegex, ValidateIP, ValidateURL
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
            ip = db.Column(db.String(16))
            url = db.Column(db.String(255))

            def __init__(self, integer, numeric, string, int_exception, boolean, email, regex, ip, url):
                self.integer = integer
                self.numeric = numeric
                self.string = string
                self.int_exception = int_exception
                self.boolean = boolean
                self.email = email
                self.regex = regex
                self.ip = ip

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
                ValidateIP(DummyModel.ip)
                ValidateURL(DummyModel.url)

        db.create_all()

        self.DummyModel = DummyModel
        self.dummy = self.DummyModel(1, 3.1, "aaa", 42, True, "this@email.com", "Hello", "127.0.0.1",
                                     "http://google.com")
        self.app = app
        self.db = db

    def simple_validate(self, field, new_value, bad_value):

        """
        Simple Validation

        """
        default_value = getattr(self.dummy, field)
        setattr(self.dummy, field, new_value)

        self.assertEqual(getattr(self.dummy, field), new_value)

        setattr(self.dummy, field, bad_value)
        self.assertEqual(getattr(self.dummy, field), new_value)

        setattr(self.dummy, field, default_value)
        self.assertNotEquals(getattr(self.dummy, field), new_value)

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
        self.simple_validate('integer', 42, 'bad wolf')

    def test_numeric(self):

        """
        Testing NumericValidator

        """
        self.simple_validate('numeric', 1.111, 'bad wolf')

        default_value = self.dummy.numeric
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

        self.simple_validate('string', "Magnolia", 3.141592)

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

        self.simple_validate('boolean', False, "Not-A-Boolean")

    def test_length(self):

        """
        Testing Max Length Validator
        """

        self.simple_validate('string', "Magnolia", "Magnolia"*100)
        self.simple_validate('string', "Magnolia", "-")

    def test_email(self):

        """
        Testing EmailConstraint()

        """
        self.simple_validate('email', "test@gmail.com", "not@")

    def test_regex(self):

        """
        Testing Regex Validator
        """

        self.simple_validate('regex', "Testing", " ")

    def test_ip(self):

        """
        Testing Regex Validator
        """

        self.simple_validate('ip', "255.255.255.0", " ")

    def test_url(self):

        """
        Testing URL Validator
        """

        self.simple_validate('url', "https://yahoo.com.ar", "Google")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ConstraintTest))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
