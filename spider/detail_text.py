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
from pathlib import Path
import os
import pandas as pd
import csv
import time

"""
爬取商品详情的文本信息
存入 csv 文件
存入 MySQL 数据库 product 表
"""

logger = get_logger('detail_text.txt')
logger.setLevel(logging.WARNING)

counter = 0


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
            logger.debug(id)

            # 2. title
            title = data['name']
            logger.debug(title)

            # 3. desc
            desc = re.sub(r'["\n]', '', data.get('simpleDesc'))
            logger.debug(desc)

            # 4. price
            price = data.get('retailPrice')
            logger.debug(price)

            # 5. originalPrice
            original_price = data.get('counterPrice')
            logger.debug(original_price)

            # 6. coverPicture
            cover_picter = extract_filename(data.get('primaryPicUrl'))
            logger.debug(cover_picter)

            # 7. slidePictures  ["1.jpg", "2.jpg", ...]
            item = data.get('itemDetail')
            slide_pictures = [
                extract_filename(item.get('picUrl1')),
                extract_filename(item.get('picUrl2')),
                extract_filename(item.get('picUrl3')),
                extract_filename(item.get('picUrl4'))
            ]
            slide_pictures = json.dumps(slide_pictures)
            logger.debug(slide_pictures)

            # 8. detailPictures
            html = item.get('detailHtml')
            detail_picture_url = re.findall(r'http[a-z0-9:/.]+\.jpg', html)
            detail_pictures = []
            for url in detail_picture_url:
                detail_pictures.append(extract_filename(url))
            detail_pictures = json.dumps(detail_pictures)
            logger.debug(detail_pictures)

            # 9. mp4
            mp4 = ''
            video = item.get('videoInfo')
            if video:
                mp4 = extract_filename(video.get('mp4VideoUrl'))
            logger.debug(mp4)

            # 10. webm
            webm = ''
            if video:
                webm = video.get('webmVideoUrl')
            logger.debug(webm)

            # 11. categoryId
            category_id = data.get('categoryList')[1].get('id')

            global counter

            counter = counter + 1

            logger.warning('%d - %s' % (counter, product_id))

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


def get_csv():
    """
    拼接所有的 data/csv/product/*.csv 文件
    生成商品详情 csv 文件
    """
    path = Path(__file__).parents[1].joinpath('data', 'csv', 'product')
    csv_list = [f for f in os.listdir(path)]
    total_df = pd.DataFrame()
    for curr_csv in csv_list:
        df = pd.read_csv(Path.joinpath(path, curr_csv))
        if total_df.empty:
            total_df = df
        else:
            total_df = total_df.append(df)
    total_df.to_csv(Path(__file__).parents[1].joinpath('data', 'csv', 'total.csv'), index=False)

    detail_list = []
    for line in open(Path(__file__).parents[1].joinpath('data', 'csv', 'total.csv')).readlines()[1:]:
        product_id = line.split(',')[-1]
        logger.debug(product_id)

        detail_list.append(get_detail_list(product_id))

    columns = [
        'id',
        'title',
        'desc',
        'price',
        'original_price',
        'cover_picter',
        'slide_pictures',
        'detail_pictures',
        'mp4',
        'webm',
        'category_id'
    ]

    detail_df = pd.DataFrame(detail_list, columns=columns)

    detail_df.to_csv(
        Path(__file__).parents[1].joinpath('data', 'csv', 'detail.csv'),
        index=False,
        encoding='utf-8',
        sep='|',
        quoting=csv.QUOTE_NONE,
        quotechar="",
        escapechar='\\'
    )


# 商品详情 csv 文件  -> MySQL
# load data local infile


if __name__ == '__main__':
    start_time = time.time()
    get_csv()
    logger.warnning('total time: %s.' % (time.time() - start_time))
