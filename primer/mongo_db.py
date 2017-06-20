# coding=utf-8
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
import pymongo

from module import MongoDb
from thirdparty import makeHTML

print('pymongo test')
client = pymongo.MongoClient('localhost', 27017)
db = client.scrapy
connection = db.jobs

# insert
# connection.insert({'company': '北京远特科技股份有限公司',
#                    'link': 'http://jobs.zhaopin.com/383991117251394.htm',
#                    'name': 'Android驱动工程师',
#                    'salary': '15001-20000',
#                    'site': '深圳-南山区',
#                    'time': '15天前'}
#                   )

# query
# item_one = connection.find_one()
# print('item_one', item_one)

count = connection.find().count()
item_all = connection.find()
print('count', count)
for item in item_all:
    print('item', item)

# remove
# connection.remove()

# make html table
rows = connection.find()
print('rows:', rows)
mongo_db = MongoDb()
job_array = mongo_db.transform(rows, '_id')
print('job_array:', job_array)

pageHead = makeHTML.head('每日工作推荐')
pageBody = makeHTML.body('智联招聘')
job_table = makeHTML.table(job_array).make()

pageBody.addPiece(job_table)
page = makeHTML.page([pageHead, pageBody])
job_html = page.make()
print('job_html:', job_html)
