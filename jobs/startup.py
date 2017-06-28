# coding=utf-8

# from scrapy.cmdline import execute
# execute(['scrapy', 'crawl', 'JobsSpider'])

import pymongo

from primer.emails import SendEmail
from primer.module import MongoDb
from thirdparty import makeHTML


class SendJob(object):
    def send(self):
        client = pymongo.MongoClient('localhost', 27017)
        db = client.scrapy
        collection = db.jobs

        rows = collection.find()
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

        send_email = SendEmail()
        send_email.send_html('每日工作推荐', job_html)

# Just for test
send_job = SendJob()
send_job.send()