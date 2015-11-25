import re
import sys
from flask_validator import Validator


class ValidateCreditCard(Validator):

    """ Validate Credit Card Number

    Check if the new value is a valid credit card number.
    Allowed formats:
       - XXXXYYYYWWWWZZZ
       - "XXXXYYYYWWWWZZZ"
       - "XXXX YYYY WWWW ZZZ"
       - "XXXX-YYYY-WWWW-ZZZ"
    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails
    """

    def check_value(self, value):
        if sys.version_info >= (3, 0):
            n = str(value).replace(' ', '').replace('-', '')
        else:
            n = str(value).translate(None, ' -')

        r = [int(ch) for ch in str(n)][::-1]
        return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0


class ValidateCurrency(Validator):

    """ Validate Currency

    Check if the new value is a valid Currency
    List provided by: https://github.com/iktw/python-currency-list/blob/master/python_currency_dict.py

    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails
    """
    currency = {
        'ALL': 'Albania Lek',
        'AFN': 'Afghanistan Afghani',
        'ARS': 'Argentina Peso',
        'AWG': 'Aruba Guilder',
        'AUD': 'Australia Dollar',
        'AZN': 'Azerbaijan New Manat',
        'BSD': 'Bahamas Dollar',
        'BBD': 'Barbados Dollar',
        'BDT': 'Bangladeshi taka',
        'BYR': 'Belarus Ruble',
        'BZD': 'Belize Dollar',
        'BMD': 'Bermuda Dollar',
        'BOB': 'Bolivia Boliviano',
        'BAM': 'Bosnia and Herzegovina Convertible Marka',
        'BWP': 'Botswana Pula',
        'BGN': 'Bulgaria Lev',
        'BRL': 'Brazil Real',
        'BND': 'Brunei Darussalam Dollar',
        'KHR': 'Cambodia Riel',
        'CAD': 'Canada Dollar',
        'KYD': 'Cayman Islands Dollar',
        'CLP': 'Chile Peso',
        'CNY': 'China Yuan Renminbi',
        'COP': 'Colombia Peso',
        'CRC': 'Costa Rica Colon',
        'HRK': 'Croatia Kuna',
        'CUP': 'Cuba Peso',
        'CZK': 'Czech Republic Koruna',
        'DKK': 'Denmark Krone',
        'DOP': 'Dominican Republic Peso',
        'XCD': 'East Caribbean Dollar',
        'EGP': 'Egypt Pound',
        'SVC': 'El Salvador Colon',
        'EEK': 'Estonia Kroon',
        'EUR': 'Euro Member Countries',
        'FKP': 'Falkland Islands (Malvinas) Pound',
        'FJD': 'Fiji Dollar',
        'GHC': 'Ghana Cedis',
        'GIP': 'Gibraltar Pound',
        'GTQ': 'Guatemala Quetzal',
        'GGP': 'Guernsey Pound',
        'GYD': 'Guyana Dollar',
        'HNL': 'Honduras Lempira',
        'HKD': 'Hong Kong Dollar',
        'HUF': 'Hungary Forint',
        'ISK': 'Iceland Krona',
        'INR': 'India Rupee',
        'IDR': 'Indonesia Rupiah',
        'IRR': 'Iran Rial',
        'IMP': 'Isle of Man Pound',
        'ILS': 'Israel Shekel',
        'JMD': 'Jamaica Dollar',
        'JPY': 'Japan Yen',
        'JEP': 'Jersey Pound',
        'KZT': 'Kazakhstan Tenge',
        'KPW': 'Korea (North) Won',
        'KRW': 'Korea (South) Won',
        'KGS': 'Kyrgyzstan Som',
        'LAK': 'Laos Kip',
        'LVL': 'Latvia Lat',
        'LBP': 'Lebanon Pound',
        'LRD': 'Liberia Dollar',
        'LTL': 'Lithuania Litas',
        'MKD': 'Macedonia Denar',
        'MYR': 'Malaysia Ringgit',
        'MUR': 'Mauritius Rupee',
        'MXN': 'Mexico Peso',
        'MNT': 'Mongolia Tughrik',
        'MZN': 'Mozambique Metical',
        'NAD': 'Namibia Dollar',
        'NPR': 'Nepal Rupee',
        'ANG': 'Netherlands Antilles Guilder',
        'NZD': 'New Zealand Dollar',
        'NIO': 'Nicaragua Cordoba',
        'NGN': 'Nigeria Naira',
        'NOK': 'Norway Krone',
        'OMR': 'Oman Rial',
        'PKR': 'Pakistan Rupee',
        'PAB': 'Panama Balboa',
        'PYG': 'Paraguay Guarani',
        'PEN': 'Peru Nuevo Sol',
        'PHP': 'Philippines Peso',
        'PLN': 'Poland Zloty',
        'QAR': 'Qatar Riyal',
        'RON': 'Romania New Leu',
        'RUB': 'Russia Ruble',
        'SHP': 'Saint Helena Pound',
        'SAR': 'Saudi Arabia Riyal',
        'RSD': 'Serbia Dinar',
        'SCR': 'Seychelles Rupee',
        'SGD': 'Singapore Dollar',
        'SBD': 'Solomon Islands Dollar',
        'SOS': 'Somalia Shilling',
        'ZAR': 'South Africa Rand',
        'LKR': 'Sri Lanka Rupee',
        'SEK': 'Sweden Krona',
        'CHF': 'Switzerland Franc',
        'SRD': 'Suriname Dollar',
        'SYP': 'Syria Pound',
        'TWD': 'Taiwan New Dollar',
        'THB': 'Thailand Baht',
        'TTD': 'Trinidad and Tobago Dollar',
        'TRY': 'Turkey Lira',
        'TRL': 'Turkey Lira',
        'TVD': 'Tuvalu Dollar',
        'UAH': 'Ukraine Hryvna',
        'GBP': 'United Kingdom Pound',
        'USD': 'United States Dollar',
        'UYU': 'Uruguay Peso',
        'UZS': 'Uzbekistan Som',
        'VEF': 'Venezuela Bolivar',
        'VND': 'Viet Nam Dong',
        'YER': 'Yemen Rial',
        'ZWD': 'Zimbabwe Dollar'
    }

    def check_value(self, value):
        return bool(self.currency.get(value))


