#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
from version import __VERSION__
setup(
    name='guesstime',
    version=__VERSION__,
    description=(
        'guesstime'
    ),
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='readerror',
    author_email='readerror@sina.com',
    maintainer='readerror',
    maintainer_email='readerror@sina.com',
    license='GPL License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/DJMIN/dao',
    python_requires='>=3.5',
    install_requires=[
        "wrapt",
        "wheel",
        "twine",
        "pyunit-time",
        "time-decode",
        "python-dateutil",
        "arrow",
    ],
)