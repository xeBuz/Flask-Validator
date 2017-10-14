""" FlaskValidator example """

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_validator import ValidateInteger, ValidateString

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


class User(db.Model):
    """ User SQLAlchemy Model for example """

    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    string = db.Column(db.String(80))
    integer = db.Column(db.Integer())

    def __init__(self, string, integer):
        self.string = string
        self.integer = integer

    @classmethod
    def __declare_last__(cls):
        ValidateInteger(User.integer)
        ValidateString(User.string, False, True, "Custom Message, "
                                                 "Field {field} - Value {value} - Oldvalue {oldvalue} - Key {key}")

db.create_all()
u = User("user", 1)
db.session.add(u)
db.session.commit()
