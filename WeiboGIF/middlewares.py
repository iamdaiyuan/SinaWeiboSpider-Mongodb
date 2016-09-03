#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: fansan
# @Date:   2016-03-11 17:09:06
# @Last Modified by:   fansan
# @Last Modified time: 2016-06-14 00:08:10

import random

from agents import AGENTS
from cookies import cookies

# Change User-Agent #
class CustomUserAgentMiddleware(object):
    """docstring for CustomUserAgentMiddleware"""
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent

# Change Cookie #
class CustomCookieMiddleware(object):
    """docstring for CustomCookieMiddleware"""
    def process_request(self, request, spider):
        cookie = random.choice(cookies)
        request.cookies = cookie


