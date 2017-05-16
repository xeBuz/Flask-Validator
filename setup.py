import re
import os
from setuptools import setup, find_packages

try:
    import pypandoc
    LONG_DESCRIPTION = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    LONG_DESCRIPTION = ''

with open('requirements.txt') as f:
    REQUIRED = f.read().splitlines()

setup(
    name='Flask-Validator',
    version='1.2.2',
    license='Mozilla Public License',
    author='Jesus Roldan',
    author_email='jesus.roldan@gmail.com',
    description="Data validator for Flask and SQL-Alchemy, working at Model component with events",
    long_description=LONG_DESCRIPTION,
    url='https://github.com/xeBuz/Flask-Validator',
    packages=find_packages(),
    platforms='any',
    test_suite='nose.collector',
    install_requires=REQUIRED,
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
