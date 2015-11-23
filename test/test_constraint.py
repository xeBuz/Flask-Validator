from flask_validator import ValidateInteger, ValidateString, ValidateInteger, ValidateBoolean, ValidateLength, \
    ValidateNumeric, ValidateEmail, ValidateRegex, ValidateIP, ValidateURL, ValidateUUID, ValidateLessThan
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
            regex = db.Column(db.String(10))
            ip = db.Column(db.String(16))
            url = db.Column(db.String(255))
            uuid = db.Column(db.String(255))

        db.create_all()

        self.DummyModel = DummyModel
        self.define_validators()

        self.dummy = DummyModel()
        self.set_default_values()

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

    def set_default_values(self):
        """
        Instanciate basic values

        """
        self.dummy.integer = 1
        self.dummy.numeric = 3.1
        self.dummy.string = "Test"
        self.dummy.int_exception = 42
        self.dummy.boolean = True
        self.dummy.email = "test@gmail.com"
        self.dummy.regex = "Aa"
        self.dummy.ip = "127.0.0.1"
        self.dummy.url = "http://yahoo.com"
        self.dummy.uuid = "19eb35868a8247a4a911758a62601cf2"

    def define_validators(self):
        """
        Define Validators

        """
        ValidateInteger(self.DummyModel.integer)
        ValidateLessThan(self.DummyModel.integer, 100000)
        ValidateInteger(self.DummyModel.int_exception, True, True)
        ValidateNumeric(self.DummyModel.numeric)
        ValidateString(self.DummyModel.string)
        ValidateBoolean(self.DummyModel.boolean)
        ValidateLength(self.DummyModel.string, 10, 2)
        ValidateEmail(self.DummyModel.email)
        ValidateRegex(self.DummyModel.regex, "[A-Z][a-z]+")
        ValidateIP(self.DummyModel.ip)
        ValidateURL(self.DummyModel.url)
        ValidateUUID(self.DummyModel.uuid)

    def test_integer(self):
        """
        Testing IntegerConstraint

        """
        self.simple_validate('integer', 42, 'bad wolf')

    def test_comparision(self):
        """
        Testing ValidateLesserThan

        """
        self.simple_validate('integer', 42, 1000000000)

    def test_numeric(self):
        """
        Testing NumericValidator

        """
        self.simple_validate('numeric', 1.111, 'bad wolf')

        default_value = self.dummy.numeric
        new_value = -10
        self.dummy.numeric = new_value
        self.assertEqual(self.dummy.numeric, new_value)

        new_value = complex(1, 1) - complex(1, 1)
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

        self.simple_validate('string', "Magnolia", "Magnolia" * 100)
        self.simple_validate('string', "Magnolia", "-")

    def test_email(self):
        """
        Testing EmailConstraint()

        """
        self.simple_validate('email', "test2@gmail.com", "not@")

    def test_regex(self):
        """
        Testing Regex Validator
        """

        self.simple_validate('regex', "Testing", " ")

    def test_ip(self):
        """
        Testing IP Validator
        """

        self.simple_validate('ip', "255.255.255.0", "12.2.1")

    def test_url(self):
        """
        Testing URL Validator
        """

        self.simple_validate('url', "https://yahoo.com.ar", "Google")

    def test_uuid(self):
        """
        Testing UUID
        """

        self.simple_validate('uuid', '12eb35868a8247a4a911758a62601cf2', "notavalidauuid")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ConstraintTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
