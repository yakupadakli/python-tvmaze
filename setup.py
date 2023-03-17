#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


setup(
    name="python-tvmaze",
    version="1.0.4",
    description="A Python client for the TvMaze API.",
    license="MIT",
    author="Yakup Adaklı",
    author_email="yakup.adakli@gmail.com",
    url="http://github.com/yakupadakli/python-tvmaze.git",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.8, <4",
    install_requires=[
        "pytest",
        "requests==2.28.2",
        "six==1.16.0"
    ],
    keywords="tvmaze python library",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.11",
    ],
    zip_safe=True,
)
