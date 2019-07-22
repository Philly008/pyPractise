# -*- coding: utf-8 -*-
# @Time       : 2019/5/5 9:34
# @Author     : Philly
# @File       : beautiful_scratch.py
# @Description: 使用Beautiful Soup的屏幕抓取程序
from urllib.request import urlopen
from bs4 import BeautifulSoup

text = urlopen('http://python.org/jobs').read()
soup = BeautifulSoup(text, 'html.parser')

jobs = set()
for job in soup.body.section('h2'):
    jobs.add('{}({})'.format(job.a.string, job.a['href']))

print('\n'.join(sorted(jobs, key=str.lower)))

