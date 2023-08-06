#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
# from setuptools import find_package_data
import sys

setup(
    name="FMLocker",
    version="1.0.1.0",
    author="inflower",
    author_email="inflowers@126.com",
    description="A MySQL Distributed-Locker",
    long_description=open("README.rst").read(),
    license="GPL",
    url="https://pypi.python.org/pypi/FMLocker",
    packages=find_packages(exclude=["*.*"]),
    include_package_data=True,
    py_modules=['FMLocker', ],
    # package_dir = {'': ''},
    # package_data = {'': ['*.txt'], 'mypkg': ['data/*.dat'],},
    # data_files=[('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
    #                   ('config', ['cfg/data.cfg']),
    #                   ('/etc/init.d', ['init-script'])],
    install_requires=[
        "mysqlclient==2.0.1",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