class ValidateIBAN(Validator):

    """ Validate IBAN

    Check if the new value is valid IBAN
    Logic by: http://rosettacode.org/wiki/IBAN#Python

    Args:
        field: SQLAlchemy column to validate
        allow_null: (bool) Allow null values
        throw_exception: (bool) Throw a ValidateError if the validation fails
    """

    _country2length = {'AL': 28, 'AD': 24, 'AT': 20, 'AZ': 28, 'BE': 16, 'BH': 22, 'BA': 20, 'BR': 29, 'BG': 22,
                       'CR': 21, 'HR': 21, 'CY': 28, 'CZ': 24, 'DK': 18, 'DO': 28, 'EE': 20, 'FO': 18, 'FI': 18,
                       'FR': 27, 'GE': 22, 'DE': 22, 'GI': 23, 'GR': 27, 'GL': 18, 'GT': 28, 'HU': 28, 'IS': 26,
                       'IE': 22, 'IL': 23, 'IT': 27, 'KZ': 20, 'KW': 30, 'LV': 21, 'LB': 28, 'LI': 21, 'LT': 20,
                       'LU': 20, 'MK': 19, 'MT': 31, 'MR': 27, 'MU': 30, 'MC': 27, 'MD': 24, 'ME': 22, 'NL': 18,
                       'NO': 15, 'PK': 24, 'PS': 29, 'PL': 28, 'PT': 25, 'RO': 24, 'SM': 27, 'SA': 24, 'RS': 22,
                       'SK': 24, 'SI': 19, 'ES': 24, 'SE': 24, 'CH': 21, 'TN': 24, 'TR': 26, 'AE': 23, 'GB': 22,
                       'VG': 24}

    def check_value(self, value):
        # Ensure upper alphanumeric input.
        iban = value.replace(' ', '').replace('\t', '')
        if not re.match(r'^[\dA-Z]+$', iban):
            return False
        # Validate country code against expected length.
        if len(iban) != self._country2length[iban[:2]]:
            return False
        # Shift and convert.
        iban = iban[4:] + iban[:4]
        digits = int(''.join(str(int(ch, 36)) for ch in iban))  # BASE 36: 0..9,A..Z -> 0..35
        return digits % 97 == 1
