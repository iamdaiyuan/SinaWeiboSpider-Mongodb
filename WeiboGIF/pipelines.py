#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: fansan
# @Date:   2016-03-11 17:09:06
# @Last Modified by:   fansan
# @Last Modified time: 2016-06-18 14:07:49
import logging

import pymongo
from items import WeiboGIFItem, KeywordItem


class MongoDBPipleline(object):
    def __init__(self):
        self.clinet = pymongo.MongoClient("localhost", 27017)
        db = self.clinet["SinaWeibo"]
        self.WeiboGIF = db["WeiboGIF"]
        self.Keyword = db['WeiboKeyword']

    def process_item(self, item, spider):
        """ 判断数据库中该Content是否已经存在 """
        if isinstance(item, WeiboGIFItem):
            Content_Id = self.WeiboGIF.find({'ContentId': item['ContentId']})
            if Content_Id.count() == 0:
                try:
                    self.WeiboGIF.insert_one(dict(item))
                    logging.info("Save Content File: %s !!!", item['ContentId'])
                    print "save post!!!"
                except Exception:
                    pass
        elif isinstance(item, KeywordItem):
            Content_Id = self.Keyword.find({'ContentId': item['ContentId']})
            if Content_Id.count() == 0:
                try:
                    self.Keyword.insert_one(dict(item))
                    logging.info("Save Content File: %s !!!", item['ContentId'])
                    print "save post!!!"
                except Exception:
                    pass
        # return item

    def close_spider(self, spider):
        self.clinet.close()
