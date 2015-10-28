import re
from setuptools import setup


# def run_tests():
#     from tests import suite
#     return suite()


setup(
    name='Flask-Validator',
    version='0.1',
    license='Mozilla Public License',
    author='Jesus Roldan',
    author_email='jesus.roldan@gmail.com',

    url='https://github.com/xeBuz/Flask-Validator',

    packages=['flask_validator'],

    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
        'SQLAlchemy>=1.0',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
