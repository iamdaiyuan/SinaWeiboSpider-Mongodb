#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: fansan
# @Date:   2016-03-11 17:09:06
# @Last Modified by:   fansan
# @Last Modified time: 2016-06-16 10:32:59

# Scrapy settings for WeiboGIF project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WeiboGIF'

SPIDER_MODULES = ['WeiboGIF.spiders']
NEWSPIDER_MODULE = 'WeiboGIF.spiders'
# DOWNLOAD_HANDLERS = {'s3': None}

DOWNLOADER_MIDDLEWARES = {
    'WeiboGIF.middlewares.CustomUserAgentMiddleware': 401,
    'WeiboGIF.middlewares.CustomCookieMiddleware': 402,
}


ITEM_PIPELINES = {
    'WeiboGIF.pipelines.MongoDBPipleline': 300,
    #'template.pipelines.RedisPipeline': 301,
}

DOWNLOAD_DELAY = 2
# LOG_LEVEL = 'INFO'






