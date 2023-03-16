#!/usr/bin/env python
# coding=utf-8

import uuid
from setuptools import setup, find_packages


setup(
    name="python-tvmaze",
    version="1.0.3a1",
    description="A Python client for the TvMaze API.",
    license="MIT",
    author="Yakup Adaklı",
    author_email="yakup.adakli@gmail.com",
    url="http://github.com/yakupadakli/python-tvmaze.git",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "pytest==7.2.2",
        "requests==2.28.2",
        "six==1.16.0"
    ],
    keywords="tvmaze library",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.11",
    ],
    zip_safe=True,
)
