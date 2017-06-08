# Python开发环境

## Mac环境
**下载pip**
- https://pip.readthedocs.io/en/stable/installing/#install-pip
- python get-pip.py
- pip install scrapy
- 失败了，重新安装python

**升级python**
- brew install python
- pip install --upgrade pip
- pip install scrapy

## Scrapy环境
- scrapy startproject jobs
- 创建一个jobs.py，实现JobsSpider类
- scrapy crawl JobsSpider

结果输出为文件：scrapy crawl JobsSpider -o items.json -t json

## Ubuntu环境
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

## pymongo
- sudo pip3 install pymongo --trusted-host pypi.douban.com
- sudo apt-get install mongodb-server

Linux数据库位置
```/var/lib/mongodb```

数据库查看工具
```
https://robomongo.org/
```




