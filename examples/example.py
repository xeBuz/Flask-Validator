from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_validator import ValidateInteger, ValidateString

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    string = db.Column(db.String(80))
    integer = db.Column(db.Integer())

    def __init__(self, string, integer):
        self.string = string
        self.integer = integer

    @classmethod
    def __declare_last__(cls):
        ValidateInteger(User.integer)
        ValidateString(User.string, False, True, "Custom Message")

db.create_all()
u = User("user", 1)
db.session.add(u)
db.session.commit()
