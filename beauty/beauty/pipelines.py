# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from __future__ import print_function

import os
import random
import requests

from .items import BeautyItem
from .items import BeautyDetailItem


def download_img(url, dir_path, img_name):
    print ('down_load:')
    req_timeout = 20
    try:
        res = requests.get(url, timeout=req_timeout)
        if str(res.status_code)[0] == "4":
            print("error ", str(res.status_code), ":", url)
            return False
    except Exception as e:
        print(e)
        return False

    file_name = os.path.join(dir_path, img_name + ".jpg")
    with open(file_name, 'wb') as f:
        f.write(res.content)

    return True


def mk_dir(root_dir, dir_name):
    new_path = os.path.join(root_dir, dir_name)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path


def process_beauty(item):
    url = item['img']
    title = item['title']
    img_path = mk_dir('.', 'img')
    download_img(url, img_path, title)
    return item


def process_beauty_detail(item):
    img = item['img']
    title = item['title']
    img_path = mk_dir('.', 'img')
    item_path = mk_dir(img_path, title)
    download_img(img, item_path, str(random.randint(0, 10000000)))
    return item


class BeautyPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, BeautyItem):
            pass
            # return process_beauty(item)
        if isinstance(item, BeautyDetailItem):
            return process_beauty_detail(item)
