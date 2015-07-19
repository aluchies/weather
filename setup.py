#!/usr/bin/env python

from setuptools import setup, find_packages
import weather


setup(
    name='weather',
    version=weather.__version__,
    description='print weather details via the command line',
    long_description='',
    keywords='weather command line',
    author='Adam Luchies',
    url='https://github.com/aluchies/weather',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'weather = weather.weather:main',
        ]
    },
    install_requires=[
        'requests',
    ],
)