#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zack
# datetime:2022/3/10 0010 13:15
import os
import sys
from setuptools import setup, find_packages

path = os.path.join(os.path.dirname(__file__), "sentrylog/README.md") 
with open(path, "r", encoding='utf-8') as f:
    desc = f.read()

setup(

    name="sentrylog",
    author="Zack",  # 作者
    version="0.0.3",
    description="sentry-logging",
    long_description=desc,
    author_email="1125564921@qq.com",
    long_description_content_type="text/markdown",
    url="https://gitee.com/zhangyaoo/sentrylogging",  # gitee
    packages=find_packages(),
    package_data={'': ['*.yaml', '*.md', '*.txt']},
    classifiers=[  # 包标签，便于搜索
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Logging",
    ],
)
