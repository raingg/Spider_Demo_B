#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 12/25/2018 17:18
# @Author : mingfei.net@gmail.com
# @FileName : product.py
# @GitHub : https://github.com/thu/Spider_Demo_B

import requests as req
import json
import pandas as pd
from pathlib import Path

# todo 获取所有一级类目 id

url = 'http://you.163.com/xhr/globalinfo//queryTop.json'

cateList = req.get(url).json()['data']['cateList']

sup_ids = []

for cate in cateList:
    sup_ids.append(cate['id'])

counter = 0

def get_csv(sup_id):
    url = 'http://you.163.com/item/list?categoryId=' + str(sup_id)
    product_list = []
    for line in req.get(url).iter_lines():
        line = line.decode('utf-8')
        if line.startswith('var json_Data='):
            data = json.loads(line[len('var json_Data='):-1])
            categoryItemList = data['categoryItemList']

            for sub in categoryItemList:
                sub_id = sub['category']['id']
                for product in sub['itemList']:
                    product_id = product['id']
                    product_list.append([sup_id, sup_id, product_id])
                    global counter
                    counter = counter + 1

    columns = ['sup_id', 'sub_id', 'product_id']
    product_df = pd.DataFrame(product_list, columns=columns)
    product_df.to_csv(Path(__file__).parents[1].joinpath('data', 'csv', 'product', str(sup_id) + '.csv'), index=False)
    print('%s.csv saved.' % sup_id)


for sup_id in sup_ids:
    get_csv(sup_id)

print(counter)

'''
csv

sup_id, sub_id, product_id
1005000,1008009,3413004
...
5k
'''
