import re
import os
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''

setup(
    name='Flask-Validator',
    version='1.2.0',
    license='Mozilla Public License',
    author='Jesus Roldan',
    author_email='jesus.roldan@gmail.com',
    description="Data validator for Flask using SQL-Alchemy, working at Model component with events",
    long_description=long_description,
    url='https://github.com/xeBuz/Flask-Validator',
    packages=find_packages(),
    platforms='any',
    test_suite='nose.collector',
    install_requires=[
        'SQLAlchemy>=1.0',
        'email_validator==1.0',
        'iso3166==0.7',
        'pytz==2015.7',
        'isbnlib==3.5.7',
        'py-moneyed==0.6.0'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
