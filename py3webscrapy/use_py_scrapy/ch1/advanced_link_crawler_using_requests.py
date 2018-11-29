# -*- coding: utf-8 -*-
# @Time       : 2018/11/29 16:19
# @Author     : Philly
# @File       : advanced_link_crawler_using_requests.py
# @Description: 使用requests 库爬虫链接
import re
from urllib import robotparser
from urllib.parse import urljoin
import requests
from py3webscrapy.use_py_scrapy.ch1.throttle import Throttle


def download(url, user_agent='wswp', num_retries=2, proxies=None):
    print('Downloading: ', url)
    headers = {'User-Agent': user_agent}
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
        html = resp.text
        if resp.status_code >= 400:
            print('Download error: ', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                return download(url, num_retries - 1)
    except requests.exception.RequestsException as e:
        print('Download error: ', e)
        html = None
    return html

def get_robots_parser(robots_url):
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp

def get_links(html):
    webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']""", re.IGNORECASE)
    return webpage_regex.findall(html)

def link_crawler(start_url, link_regex, robots_url=None, user_agent='wswp', proxies=None, delay=3, max_depth=4):
    crawl_queue = [start_url]
    seen = {}
    if not robots_url:
        robots_url = '{}/robots.txt'.format(start_url)
    rp = get_robots_parser(robots_url)
    throttle = Throttle(delay)
    while crawl_queue:
        url = crawl_queue.pop()
        if rp.can_fetch(user_agent, url):
            depth = seen.get(url, 0)
            if depth == max_depth:
                print('Skipping %s due to depth' % url)
                continue
            throttle.wait(url)
            html = download(url, user_agent=user_agent, proxies=proxies)
            if not html:
                continue
            for link in get_links(html):
                if re.match(link_regex, link):
                    abs_link = urljoin(start_url, link)
                    if abs_link not in seen:
                        seen[abs_link] = depth + 1
                        crawl_queue.append(abs_link)
        else:
            print('Blocked by robots.txt: ', url)


if __name__ == '__main__':
    link_crawler('http://example.python-scraping.com', '/places/default/(index|view)/', max_depth=2)
