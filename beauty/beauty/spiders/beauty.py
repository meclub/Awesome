# coding=utf-8
import scrapy
from ..items import BeautyItem
from ..items import BeautyDetailItem
from scrapy import Request, Selector


class BeautySpider(scrapy.Spider):
    name = "BeautySpider"
    host = "http://pic.yesky.com/"
    start_urls = [
        "http://pic.yesky.com/c/6_20491.shtml"]

    def start_detail(self, url):
        yield Request(url=url, callback=self.parse_detail)

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
            yield Request(item['link'], callback=self.parse_detail)
            yield item

    def parse_detail(self, response):
        selector = Selector(response)
        item = BeautyDetailItem()
        item['title'] = selector.xpath("//div[@class='ll_img']/h2/a/text()").extract_first()
        item['link'] = selector.xpath("//div[@class='ll_img']/h2/a/text()").extract_first()
        item['img'] = selector.xpath("//div[@class='l_effect_img_mid']/a/img/@src").extract_first()
        next_detail = selector.xpath("//div[@class='l_effect_img_mid']/a/@href").extract_first()
        print (item)
        if next_detail:
            yield Request(next_detail, callback=self.parse_detail)
        yield item
