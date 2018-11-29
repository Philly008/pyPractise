# -*- coding: utf-8 -*-
# @Time       : 2018/11/27 16:03
# @Author     : Philly
# @File       : higher_fun.py
# @Description: 
from urllib import robotparser

rp = robotparser.RobotFileParser()
rp.set_url('http://example.python-scraping.com/robots.txt')
print(rp.read())
url = 'http://example.python-scraping.com'
user_agent = 'BadCrawler'
print(rp.can_fetch(user_agent, url))
user_agent = 'GoodCrawler'
print(rp.can_fetch(user_agent, url))


