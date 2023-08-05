#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from pappdb import VERSION_STRING

setup(
    include_package_data=True,
    name='pappdb',
    version=VERSION_STRING,
    author='Florian Scherf',
    url='https://github.com/fscherf/pappdb',
    author_email='mail@florianscherf.de',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    scripts=[],
)
