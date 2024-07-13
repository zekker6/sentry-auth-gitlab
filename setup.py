#!/usr/bin/env python
"""
sentry-auth-gitlab-v2
==================

:copyright: (c) 2015 Functional Software, Inc
"""
from __future__ import absolute_import
from setuptools import setup, find_packages
import os

tests_require = [
    'pytest',
    'mock',
]

install_requires = [
    'sentry',
]

# The directory containing this file

HERE = os.path.dirname(os.path.realpath(__file__))

# The text of the README file
with open(HERE + "/README.md", 'r') as f:
    README = f.read()

setup(
    name='sentry-auth-gitlab-v2',
    version='0.4.2',
    author='Zakhar Bessarab',
    author_email='zekker6@gmail.com',
    url='https://github.com/zekker6/sentry-auth-gitlab',
    description='Gitlab authentication provider for Sentry',
    long_description=README,
    long_description_content_type="text/markdown",
    license='',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'tests': tests_require},
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'auth_gitlab = auth_gitlab.apps.Config',
         ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
