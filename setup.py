#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: mushaoyu
# Mail: 407703712@qq.com
# Created Time:  2022/10/03 01:25:34 PM
#############################################


from setuptools import setup, find_packages

setup(
    name = "manjutools",
    version = "0.0.6",
    keywords = ("agent","unitl", "format", "path"),
    description = "collect some commons methods",
    long_description = "collect some commons methods",
    license = "MIT Licence",

    url = "https://github.com/haimalairen/py-tools",
    author = "mushaoyu",
    author_email = "407703712@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['fake_useragent']
)