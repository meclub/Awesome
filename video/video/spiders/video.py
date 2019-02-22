# coding=utf-8
import scrapy
from scrapy import Request
from scrapy import Selector

from ..items import VideoItem

class VideoSpider(scrapy.Spider):
    name = "VideoSpider"
    host = "https://www.360kan.com/"
    start_urls = [
        "https://www.360kan.com"]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        selector = Selector(response)
        slide_list = selector.xpath("//div[@class='b-topslider-item js-g-slide-item g-slide-item']")
        print("parse_page ------------------")
        print(slide_list)
        # 首页的视频容器
        for slide in slide_list:
            # 遍历视频容器的视频列表
            video_list = slide.xpath(".//a")
            for video in video_list:
                # 遍历视频列表
                link = video.xpath(".//@href").extract_first()
                yield Request(link, callback=self.parse_detail)

    def parse_detail(self, response):
        selector = Selector(response)
        video_source = selector.xpath("//p[@class='js-current s-playsite-current']/span/text()").extract_first()
        if video_source is None:
            video_source = selector.xpath("//div[@class='site g-clear']/div/a/span/text()").extract_first()
        if video_source is None:
            video_source = selector.xpath("//div[@class='now-site js-now-site']/span/text()").extract_first()
        if video_source is None:
            video_source = selector.xpath("//div[@class='top-list-zd g-clear']/a/text()").extract_first()
        print("video_source:" + video_source)

        # save item
        item = VideoItem()
        item['name'] = video_source
        print(item)
        yield item