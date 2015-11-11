# Flask-Validator
[![Travis](https://travis-ci.org/xeBuz/Flask-Validator.svg)](https://travis-ci.org/xeBuz/Flask-Validator)
[![Code Climate](https://codeclimate.com/github/xeBuz/Flask-Validator/badges/gpa.svg)](https://codeclimate.com/github/xeBuz/Flask-Validator) 
[![Documentation Status](https://readthedocs.org/projects/flask-validator/badge/?version=latest)](http://flask-validator.readthedocs.org/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/xeBuz/Flask-Validator/badge.svg?branch=master&service=github)](https://coveralls.io/github/xeBuz/Flask-Validator?branch=master)


------

## Description

Data validator for Flask using SQL-Alchemy, working at Model component with events, preventing invalid data in the columns.

## Instalation

```bash
pip install flask-validator
```


## Documentation

For the online documentation, follow [this link](http://flask-validator.readthedocs.org/en/latest/)


## Basic usage

```python
from flask_validator import ValidateInteger, ValidateString

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
        ValidateString(User.string)
```


## Allowed Constraints

- ValidateInteger
- ValidateNumeric
- ValidateString
- ValidateBoolean
- ValidateMaxLenght






