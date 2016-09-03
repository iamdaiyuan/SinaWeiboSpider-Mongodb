#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: fansan
# @Date:   2016-03-11 17:09:06
# @Last Modified by:   fansan
# @Last Modified time: 2016-06-15 20:05:18

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboGIFItem(scrapy.Item):
    # define the fields for your item here like:
    ContentId = scrapy.Field()
    ContentUrl = scrapy.Field()
    Content = scrapy.Field()
    GIFUrl = scrapy.Field()
    RepostNum = scrapy.Field()
    CommentNum = scrapy.Field()
    LikeNum = scrapy.Field()
    Comment = scrapy.Field()
    PostTime = scrapy.Field()

class KeywordItem(scrapy.Item):
    # define the fields for your item here like:
    Keyword = scrapy.Field()
    ContentId = scrapy.Field()
    ContentUrl = scrapy.Field()
    Content = scrapy.Field()
    GIFUrl = scrapy.Field()
    RepostNum = scrapy.Field()
    CommentNum = scrapy.Field()
    LikeNum = scrapy.Field()
    Comment = scrapy.Field()
    PostTime = scrapy.Field()


