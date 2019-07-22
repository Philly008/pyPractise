# -*- coding: utf-8 -*-
# @Time       : 2019/4/18 17:13
# @Author     : Philly
# @File       : scratch_simple.py
# @Description: 简单的屏幕抓取程序
from urllib.request import urlopen
import re


p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text = urlopen('http://python.org/jobs').read().decode()
for url, name in p.findall(text):
    print('{} ({})'.format(name, url))


