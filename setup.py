#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django_de',
      version='0.1',
      packages=find_packages(),
      package_data={'django_de': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'django_de': ['bin/*.pyc']},
      scripts=['django_de/bin/manage.py'])
