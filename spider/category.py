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

cateList = r.json()['data']['cateList']

categories = []
for cate in cateList:
    categories.append([cate['id'], cate['name']])
    for group in cate['subCateGroupList']:
        for sub in group['categoryList']:
            categories.append([
                sub['id'],
                sub['name'],
                group['name'],  # ***
                sub['frontName'],
                sub['bannerUrl'],
                sub['superCategoryId'],
            ])


print(categories)


'''
# csv:
id, title, group, desc, icon, categoryId
1005000,居家,,,,
1008009,床品件套,床品,MUJI等品牌制造商出品,785a1507ce654746875063805c6c4235.png,1005000
'''