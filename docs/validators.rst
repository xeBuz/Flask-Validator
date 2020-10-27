Validators available
====================


At the moment, the library supports these validations:

* Types

  * :ref:`in_integer`
  * :ref:`in_numeric`
  * :ref:`in_string`
  * :ref:`in_boolean`

* Numeric

  * :ref:`in_length`
  * :ref:`in_nan`

* Comparison

  * :ref:`in_lesser`
  * :ref:`in_lesser_equal`
  * :ref:`in_greater`
  * :ref:`in_greater_equal`

* Internet

  * :ref:`in_email`
  * :ref:`in_ip`
  * :ref:`in_url`

* Location

  * :ref:`in_country`
  * :ref:`in_timezone`
  * :ref:`in_locale`

* Financial

  * :ref:`in_creditcard`
  * :ref:`in_currency`
  * :ref:`in_iban`
  * :ref:`in_bic`

* Others

  * :ref:`in_isbn`
  * :ref:`in_uuid`
  * :ref:`in_regex`
  * :ref:`in_range`


.. _in_integer:

ValidateInteger
---------------

Check if the new value is a valid ``int`` or ``long`` type

Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+

.. note:: ``long`` type is only available in Python 2.7


.. _in_numeric:

ValidateNumeric
---------------

Check if the new value is a valid ``int``, ``long``, ``float`` or ``complex`` type


Parameters:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| allow_null              | True     | Allow ``null`` values                                           |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+
| message                 | None     | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+----------+-----------------------------------------------------------------+


.. note:: ``long`` type is only available i  Python 2.7



.. _in_string:

ValidateString
--------------

Check if the new value is a valid ``string`` type.

Parameters:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| allow_null              | True     | Allow ``null`` values                                           |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+
| message                 | None     | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+----------+-----------------------------------------------------------------+



.. _in_boolean:

ValidateBoolean
---------------

Check if the new value is a valid ``bool`` type.

Parameters:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+
| message                 | None     | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+----------+-----------------------------------------------------------------+



.. _in_length:

Validatelength
--------------

Check if the new value has a length with a maximum and a minimum

Parameters:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| max_length              | None     | Maximum value length                                            |
+-------------------------+----------+-----------------------------------------------------------------+
| min_length              | 0        | Minimum value length                                            |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+
| message                 | None     | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+----------+-----------------------------------------------------------------+


.. _in_nan:

ValidateNumber
--------------

Check if the new value is a number or not (NaN)

Parameters:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+
| message                 | None     | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+----------+-----------------------------------------------------------------+


.. _in_lesser:

ValidateLessThan
----------------

Check if the new value is less than the value of X

Parameters:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| value                   |          | Value to check                                                  |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+
| message                 | None     | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+----------+-----------------------------------------------------------------+



.. _in_lesser_equal:

ValidateLessThanOrEqual
-----------------------

Check if the new value is less than or equal to the value of X

Parameters:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| value                   |          | Value to check                                                  |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+
| message                 | None     | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+----------+-----------------------------------------------------------------+


.. _in_greater:

ValidateGreaterThan
-------------------

Check if the new value is greater than the value of X

Parameters:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| value                   |          | Value to check                                                  |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+
| message                 | None     | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+----------+-----------------------------------------------------------------+



.. _in_greater_equal:

ValidateGreaterThanOrEqual
--------------------------

Check if the new value is greater than or equal to the value of X

Parameters:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| value                   |          | Value to check                                                  |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+
| message                 | None     | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+----------+-----------------------------------------------------------------+



.. _in_email:

ValidateEmail
-------------

Check if the new value is a valid e-mail, using the email_validator_ library.

Parameters:

+-------------------------+----------+--------------------------------------------------------------------------------+
| Parameter               | Default  | Description                                                                    |
+=========================+==========+================================================================================+
| field                   |          | SQLAlchemy column to validate                                                  |
+-------------------------+----------+--------------------------------------------------------------------------------+
| allow_smtputf8          | True     | Allow internationalized addresses that would require the SMTPUTF8_ extension  |
+-------------------------+----------+--------------------------------------------------------------------------------+
| check_deliverability    | True     | Check domain name resolution                                                  |
+-------------------------+----------+--------------------------------------------------------------------------------+
| allow_empty_local       | False    | Allow an empty local part for validating Postfix aliases                      |
+-------------------------+----------+--------------------------------------------------------------------------------+
| allow_null              | True     | Allow ``null`` values                                                          |
+-------------------------+----------+--------------------------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails                        |
+-------------------------+----------+--------------------------------------------------------------------------------+
| message                 | None     | Add a custom message to the ``ValidateError`` exception                        |
+-------------------------+----------+--------------------------------------------------------------------------------+




.. _in_regex:

ValidateRegex
-------------

Compare a value against a regular expression

Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+


.. _in_range:

ValidateRange
-------------

Check if the new value is in a range

Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| range                   |           | Range values                                                    |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+


.. _in_ip:

ValidateIP
----------

Check if the value is a valid IP Address

Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| ipv6                    | False     | Check IPv6 Address instread of IPv4                             |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+


.. _in_url:

ValidateURL
-----------

Check if the value is a valid URL

Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+



.. _in_uuid:

ValidateUUID
------------

Check if the value is a valid UUUID

Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| version                 | 4         | UUID version                                                    |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+



.. _in_country:

ValidateCountry
---------------

Check if the value is a valid Country. Validation provided by iso3166_. Allowed names:

* Name
* Alpha2
* Alpha3
* Numeric
* Apolitic Name

Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+


.. _in_timezone:

ValidateTimezone
----------------

Check if the value is a valid Timezone. Validation provided by pytz_


Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+



.. _in_locale:

ValidateLocale
--------------

Check if the value is a valid Locale.


Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+



.. _in_creditcard:

ValidateCreditCard
------------------

Check if the new value is valid credit card number.

Allowed formats:
* XXXXYYYYWWWWZZZ
* "XXXXYYYYWWWWZZZ"
* "XXXX YYYY WWWW ZZZ"
* "XXXX-YYYY-WWWW-ZZZ"


Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+



.. _in_currency:

ValidateCurrency
----------------

Check if the new value is a valid Currency

Validation provided by: moneyed_


Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+



.. _in_iban:

ValidateIBAN
------------

Check if the new value is a valid IBAN (International Bank Account Number)

More reference: https://en.wikipedia.org/wiki/International_Bank_Account_Number



Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+


.. _in_iban:

ValidateBIC
------------

Check if the new value is a valid BIC (SO 9362 defined standard format of Bank Identifier Codes)

More reference: https://en.wikipedia.org/wiki/ISO_9362



Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+




.. _in_isbn:

ValidateISBN
------------

Check if the new value is valid ISBN (International Standard Book Number). Allows ISBN10 or ISBN13

Validation provided by: isbnlib_
More reference: https://en.wikipedia.org/wiki/International_Standard_Book_Number



Parameters:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+
| message                 | None      | Add a custom message to the ``ValidateError`` exception         |
+-------------------------+-----------+-----------------------------------------------------------------+



.. _email_validator: https://github.com/JoshData/python-email-validator
.. _SMTPUTF8: https://tools.ietf.org/html/rfc6531
.. _iso3166: https://pypi.python.org/pypi/iso3166
.. _pytz: http://pytz.sourceforge.net/
.. _isbnlib: https://pypi.python.org/pypi/isbnlib/3.5.6
.. _moneyed: https://github.com/limist/py-moneyed/
