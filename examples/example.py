from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_validator import Validator, IntegerConstraint, StringConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    string = db.Column(db.String(80))
    integer = db.Column(db.Integer())

    def __init__(self, string, integer):
        print 'User init'
        self.string = string
        self.integer = integer

    @classmethod
    def __declare_last__(cls):
        Validator(User.integer, IntegerConstraint())
        Validator(User.string, StringConstraint())

db.create_all()
u = User("user", 1)
db.session.add(u)
db.session.commit()
