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
    version='1.2.3',
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
        'Flask-SQLAlchemy>=1.0',
        'email_validator==1.0.2',
        'iso3166==0.8',
        'pytz==2017.2',
        'isbnlib==3.6.8',
        'py-moneyed==0.7.0'
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
