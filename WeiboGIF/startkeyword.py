# -*- coding: utf-8 -*-
# @Author: fansan
# @Date:   2016-06-15 20:10:53
# @Last Modified by:   fansan
# @Last Modified time: 2016-06-18 14:08:48

import urllib

# 添加搜索关键字 #
KeyWord = ['gif 小清新' ,
           'gif 萌宠',
           'gif 化妆',
           'gif 宋仲基',
           'gif tumblr',
           'gif Twitter',
           'gif 一言不合',
           'gif 勒夫',
           'gif 美图',
           'gif 漫威',
           'gif 卷福',
           'gif 懒蛋蛋',
           'gif 表情包',
           'gif 比赛',
           'gif 汽车',
           'gif 军事',
           'gif 动图+极限挑战',
           'gif 张艺兴',
           'gif 鹿晗',
           'gif 吴亦凡',
           'gif 胡歌',
           'gif 霍建华',
           'gif 抖森',
           'gif 灾难',
           'gif 美食',
           'gif 旅行',
           'gif 污',
           'gif 福利',
           'gif 内涵',
           'gif 极限运动',
           'gif 科技',
           'gif 作死',
           'gif 风景',
           'gif 不动戳大',
           'gif 动态图猜出处',
           'gif 搞笑GIF',
           'gif 艺术',
           'gif 设计',
           'gif 动物',
           'gif NBA精彩GIF',
           'gif 反应',]


StartKeyword = ['http://weibo.cn/search/mblog/?' + urllib.urlencode({'keyword': word, 'page': '1'}) for word in KeyWord]
