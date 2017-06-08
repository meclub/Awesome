# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from __future__ import print_function

import os
import requests


def download_img(url, dir_path, img_name):
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


def mk_dir(dir_name):
    new_path = os.path.join('.', dir_name)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path


class BeautyPipeline(object):
    def process_item(self, item, spider):
        url = item['img']
        title = item['title']
        dir_path = mk_dir('img')
        download_img(url, dir_path, title)
        return item
