Validators availables
=====================


At the moment, the library support this validations:

* :ref:`in_integer`
* :ref:`in_numeric`
* :ref:`in_string`
* :ref:`in_boolean`
* :ref:`in_lenght`
* :ref:`in_email`



.. _in_integer:

ValidateInteger
---------------

Check if the new value is a valid ``int`` or ``long`` type


Optional parametes:

+-------------------------+-----------+-----------------------------------------------------------------+
| Parameter               | Default   | Description                                                     |
+=========================+===========+=================================================================+
| throw_exception         | False     | Throw a ``ValueError`` exception on validation fails            |
+-------------------------+-----------+-----------------------------------------------------------------+
| allow_null              | True      | Allow ``null`` values                                           |
+-------------------------+-----------+-----------------------------------------------------------------+

.. note:: ``long`` type is only available i  Python 2.7


.. _in_numeric:

ValidateNumeric
---------------

Check if the new value is a valid ``int``, ``long``, ``float`` or ``complex`` type


Optional parametes:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| throw_exception         | False    | Throw a ``ValueError`` exception on validation fails            |
+-------------------------+----------+-----------------------------------------------------------------+
| allow_null              | True     | Allow ``null`` values                                           |
+-------------------------+----------+-----------------------------------------------------------------+


.. note:: ``long`` type is only available i  Python 2.7



.. _in_string:

ValidateString
--------------

Check if the new value is a valid ``string`` type.

Optional parametes:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| throw_exception         | False    | Throw a ``ValueError`` exception on validation fails            |
+-------------------------+----------+-----------------------------------------------------------------+
| allow_null              | True     | Allow ``null`` values                                           |
+-------------------------+----------+-----------------------------------------------------------------+



.. _in_boolean:

ValidateBoolean
---------------

Check if the new value is a valid ``bool`` type.

Optional parametes:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| throw_exception         | False    | Throw a ``ValueError`` exception on validation fails            |
+-------------------------+----------+-----------------------------------------------------------------+



.. _in_lenght:

ValidateLenght
--------------

Check if the new value is a valid ``string`` type.

Optional parametes:

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| throw_exception         | False    | Throw a ``ValueError`` exception on validation fails            |
+-------------------------+----------+-----------------------------------------------------------------+
| max_lenght              | None     | Maximum value lenght                                            |
+-------------------------+----------+-----------------------------------------------------------------+
| min_lenght              | 0        | Minumum value lenght                                            |
+-------------------------+----------+-----------------------------------------------------------------+



.. _in_email:

ValidateEmail
-------------

Check if the new value is a valid e-mail, using email_validator_ library.

Optional parametes:

+-------------------------+----------+--------------------------------------------------------------------------------+
| Parameter               | Default  | Description                                                                    |
+=========================+==========+================================================================================+
| throw_exception         | False    | Throw a ``ValueError`` exception on validation fails                           |
+-------------------------+----------+--------------------------------------------------------------------------------+
| allow_null              | True     | Allow ``null`` values                                                          |
+-------------------------+----------+--------------------------------------------------------------------------------+
| allow_smtputf8          | True     | Allow internationalized addresses that would require the SMTPUTF8_ extension.  |
+-------------------------+----------+--------------------------------------------------------------------------------+
| check_deliverability    | True     | Check domain name resolution.                                                  |
+-------------------------+----------+--------------------------------------------------------------------------------+
| allow_empty_local       | False    | Allow an empty local part for validating Postfix aliases.                      |
+-------------------------+----------+--------------------------------------------------------------------------------+





Example
-------

+-------------------------+----------+-----------------------------------------------------------------+
| Parameter               | Default  | Description                                                     |
+=========================+==========+=================================================================+
| throw_exception         | False    | Throw a ``ValueError`` exception on validation fails            |
+-------------------------+----------+-----------------------------------------------------------------+
|                         |          |                                                                 |
+-------------------------+----------+-----------------------------------------------------------------+
|                         |          |                                                                 |
+-------------------------+----------+-----------------------------------------------------------------+


.. _email_validator: https://github.com/JoshData/python-email-validator
.. _SMTPUTF8: https://tools.ietf.org/html/rfc6531