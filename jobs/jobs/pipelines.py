# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class JobsPipeline(object):
    def __init__(self):
        print ('init')
        self.connection = pymongo.MongoClient('localhost', 27017)
        self.db = self.connection['scrapy']
        self.collection = self.db['jobs']
        self.collection.remove()

    def process_item(self, item, spider):
        if not self.connection or not item:
            return
        self.collection.insert_one(dict(item))

    def __del__(self):
        if self.connection:
            self.connection.close()

    def close_spider(self, spider):
        pass
