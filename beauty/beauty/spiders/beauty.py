# coding=utf-8
import scrapy
from ..items import BeautyItem
from scrapy import Request, Selector


class BeautySpider(scrapy.Spider):
    name = "BeautySpider"
    host = "http://pic.yesky.com/"
    start_urls = [
        "http://pic.yesky.com/c/6_20491.shtml"]

    def parse(self, response):
        selector = Selector(response)
        beauty_list = selector.xpath("//div[@class='lb_box']/dl")
        for beauty in beauty_list:
            item = BeautyItem()
            item['img'] = beauty.xpath(".//dt/a/img/@src").extract_first()
            item['link'] = beauty.xpath(".//dd/a/@href").extract_first()
            item['title'] = beauty.xpath(".//dd/a/text()").extract_first()
            item['count'] = beauty.xpath(".//dd/span/text()").extract_first().strip().replace('(', '').replace(')', '')
            item['date'] = beauty.xpath(".//div[@class='nmark']/span[@class='date']/text()").extract_first()
            yield item


