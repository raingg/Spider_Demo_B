#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 12/25/2018 10:42
# @Author : mingfei.net@gmail.com
# @FileName : category.py
# @GitHub : https://github.com/thu/Spider_Demo_B

"""
爬取 一级/二级 类目信息
"""

import requests as req


link = 'http://you.163.com/xhr/globalinfo//queryTop.json'

r = req.get(link)

print(r.json()['data']['cateList'][0]['name'])