import re
import os
from setuptools import setup, find_packages

try:
    import pypandoc
    LONG_DESCRIPTION = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    LONG_DESCRIPTION = ''

setup(
    name='Flask-Validator',
    version='1.4.2',
    license='Mozilla Public License',
    author='Jesus Roldan',
    author_email='jesus.roldan@gmail.com',
    description="Data validator for Flask and SQL-Alchemy, working at Model component with events",
    long_description=LONG_DESCRIPTION,
    url='https://github.com/xeBuz/Flask-Validator',
    packages=find_packages(),
    platforms='any',
    test_suite='nose.collector',
    install_requires=[
        'Flask-SQLAlchemy==2.4.4',
        'email_validator==1.1.2',
        'iso3166==1.0.1',
        'pytz==2020.4',
        'isbnlib==3.10.4',
        'py-moneyed==0.8.0',
        'schwifty==2022.6.1'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
