Validators availables
=====================


At the moment, the library support this validations:

* Types

  * :ref:`in_integer`
  * :ref:`in_numeric`
  * :ref:`in_string`
  * :ref:`in_boolean`

* Numeric

  * :ref:`in_lenght`

* Comparision

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

* Finantial

  * :ref:`in_creditcard`
  * :ref:`in_currency`
  * :ref:`in_iban`

* Others

  * :ref:`in_isbn`
  * :ref:`in_uuid`
  * :ref:`in_regex`


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

.. _in_integer:

ValidateInteger
---------------

Check if the new value is a valid ``int`` or ``long`` type

Parametes:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+


.. note:: ``long`` type is only available i  Python 2.7


.. _in_numeric:

ValidateNumeric
---------------

Check if the new value is a valid ``int``, ``long``, ``float`` or ``complex`` type


Parametes:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| allow_null              | True     | Allow ``null`` values                                           |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+


.. note:: ``long`` type is only available i  Python 2.7



.. _in_string:

ValidateString
--------------

Check if the new value is a valid ``string`` type.

Parametes:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| allow_null              | True     | Allow ``null`` values                                           |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+



.. _in_boolean:

ValidateBoolean
---------------

Check if the new value is a valid ``bool`` type.

Parametes:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+



.. _in_lenght:

ValidateLenght
--------------

Check if the new value has a lenght with a maximun and a minimun

Parametes:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| max_lenght              | None     | Maximum value lenght                                            |
+-------------------------+----------+-----------------------------------------------------------------+
| min_lenght              | 0        | Minumum value lenght                                            |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+



.. _in_lesser:

ValidateLessThan
----------------

Check if the new value is a lesser than X value

Parametes:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| value                   |          | Value to check                                                  |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+


.. _in_lesser_equal:

ValidateLessThanOrEqual
-----------------------

Check if the new value is a lesser than X value or equal

Parametes:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| value                   |          | Value to check                                                  |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+

.. _in_greater:

ValidateGreaterThan
-------------------

Check if the new value is a greater than X value

Parametes:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| value                   |          | Value to check                                                  |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+


.. _in_greater_equal:

ValidateGreaterThanOrEqual
--------------------------

Check if the new value is a greater than X value or equal

Parametes:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| field                   |          | SQLAlchemy column to validate                                   |
+-------------------------+----------+-----------------------------------------------------------------+
| value                   |          | Value to check                                                  |
+-------------------------+----------+-----------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+----------+-----------------------------------------------------------------+



.. _in_email:

ValidateEmail
-------------

Check if the new value is a valid e-mail, using email_validator_ library.

Parametes:

+-------------------------+----------+--------------------------------------------------------------------------------+
| Parameter               | Default  | Description                                                                    |
+=========================+==========+================================================================================+
| field                   |          | SQLAlchemy column to validate                                                  |
+-------------------------+----------+--------------------------------------------------------------------------------+
| allow_smtputf8          | True     | Allow internationalized addresses that would require the SMTPUTF8_ extension.  |
+-------------------------+----------+--------------------------------------------------------------------------------+
| check_deliverability    | True     | Check domain name resolution.                                                  |
+-------------------------+----------+--------------------------------------------------------------------------------+
| allow_empty_local       | False    | Allow an empty local part for validating Postfix aliases.                      |
+-------------------------+----------+--------------------------------------------------------------------------------+
| allow_null              | True     | Allow ``null`` values                                                          |
+-------------------------+----------+--------------------------------------------------------------------------------+
| throw_exception         | False    | Throw a ``ValidateError`` exception on validation fails                        |
+-------------------------+----------+--------------------------------------------------------------------------------+




.. _in_regex:

ValidateRegex
-------------

Compare a value against a regular expresion

Parametes:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+



.. _in_ip:

ValidateIP
----------

Check if the value is a valid IP Address

Parametes:

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


.. _in_url:

ValidateURL
-----------

Check if the value is a valid URL

Parametes:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+



.. _in_uuid:

ValidateUUID
------------

Check if the value is a valid UUUID

Parametes:

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



.. _in_country:

ValidateCountry
---------------

Check if the value is a valid Country. Validation provided by iso3166_. Allowed names:

* Name
* Alpha2
* Alpha3
* Numeric
* Apolitic Name

Parametes:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+


.. _in_timezone:

ValidateTimezone
----------------

Check if the value is a valid Timezone. Validation provided by pytz_


Parametes:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+



.. _in_locale:

ValidateLocale
--------------

Check if the value is a valid Locale.


Parametes:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
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


Parametes:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+

.. _in_currency:

ValidateCurrency
----------------

Check if the new value is a valid Currency

List provided by: https://github.com/iktw/python-currency-list/blob/master/python_currency_dict.py


Parametes:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+


.. _in_iban:

ValidateIBAN
------------

Check if the new value is valid IBAN (International Bank Account Number)

More reference: https://en.wikipedia.org/wiki/International_Bank_Account_Number



Parametes:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+



.. _in_isbn:

ValidateISBN
------------

Check if the new value is valid ISBN (International Standard Book Number). Allows ISBN10 or ISBN13

Validation provided by: isbnlib_
More reference: https://en.wikipedia.org/wiki/International_Standard_Book_Number



Parametes:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| field                   |           | SQLAlchemy column to validate                                   |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+
| throw_exception         | False     | Throw a ``ValidateError`` exception on validation fails         |
+-------------------------+-----------+-----------------------------------------------------------------+


.. _email_validator: https://github.com/JoshData/python-email-validator
.. _SMTPUTF8: https://tools.ietf.org/html/rfc6531
.. _iso3166: https://pypi.python.org/pypi/iso3166
.. _pytz: http://pytz.sourceforge.net/
.. _isbnlib: https://pypi.python.org/pypi/isbnlib/3.5.6