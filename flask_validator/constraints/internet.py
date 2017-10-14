""" Internet Validators 

- ValidateEmail
- ValidateIP
- ValidateURL
"""

import socket
import re
from email_validator import validate_email, EmailNotValidError
from flask_validator import Validator


class ValidateEmail(Validator):
    """ Validate Email type.

    Check if the new value is a valid e-mail.
    Using this library to validate https://github.com/JoshData/python-email-validator

    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        allow_smtputf8: (bool) Set to False to prohibit internationalized addresses that would require the SMTPUTF8.
        check_deliverability: (bool) Set to False to skip the domain name resolution check.
        allow_empty_local (bool) Set to True to allow an empty local part (i.e. @example.com),
            e.g. for validating Postfix aliases.
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails

    """

    allow_smtputf8 = True
    check_deliverability = True
    allow_empty_local = False

    def __init__(self, field, allow_smtputf8=True,check_deliverability=True, allow_empty_local=False,
                 allow_null=True, throw_exception=False, message=None):

        self.allow_smtputf8 = allow_smtputf8
        self.check_deliverability = check_deliverability
        self.allow_empty_local = allow_empty_local

        Validator.__init__(self, field, allow_null, throw_exception, message)

    def check_value(self, value):
        try:
            validate_email(value,
                           allow_smtputf8=self.allow_smtputf8,
                           check_deliverability=self.check_deliverability,
                           allow_empty_local=self.allow_empty_local)
            return True
        except EmailNotValidError:
            return False


class ValidateIP(Validator):
    """ Validate Regex

    Compare a value against a regular expresion

    Args:
        field: SQLAlchemy column to validate
        ipv6: Match against IPV6
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails
    """
    ipv6 = None

    def __init__(self, field, ipv6=False, allow_null=True, throw_exception=False, message=None):
        self.ipv6 = ipv6

        Validator.__init__(self, field, allow_null, throw_exception, message)

    def check_value(self, value):
        try:
            if not self.ipv6:
                socket.inet_pton(socket.AF_INET, value)
            else:
                socket.inet_pton(socket.AF_INET6, value)

            return True
        except socket.error:
            return False


class ValidateURL(Validator):
    """ Validate URL

    Check if the values is a valid URL

    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values. Default True
        throw_exception: (bool) Throw a ValidateError if the validation fails

    """

    regex = r'^[a-z]+://(?P<host>[^/:]+)(?P<port>:[0-9]+)?(?P<path>\/.*)?$'

    def check_value(self, value):
        if re.match(self.regex, value):
            return True
        else:
            return False
