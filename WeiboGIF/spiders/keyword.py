#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: fansan
# @Date:   2016-06-13 15:08:13
# @Last Modified by:   fansan
# @Last Modified time: 2016-06-16 23:46:45

# Load Modules #
import time
import re
import logging

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector
from datetime import datetime
from scrapy.http import FormRequest, Request

from WeiboGIF.agents import AGENTS
from WeiboGIF.items import KeywordItem
from WeiboGIF.startkeyword import StartKeyword

# Define Spider Class #
class WeiboGIFSpider(CrawlSpider):
    """docstring for WeiboGIFSpider"""
    name = "keyword"

    allow_domains = [
        "weibo.cn"
    ]

    host = "http://weibo.cn"

    # 设定爬虫起始页 #
    start_urls = StartKeyword

    # 定义解析函数 #
    def parse(self, response):
        """加载搜索页面并提取目标URL"""
        sel = Selector(response)
        # 提取出页面中包含GIF图片的微博模块 #
        TargetUrls = sel.xpath("//img[@class='ib' and contains(@src, '.gif')]/../../..")
        # 提取关键词 #
        keyword = sel.xpath("//input[@type='text' and @name='keyword']/@value").extract()
        # 遍历这些微博，并提取信息 #
        for targeturl in TargetUrls:
            # 设定储存容器 #
            item = KeywordItem()
            # 关键词 #
            item['Keyword'] = keyword[0]
            # 提取微博的唯一标识符：contentid
            contentid = targeturl.xpath('@id').extract_first() # Weibo ContentID
            # 提取微博内容 #
            content = targeturl.xpath('div/span[@class="ctt"]/text()').extract_first() # Weibo Content

            # 提取其他指标数据 #
            repost = re.findall(u'\u8f6c\u53d1\[(\d+)\]', targeturl.extract())
            commentnum = re.findall(u'\u8bc4\u8bba\[(\d+)\]', targeturl.extract())
            like = re.findall(u'\u8d5e\[(\d+)\]', targeturl.extract())
            # 提取微博发送时间数据 #
            others = targeturl.xpath('div/span[@class="ct"]/text()').extract_first()

            # 将数据保存到容器item中 #
            item['ContentId'] = contentid
            if content:
                item["Content"] = content.strip(u"[\u4f4d\u7f6e]")
            if like:
                item["LikeNum"] = str(like[0])

            # 提取组图URL,若一条微博存在多张GIF，则存储父链接 TotalUrl
            TotalUrl = targeturl.xpath(u'div/a[contains(text(),"\u7ec4\u56fe")]/@href').extract()
            # 提取页面中显示的GIF链接 #
            gifurl = targeturl.xpath('div/a/img[@class="ib"]/@src').extract_first() # GIF Url
            # 判断微博中存在一张还是多张GIF图，然后构建不同的 MyUrl
            MyUrl = TotalUrl[0] if TotalUrl else gifurl.replace('wap180', 'large')
            if repost:
                item["RepostNum"] = str(repost[0])
            if commentnum:
                item["CommentNum"] = str(commentnum[0])
            # 提取微博发送时间数据 #
            if others:
                others = others.split(u"\u6765\u81ea")
                item["PostTime"] = others[0]
            # 提取微博评论链接，并利用 parse_Comment 函数进行解析 #
            # 其中评论数据以 list 形式呈现出来 #
            Comment_url = targeturl.xpath("div/a[@class='cc' and @href]/@href").extract_first()
            item['ContentUrl'] = Comment_url
            CommentList = []
            yield Request(url = Comment_url, meta = {'item': item, 'Comment': CommentList, 'GIFUrl': MyUrl}, callback = self.parse_Comment)
        if Content_nextpage := sel.xpath(
            "//div[@id='pagelist']/form/div/a[1]/@href"
        ).extract():
            yield Request(url = self.host + Content_nextpage[0], callback = self.parse)


    # 定义提取评论数据的函数 #
    def parse_Comment(self, response):
        """提取评论数据"""
        item = response.meta['item']
        CommentList = response.meta['Comment']
        MyUrl = response.meta['GIFUrl']
        sel = Selector(response)
        # 提取页面中评论数据的模块 #
        tweets = sel.xpath('body/div[@class="c" and @id]')
        # 遍历当前页面中的评论数据，并保存到 CommentList 中 #
        for tweet in tweets:
            Cond1 = tweet.xpath('a/@href').extract_first()
            if Cond1:
                comment = tweet.xpath('span[@class="ctt"]/text()').extract()
                if len(comment) > 1:
                    CommentList.append(comment[1].strip(u"[\u4f4d\u7f6e]"))
                elif len(comment) == 1:
                    CommentList.append(comment[0].strip(u"[\u4f4d\u7f6e]"))

        # 判断是否有下一页的选项 #
        Comment_nextpage = sel.xpath(
            u'body//div[@class="pa" and @id="pagelist"]/form/div/a[text()="\u4e0b\u9875"]/@href').extract()
        # 翻页并继续解析 #
        if Comment_nextpage:
            yield Request(url=self.host + Comment_nextpage[0], meta = {'item': item, 'Comment': CommentList, 'GIFUrl': MyUrl}, callback=self.parse_Comment)
        # 否则将评论数据保存到 item 中 #
        else:
            item['Comment'] = CommentList
            Cond_gif = re.findall(r'.gif', MyUrl)
            # 如果 MyUrl 为gif链接，则直接将 MyUrl 保存到 item 中，并传递到 pipeline 中
            if Cond_gif:
                item['GIFUrl'] = MyUrl
                yield item
                print "GIFUrl is saved!!!"
                print 'No more Search Comment!!!'
            # 否则，传递到 parse_Picture 函数中继续解析 #
            else:
                yield Request(url = MyUrl, meta = {'item':item}, callback = self.parse_Picture)


    # 定义解析GIF组图URL的函数 #
    def parse_Picture(self, response):
        sel = Selector(response)
        item = response.meta['item']
        # 提取网页中所有GIF图片的URL #
        TargetUrls = sel.xpath("//img[contains(@src, '.gif')]/@src").extract()
        # 构建最终的 GIFUrl #
        MyUrl = [targeturl.replace('thumb180', 'large') for targeturl in TargetUrls]
        item['GIFUrl'] = MyUrl
        yield item
        print "GIFUrl is saved!!!"




