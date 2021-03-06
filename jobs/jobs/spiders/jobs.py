# coding=utf-8
import scrapy
from scrapy import Request
from scrapy import Selector

from ..items import JobsItem


class JobsSpider(scrapy.Spider):
    name = "JobsSpider"
    host = "http://sou.zhaopin.com/"
    start_urls = [
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=android&sm=0&isfilter=1&p=1&sf=15001&st=20000"]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        selector = Selector(response)
        new_list = selector.xpath("//table[@class='newlist']")
        for job in new_list:
            item = JobsItem()
            keywords = str(job.xpath(".//td[@class='zwmc']/div/a/b/text()").extract_first())
            item['name'] = keywords + str(job.xpath(".//td[@class='zwmc']/div/a/text()").extract_first())
            item['link'] = job.xpath(".//td[@class='zwmc']/div/a/@href").extract_first()
            item['company'] = job.xpath(".//td[@class='gsmc']/a/text()").extract_first()
            item['salary'] = job.xpath(".//td[@class='zwyx']/text()").extract_first()
            item['site'] = job.xpath(".//td[@class='gzdd']/text()").extract_first()
            item['time'] = job.xpath(".//td[@class='gxsj']/span/text()").extract_first()
            print(item)
            yield item
