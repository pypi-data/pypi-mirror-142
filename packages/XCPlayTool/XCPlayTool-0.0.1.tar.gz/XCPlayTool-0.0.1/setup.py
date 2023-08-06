#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: xuxuechao
# Mail: 932829703@qq.com
# Created Time:  2022-03-14 29:25: AM
#############################################


from setuptools import setup, find_packages

setup(
    name = "XCPlayTool",
    version = "0.0.1",
    keywords = ["xxc","play"],
    description = "测试上传pip",
    long_description = "测试上传pip...",
    license = "MIT Licence",
    url = "https://github.com/19933139420/pythonTest",
    author = "xuxuechao",
    author_email = "932829703@qq.com",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['chardet','sympy']
)