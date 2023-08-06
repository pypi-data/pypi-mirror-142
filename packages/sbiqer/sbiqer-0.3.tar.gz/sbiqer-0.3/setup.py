#!/usr/bin/python
# encoding: utf-8
from setuptools import setup, find_packages

setup(
    name="sbiqer",
    version="0.3",
    license="MIT Licence",
    keywords=["pip", "spider", "python", "crawler"],
    description="a lightweight spider tool",

    url="https://github.com/srx-2000/sbiqer",
    author="beier",
    author_email="1601684622@qq.com",

    # packages=find_packages(),
    python_requires='>=3.7',
    packages=['sbiqer'],
    include_package_data=True,
    platforms="any",
    install_requires=[]
)
