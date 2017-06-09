# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeautyItem(scrapy.Item):
    # define the fields for your item here like:
    img = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    count = scrapy.Field()
    date = scrapy.Field()
    pass


class BeautyDetailItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    img = scrapy.Field()
    pass
