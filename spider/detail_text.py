#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 12/26/2018 17:03
# @Author : mingfei.net@gmail.com
# @FileName : detail_text.py
# @GitHub : https://github.com/thu/Spider_Demo_B

import requests as req
import json

"""
爬取商品详情的文本信息
存入 csv 文件
存入 MySQL 数据库 product 表
"""


def get_csv(product_id):
    """
    id, title, ...


    detail.csv:
    id, title, ....
    1, '',..

    4k

    :param product_id:
    :return:
    """

    url = 'http://you.163.com/item/detail?id=' + str(product_id)

    for line in req.get(url).iter_lines():
        line = line.decode('utf-8')
        if line.startswith('"item":'):
            data = json.loads(line[len('"item":'):-1])


            # 1. id
            id = data['id']
            print(id)

            # 2. title
            title = data['name']
            print(title)

            # ...

            # slidePictures

            # detailPictures

            # mp4

            # webm


get_csv(3413004)

# todo 拼接所有的 product/csv 文件
# 对 product_id 循环电泳 get_csv


# detail.csv -> MySQL
