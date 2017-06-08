# Python开发学习之路

## [开发环境](./docs/Install.md)
### Mac环境搭建
- brew install python
- pip install --upgrade pip
- pip install scrapy

### Ubuntu环境搭建
增加pip代理配置
```
cat ~/.pip/pip.conf
[global]
index-url=http://pypi.douban.com/simple
```
- sudo python3 get-pip.py  --trusted-host pypi.douban.com
- sudo pip install service-identity --trusted-host pypi.douban.com
- sudo pip install incremental --trusted-host pypi.douban.com
- sudo pip install scrapy --trusted-host pypi.douban.com
- sudo apt-get install crawl

### 创建scrapy工程
- scrapy startproject jobs
- 创建一个jobs.py，实现JobsSpider类
- scrapy crawl JobsSpider

### 安装pymongo
- sudo pip3 install pymongo --trusted-host pypi.douban.com
- sudo apt-get install mongodb-server

## 网络爬虫
### [爬虫数据解析](./docs/Selector.md)
'//' 是绝对路径， './/'是当前路径, '@'是选择attr
```
body = '<html><body><span>good</span></body></html>'
Selector(text=body).xpath('//span/text()').extract()
response = HtmlResponse(url='http://example.com', body=body)
response.xpath('//base/@href').extract()
response.css('base::attr(href)').extract()
response.xpath('//a[contains(@href, "image")]/@href').extract()
response.css('a[href*=image]::attr(href)').extract()
response.xpath('//a[contains(@href, "image")]/img/@src').extract()
response.css('a[href*=image] img::attr(src)').extract()
```