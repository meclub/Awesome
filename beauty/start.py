# from scrapy.cmdline import execute
# execute(['scrapy', 'crawl', 'BeautySpider'])
from .share import ShareBeauty

share_beauty = ShareBeauty();
share_beauty.share()