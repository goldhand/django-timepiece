# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import django-timepiece
version = django-timepiece.__version__

setup(
    name='django-timepiece',
    version=version,
    author='',
    author_email='will@django.nu',
    packages=[
        'django-timepiece',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['django-timepiece/manage.py'],
)