""" FlaskValidator tests """

from flask_validator import ValidateInteger, ValidateString, ValidateInteger, ValidateBoolean, \
    ValidateLength, ValidateNumeric, ValidateEmail, ValidateRegex, ValidateIP, ValidateURL, \
    ValidateUUID, ValidateLessThan, ValidateGreaterThan, ValidateLessThanOrEqual, \
    ValidateGreaterThanOrEqual, ValidateCountry, ValidateTimezone, ValidateLocale, ValidateError, \
    ValidateCreditCard, ValidateCurrency, ValidateIBAN, ValidateISBN, ValidateRange, \
    ValidateNumber, ValidateBIC
import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class ConstraintTest(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db = SQLAlchemy(app)

        class DummyModel(db.Model):
            """ SQLAlchemy Dummy Object """

            id = db.Column(db.Integer, primary_key=True)
            integer = db.Column(db.Integer())
            large = db.Column(db.Integer())
            numeric = db.Column(db.Float())
            numeric_raise = db.Column(db.Float())
            string = db.Column(db.String(80))
            int_exception = db.Column(db.Integer())
            str_exception = db.Column(db.String(20))
            boolean = db.Column(db.Boolean())
            email = db.Column(db.String(80))
            regex = db.Column(db.String(10))
            ip = db.Column(db.String(16))
            ipv6 = db.Column(db.String(100))
            url = db.Column(db.String(255))
            uuid = db.Column(db.String(255))
            country = db.Column(db.String(50))
            timezone = db.Column(db.String(100))
            locale = db.Column(db.String(20))
            creditcard = db.Column(db.String(20))
            currency = db.Column(db.String(3))
            iban = db.Column(db.String(100))
            bic = db.Column(db.String(100))
            isbn = db.Column(db.String(100))
            null = db.Column(db.String(1))
            temporal = db.Column(db.String(5))
            rangefield = db.Column(db.Integer())
            nan = db.Column(db.Float)

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
        self.dummy.integer = 100
        self.dummy.large = 1000
        self.dummy.numeric = 3.1
        self.dummy.numeric_raise = 1
        self.dummy.string = "Test"
        self.dummy.int_exception = 42
        self.dummy.str_exception = "Baggings"
        self.dummy.boolean = True
        self.dummy.email = "test@gmail.com"
        self.dummy.regex = "Aa"
        self.dummy.ip = "127.0.0.1"
        self.dummy.ipv6 = '2001:0db8:0a0b:12f0:0000:0000:0000:0001'
        self.dummy.url = "http://yahoo.com"
        self.dummy.uuid = "19eb35868a8247a4a911758a62601cf2"
        self.dummy.country = 'Argentina'
        self.dummy.timezone = 'UTC'
        self.dummy.locale = 'en_us'
        self.dummy.creditcard = 378282246310005  # PayPal Example
        self.dummy.currency = 'USD'
        self.dummy.iban = 'GB82 WEST 1234 5698 7654 32'
        self.dummy.bic = 'DABAIE2D'
        self.dummy.isbn = '1-56619-909-3'
        self.dummy.null = 'A'
        self.dummy.temporal = 'abcd'
        self.dummy.rangefield = 12
        self.dummy.nan = float(1.2)

    def define_validators(self):
        """
        Define Validators

        """
        ValidateInteger(self.DummyModel.integer)
        ValidateLessThan(self.DummyModel.integer, 100000)
        ValidateLessThanOrEqual(self.DummyModel.integer, 99999)
        ValidateInteger(self.DummyModel.int_exception, True, True)
        ValidateString(self.DummyModel.str_exception, True, True, "Test Message")
        ValidateNumeric(self.DummyModel.numeric)
        ValidateString(self.DummyModel.string)
        ValidateBoolean(self.DummyModel.boolean)
        ValidateLength(self.DummyModel.string, 10, 2)
        ValidateEmail(self.DummyModel.email)
        ValidateRegex(self.DummyModel.regex, "[A-Z][a-z]+")
        ValidateIP(self.DummyModel.ip)
        ValidateIP(self.DummyModel.ipv6, True)
        ValidateURL(self.DummyModel.url)
        ValidateUUID(self.DummyModel.uuid)
        ValidateCountry(self.DummyModel.country)
        ValidateTimezone(self.DummyModel.timezone)
        ValidateLocale(self.DummyModel.locale)
        ValidateGreaterThan(self.DummyModel.large, 100)
        ValidateGreaterThanOrEqual(self.DummyModel.large, 101)
        ValidateCreditCard(self.DummyModel.creditcard)
        ValidateCurrency(self.DummyModel.currency)
        ValidateIBAN(self.DummyModel.iban)
        ValidateISBN(self.DummyModel.isbn)
        ValidateBIC(self.DummyModel.bic)
        ValidateString(self.DummyModel.null, True)
        self.rangevalues = [11, 12, 13]
        ValidateRange(self.DummyModel.rangefield, self.rangevalues)
        ValidateNumber(self.DummyModel.nan)

    def test_integer(self):
        """
        Testing IntegerConstraint

        """
        self.simple_validate('integer', 42, 'bad wolf')

    def test_comparision_lesser(self):
        """
        Testing ValidateLesserThan and ValidateLesserThanOrEqual

        """
        self.simple_validate('integer', 42, 1000000000)

    def test_comparision_greater(self):
        """
        Testing ValidateGreaterThan and ValidateGreaterThanOrEqual

        """
        self.simple_validate('large', 101, 10)

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
        Testing StringConstraint

        """
        self.simple_validate('string', "Magnolia", 3.141592)

    def test_exception(self):
        """
        Testing IntegerConstraint() with exceptions

        """
        default_value = self.dummy.int_exception
        with self.assertRaises(ValidateError):
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

    def test_length_raise(self):
        """
        Testing Length  - Raise Warning

        """
        with self.assertRaises(Warning):
            ValidateLength(self.DummyModel.numeric_raise)
            self.dummy.numeric_raise = 111

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

        with self.assertRaises(AttributeError):
            ValidateRegex(self.DummyModel.regex, "aa(aa")
            self.dummy.regex = 'nope'

    def test_ip(self):
        """
        Testing IP Validator
        """

        self.simple_validate('ip', "255.255.255.0", "12.2.1")

        self.simple_validate('ipv6', "2001:db8:a0b:12f0::1", "255.255.255.0")

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

    def test_country(self):
        """
        Testing Country
        """

        self.simple_validate('country', 'Finland', "Murrica")

    def test_timezone(self):
        """
        Testing Timezone
        """

        self.simple_validate('timezone', 'GMT', "NotTZ")

    def test_timezone_brit(self):
        """
        Testing Locale
        """

        self.simple_validate('locale', 'ES_AR', "BRITISH")

    def test_creditcard(self):
        """
        Testing CreditCard
        """

        self.simple_validate('creditcard', '4111 1111 1111 1111', "202")
        self.simple_validate('creditcard', '4111-1111-1111-1111', "11111")

    def test_currency(self):
        """
        Testing Currency
        """

        self.simple_validate('currency', 'EGP', "$$$")

    def test_iban(self):
        """
        Testing IBAN
        """

        self.simple_validate('iban', 'GB82WEST12345698765432', "DX89 3704 0044 0532 0130 00")

    def test_isbn(self):
        """
        Testing ISBN
        """

        self.simple_validate('isbn', '978-3-16-148410-0', "111112")

    def test_bic(self):
        """
        Testing BIC
        """

        self.simple_validate('bic', 'PBNKDEFFXXX', "d")

    def test_null(self):
        """
        Testing allow_null
        """

        self.simple_validate('null', None, 1.1)

    def test_delete(self):
        """
        Testing Delete
        """
        valid = ValidateString(self.DummyModel.temporal)
        self.simple_validate('temporal', 'bbb', 123)

        valid.stop()
        self.dummy.temporal = 123
        self.assertEqual(self.dummy.temporal, 123)

        self.dummy.temporal = "aaa"
        valid.start()
        self.simple_validate('temporal', 'bbb', 123)

    def test_exception_with_message(self):
        """
        Testing StringValidate() with exceptions and messages

        """

        default_value = self.dummy.str_exception
        with self.assertRaises(ValidateError):
            self.dummy.str_exception = 42
            self.assertEqual(self.dummy.str_exception, default_value)

    def test_range(self):
        """
        Test Range
        """
        self.simple_validate('rangefield', 11, 1)

    def test_isnan(self):
        """
        Test NaN
        """
        self.simple_validate('nan', float(0), float(False))

def suite():
    """ Test Suite """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ConstraintTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
