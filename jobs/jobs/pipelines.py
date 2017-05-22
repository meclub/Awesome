# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class JobsPipeline(object):
    def __init__(self):
        self.connection = pymongo.MongoClient('localhost', 27017)
        self.db = self.connection.scrapy
        self.connection = self.db.jobs

    def process_item(self, item, spider):
        if not self.connection or not item:
            return
        self.connection.save(item)

    def __del__(self):
        if self.connection:
            self.connection.close()
