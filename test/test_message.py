""" FlaskValidator tests """

import unittest

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_validator import Validator


class MessageTest(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db = SQLAlchemy(app)

        class DummyModel(db.Model):
            """ SQLAlchemy Dummy Object """

            id = db.Column(db.Integer, primary_key=True)
            integer = db.Column(db.Integer)

        db.create_all()

        self.DummyModel = DummyModel
        self.define_validators()

        self.dummy = DummyModel()

        self.app = app
        self.db = db

    def simple_validate(self, field, value):
        """
        Simple Validation

        """
        setattr(self.dummy, field, value)

    def define_validators(self):
        """
        Define Validators

        """
        class FailValidator(Validator):
            def check_value(self, value):
                return False

        FailValidator(self.DummyModel.integer, throw_exception=True,
                      message="{do} {not} {interpolate} {this}",
                      interpolate_message=False)

    def test_disable_message_interpolation(self):
        """
        Testing FlaskValidator.interpolate_message

        """
        with self.assertRaises(Exception) as context:
            self.simple_validate('integer', 1)

        self.assertEqual("{do} {not} {interpolate} {this}",
                         str(context.exception))


def suite():
    """ Test Suite """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MessageTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
