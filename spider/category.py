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
import pandas as pd
from pathlib import Path
import mysql.connector

url = 'http://you.163.com/xhr/globalinfo//queryTop.json'

r = req.get(url)

cateList = r.json()['data']['cateList']

categories = []
urls = []
for cate in cateList:
    categories.append([cate['id'], cate['name']])
    for group in cate['subCateGroupList']:
        for sub in group['categoryList']:
            urls.append(sub['bannerUrl'])
            categories.append([
                sub['id'],
                sub['name'],
                group['name'],  # ***
                sub['frontName'],
                sub['bannerUrl'].split('/')[-1],
                str(sub['superCategoryId']),
            ])

columns = ['id', 'title', 'group', 'desc', 'icon', 'categoryId']

cate_pd = pd.DataFrame(categories, columns=columns)
cate_pd.to_csv(Path(__file__).parents[1].joinpath('data', 'csv', 'category.csv'), encoding='UTF-8', index=False)

'''
# csv:
id, title, group, desc, icon, categoryId
1005000,居家,,,,
1008009,床品件套,床品,MUJI等品牌制造商出品,785a1507ce654746875063805c6c4235.png,1005000
'''

connection = mysql.connector.connect(
    user='root',
    password='system'
)

cursor = connection.cursor()

cursor.execute('set foreign_key_checks = 0')  # 临时解除外键约束
cursor.execute('truncate table db_b.category')
cursor.execute('set foreign_key_checks = 1')  # 再次启用外键约束

sql = """
load data local infile 'D:/PycharmProjects/Spider_Demo_B/data/csv/category.csv'
into table db_b.category
fields terminated by ','
ignore 1 lines
(id, title, @v_group, @v_desc, @v_icon, @v_categoryId)
set
`group` = nullif(@v_group, ''),
`desc` = nullif(@v_desc, ''),
icon = nullif(@v_icon, ''),
categoryId = nullif(@v_categoryId, '')
"""

cursor.execute(sql)

connection.commit()


def download(url):
    filename = url.split('/')[-1]
    with open(Path(__file__).parents[1].joinpath('data', 'icons', filename), 'wb') as f:
        f.write(req.get(url).content)
        print('%s download.' % url)


for url in urls:
    download(url)
