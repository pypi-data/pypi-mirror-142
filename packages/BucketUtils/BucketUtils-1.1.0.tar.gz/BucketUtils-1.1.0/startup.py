#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: wangyongpeng
# Mail: 1690992651@qq.com
# Created Time:  2022-03-15
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name="BucketUtils",      #这里是pip项目发布的名称
    version="1.1.0",  #版本号，数值大的会优先被pip
    keywords=("pip", "wangyongpeng","tree"),
    description="用树模型代替qcut进行分桶。",
    long_description="用决策树来分桶",
    license="MIT Licence",

    url="https://github.com/HeiBoWang/DecisionTreeBktUtil.git",     # 项目相关文件地址，一般是github
    author="wangyongpeng",
    author_email="1690992651@qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["numpy"]          # 这个项目需要的第三方库
)


