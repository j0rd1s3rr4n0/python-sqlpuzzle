#!/usr/bin/env python
#
# sqlpuzzle
# Michal Horejsek <horejsekmichal@gmail.com>
# https://github.com/horejsek/sqlpuzzle
#
# This application is released under the GNU General Public License
# v3 (or, at your option, any later version). You can find the full
# text of the license under http://www.gnu.org/licenses/gpl.txt.
# By using, editing and/or distributing this software you agree to
# the terms and conditions of this license.
# Thank you for using free software!
#

from distutils.core import setup

version = '0.14.2'

setup(
    name = 'sqlpuzzle',
    packages = [
        'sqlpuzzle',
        'sqlpuzzle/_features',
        'sqlpuzzle/_queries',
        'sqlpuzzle/_libs',
    ],
    version = version,
    url = 'https://github.com/horejsek/sqlpuzzle',
    description = 'Python module.',
    author = 'Michal Horejsek',
    author_email = 'horejsekmichal@gmail.com',
    license = 'GNU General Public License (GPL)',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
    ],
)

