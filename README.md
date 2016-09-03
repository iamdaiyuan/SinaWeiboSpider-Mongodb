# 微博 GIF 爬虫程序

## 爬虫功能

此项目主要用于从新浪微博网页中爬取目标用户带有 *gif* 的微博。(可按需求修改,爬取自己想要的内容)

爬取内容：

新建一个名为 **SinaWeibo** 的数据库。

Part1: 通过用户关键字搜索获取的内容，数据储存在表 **WeiboGIF** 中。

- ContentUrl: 带有 gif 的新浪微博 URL 地址
- PostTime: 微博的发送时间
- ContentId: 微博的唯一标识符
- RepostNum: 微博的转发数
- CommentNum: 微博的评论数
- Content: 微博的文本内容
- GIFUrl: gif 图片的 URL 地址
- LikeNum: 点赞数
- Comment: 微博评论内容

Part2: 通过微博关键字搜索获取的内容，数据储存在表 **WeiboKeyword** 中。

- Keyword: 微博关键字
- ContentUrl: 带有 gif 的新浪微博 URL 地址
- PostTime: 微博的发送时间
- ContentId: 微博的唯一标识符
- RepostNum: 微博的转发数
- CommentNum: 微博的评论数
- Content: 微博的文本内容
- GIFUrl: gif 图片的 URL 地址
- LikeNum: 点赞数
- Comment: 微博评论内容

## 环境、架构

- 开发语言: python2.7
- 开发环境: OS X EI Capitan
- 数据库: MongoDB 3.2.1
- 爬虫框架: Scrapy


## 部署环境

1. 安装 mongodb
2. 安装 Scrapy 软件库
3. python 模块: pymongo, requests, base64, urllib, re, time, datetime, json
4. 登陆微博的账号和密码置于 **cookies.py** 中
5. 用户搜索关键字置于 **startuser.py** 中
6. 微博搜索关键字置于 **startkeyword.py** 中

## 执行程序

总共有三个需求，分别对应三个Python文件:

**首先启动 MongoDB，然后切换到这三个文件所在的路径中，再根据需求执行相应的文件:**

- 爬取用户所有微博: **RunTotalFiles.py**
- 爬取用户每天新更新的微博: **RunDailyTask.py**
- 爬取包含关键词的微博: **RunKeyword.py**


- @author: fansan
- @email: fansan@live.com