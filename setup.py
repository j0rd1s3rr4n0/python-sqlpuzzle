#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# https://packaging.python.org/en/latest/single_source_version.html
execfile('sqlpuzzle/version.py')

setup(
    name='sqlpuzzle',
    version=VERSION,
    packages=[
        'sqlpuzzle',
        'sqlpuzzle/_backends',
        'sqlpuzzle/_common',
        'sqlpuzzle/_queries',
        'sqlpuzzle/_queryparts',
    ],

    install_requires=[line.strip() for line in open('requirements.txt').readlines()],

    url='https://github.com/horejsek/python-sqlpuzzle',
    author='Michal Horejsek',
    author_email='horejsekmichal@gmail.com',
    description='Python library for writing SQL queries.',
    license='PSF',

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
    ],
)
