# coding=utf-8
import scrapy


class JobsSpider(scrapy.Spider):
    name = "JobsSpider"
    host = "http://sou.zhaopin.com/"
    start_urls = [
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=android&sm=0&isfilter=1&p=1&sf=15001&st=20000"]

    def parse(self, response):
        print(response.body)
