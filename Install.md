# Awesome

## Mac网络爬虫环境搭建
**下载pip**
- https://pip.readthedocs.io/en/stable/installing/#install-pip
- python get-pip.py
- pip install scrapy
- 失败了，重新安装python

**升级python**
- brew install python
- pip install --upgrade pip
- pip install scrapy

## 工程搭建
- scrapy startproject jobs
- 创建一个jobs.py，实现JobsSpider类
- scrapy crawl JobsSpider

## ubuntu
增加pip代理配置
```
cat ~/.pip/pip.conf
[global]
index-url=http://pypi.douban.com/simple
```
- sudo python3 get-pip.py  --trusted-host pypi.douban.com
- sudo pip3 install scrapy --trusted-host pypi.douban.com
- sudo pip install service-identity --trusted-host pypi.douban.com
- sudo pip install incremental --trusted-host pypi.douban.com
- sudo pip install scrapy --trusted-host pypi.douban.com
- sudo apt-get install crawl




