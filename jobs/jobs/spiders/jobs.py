# coding=utf-8
import scrapy
from scrapy import Request
from scrapy import Selector


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
        newlist = selector.xpath("//table[@class='newlist']")
        # print(newlist)
        for item in newlist:
            if isinstance(item, Selector):
                zwmc = item.xpath(".//td[@class='zwmc']/div/a/text()").extract()
                gsmc = item.xpath(".//td[@class='gsmc']/a/text()").extract()
                zwyx = item.xpath(".//td[@class='zwyx']/text()").extract()
                print('zwmc:', zwmc)
                print("gsmc:", gsmc)
                print("zwyx:", zwyx)
