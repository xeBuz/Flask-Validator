# Flask-Validator
![PyPi status](https://img.shields.io/pypi/status/Flask-Validator.svg)
[![PyPI version](https://badge.fury.io/py/Flask-Validator.svg)](https://badge.fury.io/py/Flask-Validator)
[![Travis](https://travis-ci.org/xeBuz/Flask-Validator.svg)](https://travis-ci.org/xeBuz/Flask-Validator)
[![Documentation Status](https://readthedocs.org/projects/flask-validator/badge/?version=latest)](http://flask-validator.readthedocs.org/en/latest/?badge=latest)
[![Requirements Status](https://requires.io/github/xeBuz/Flask-Validator/requirements.svg?branch=master)](https://requires.io/github/xeBuz/Flask-Validator/requirements/?branch=master)
[![Coverage Status](https://coveralls.io/repos/xeBuz/Flask-Validator/badge.svg?branch=master&service=github)](https://coveralls.io/github/xeBuz/Flask-Validator?branch=master)
[![](https://landscape.io/github/xeBuz/Flask-Validator/master/landscape.svg?style=flat)](https://landscape.io/github/xeBuz/Flask-Validator/master)
[![Code Climate](https://codeclimate.com/github/xeBuz/Flask-Validator/badges/gpa.svg)](https://codeclimate.com/github/xeBuz/Flask-Validator) 


------

## Description

Data validator for Flask using SQL-Alchemy, working at Model component with events, preventing invalid data in the columns.
The extension works with event listeners form SQLAlchemy.

## Instalation

```bash
pip install flask-validator
```


## Documentation

For the online documentation, follow [this link](http://flask-validator.readthedocs.org/en/latest/)


## Basic usage

The most performant way to set up your validations is uring the SQLAlchemy special  directive_ ``__declare_last__``, it occurs after mappings are assumed to be completed and the ‘configure’ step has finished.

```python
from flask_validator import ValidateInteger, ValidateString, ValidateEmail

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    code = db.Column(db.Integer())
    email = db.Column(db.String(125))

    def __init__(self, string, integer):
        self.string = string
        self.integer = integer

    @classmethod
    def __declare_last__(cls):
        ValidateString(User.name)
        ValidateInteger(User.code)
        ValidateEmail(User.email)
        
user = User('Arthur Dent', 42, 'arthur@babelfish.org')

user.name = 666
print user.name 
# 'Arthur Dent'
user.name = 'Zaphod Beeblebrox'
print user.name
# 'Zaphod Beeblebrox'
```


## Exceptions

Every Constraint has a parameter to throw an exception everytime the validation fails, for example:

```python
ValidateNumeric(Table.field, False, True, "Message")
```

The third parameter enables this feature and throw a `ValidateError` exception, otherwise it will fails silently.


## Message Exception

The fourth parameter allow a custom message exception, with a few variables available

- `old_value`: value previous to the modification
- `new_value`: value provided (with the error)
- `key`: the column name
- `field`: object.column


## Available Constraints

- Types
  - ValidateInteger
  - ValidateNumeric
  - ValidateString
  - ValidateBoolean
- Numeric
  - ValidateLenght
- Comparision
  - ValidateLessThan
  - ValidateLessThanOrEqual
  - ValidateGreaterThan
  - ValidateGreaterThanOrEqual
- Internet
  - ValidateEmail
  - ValidateIP
  - ValidateURL
- Location
  - ValidateCountry
  - ValidateTimezone
  - ValidateLocale
- Finantial
  - ValidateCreditCard
  - ValidateCurrency
  - ValidateIBAN
- Others 
  - ValidateUUID
  - ValidateISBN
  - ValidateRegex


## Custom Validators


You will be able to create customs validator implementing the class Validator.

You must define your own method ``check_value()`` and if you are receiving any argument, you also must call the parent ``__init__()``


```python
from flask_validator import Validator

class ValidateAorB(Validator)
    def __init__(self, field, useless, allow_null=True, throw_exception=False, message=None):
        self.useless = useless

        Validator.__init__(self, field, allow_null, throw_exception, message):

    def check_value(self, value):
        retunr if value in ['A', 'B']
        
class ValidateA(Validator)
    def check_value(self, value):
        retunr if value == 'A'
```            
           
            
## Pause the validation

The extension has two methods to stop and restart the listener. 

```python
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    code = db.Column(db.Integer())
    email = db.Column(db.String(125))

    def __init__(self, string, integer):
        self.string = string
        self.integer = integer

# Initialize the validator
validate =  ValidateString(User.name)

# Do something validated
# ...

validate.stop()

# Assign values without being validated
# ...

validate.start()

# Re-enabled the listener

```



