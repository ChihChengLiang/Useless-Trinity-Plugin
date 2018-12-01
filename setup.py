#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='useless-plugin',
    py_modules=['useless_plugin'],
    entry_points={
        'trinity.plugins': 'useless_plugin=useless_plugin:UselessPlugin',
    },
)