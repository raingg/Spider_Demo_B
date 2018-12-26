#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 12/25/2018 17:18
# @Author : mingfei.net@gmail.com
# @FileName : product.py
# @GitHub : https://github.com/thu/Spider_Demo_B

import requests as req
import json


# todo 获取所有一级类目 id

sup_ids = []


def get_csv(sup_id):
    url = 'http://you.163.com/item/list?categoryId=' + str(sup_id)
    for line in req.get(url).iter_lines():
        line = line.decode('utf-8')
        if line.startswith('var json_Data='):
            data = json.loads(line[len('var json_Data='):-1])
            print(type(data))
            categoryItemList = data['categoryItemList']
            print(categoryItemList)

            # sub_id
            # product_id


get_csv(1005000)
# for sup_id in sup_ids:
#     get_csv(sup_id)




'''
csv

sup_id, sub_id, product_id
1005000,1008009,3413004
...
5k
'''