#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
# python setup.py sdist 打包成tar.gz的形式
# python setup.py bdist_wheel  打包成wheel格式

setup(
    py_modules=["expasy"],
    packages=find_packages(),
    name="biomagicbox",
    version="0.1.0",
    description="Tools for bioinformatics",
    long_description="***",
    author="Fujun Sun",
    author_email="sfjdx1144@live.com",
    install_requires=['requests'],
    zip_safe=False,
    license="MIT Licence",
    python_requires=">=3.4.0",
    include_package_data=True
)
