#!/usr/bin/env python
# coding: utf-8

from setuptools import setup


setup(
    name='pigeonking',
    version='0.0.2',
    author='pigeonking',
    author_email='yuezih@std.uestc.edu.cn',
    url='https://github.com/yuezih/King-of-Pigeon',
    description='King of Pigeon',
    packages=['pigeonking'],
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'pigeonking = pigeonking:pigeonking'
        ]
    }
)