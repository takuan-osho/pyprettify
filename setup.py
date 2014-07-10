# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='pyprettify',
    version='0.1.0',
    py_modules=['pyprettify'],
    install_requires=[
        'Click',
        'beautifulsoup4',
    ],
    entry_points='''
        [console_scripts]
        pyprettify=pyprettify:cli
    ''',
)
