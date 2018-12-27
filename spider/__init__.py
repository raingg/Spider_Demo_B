#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 12/25/2018 10:41
# @Author : mingfei.net@gmail.com
# @FileName : __init__.py.py
# @GitHub : https://github.com/thu/Spider_Demo_B

import logging
from pathlib import Path


def extract_filename(url):
    return url.split('/')[-1]


def get_logger(filename):

    logger = logging.Logger(filename)

    sh = logging.StreamHandler()
    fh = logging.FileHandler(Path(__file__).parents[1].joinpath('data', 'log', filename), mode='w')

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(threadName)s - %(lineno)s - %(message)s')

    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger
