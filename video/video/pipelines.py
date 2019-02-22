# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class VideoPipeline(object):
    def __init__(self):
        print('init')

    def process_item(self, item, spider):
        print("item:" + item)
        return item

    def close_spider(self, spider):
        print('close_spider')
        pass
