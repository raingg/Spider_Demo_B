#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 12/26/2018 17:03
# @Author : mingfei.net@gmail.com
# @FileName : detail_text.py
# @GitHub : https://github.com/thu/Spider_Demo_B

import requests as req
import json
import re  # regexp
from spider import *

"""
爬取商品详情的文本信息
存入 csv 文件
存入 MySQL 数据库 product 表
"""


def get_detail_list(product_id):
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
            data = json.loads(line[len('"item":'):-1])  # dict

            # 1. id
            id = data['id']
            print(id)

            # 2. title
            title = data['name']
            print(title)

            # 3. desc
            desc = data.get('simpleDesc')
            print(desc)

            # 4. price
            price = data.get('retailPrice')
            print(price)

            # 5. originalPrice
            original_price = data.get('counterPrice')
            print(original_price)

            # 6. coverPicture
            cover_picter = extract_filename(data.get('primaryPicUrl'))
            print(cover_picter)

            # 7. slidePictures  ["1.jpg", "2.jpg", ...]
            item = data.get('itemDetail')
            slide_pictures = [
                extract_filename(item.get('picUrl1')),
                extract_filename(item.get('picUrl2')),
                extract_filename(item.get('picUrl3')),
                extract_filename(item.get('picUrl4'))
            ]
            slide_pictures = json.dumps(slide_pictures)
            print(slide_pictures)

            # 8. detailPictures
            html = item.get('detailHtml')
            detail_picture_url = re.findall(r'http[a-z0-9:/.]+\.jpg', html)
            detail_pictures = []
            for url in detail_picture_url:
                detail_pictures.append(extract_filename(url))
            detail_pictures = json.dumps(detail_pictures)
            print(detail_pictures)

            # 9. mp4
            vedio = item.get('videoInfo')
            mp4 = extract_filename(vedio.get('mp4VideoUrl'))
            print(mp4)

            # 10. webm
            webm = vedio.get('webmVideoUrl')
            print(webm)

            # 11. categoryId
            category_id = data.get('categoryList')[1].get('id')
            print(category_id)

            return [
                id,
                title,
                desc,
                price,
                original_price,
                cover_picter,
                slide_pictures,
                detail_pictures,
                mp4,
                webm,
                category_id
            ]


print(get_detail_list(3413004))


def get_csv():
    # 拼接所有的 data/csv/product/*.csv 文件
    # 对 product_id 循环电泳
    # 生成商品详情 csv 文件
    pass


# 商品详情 csv 文件  -> MySQL
