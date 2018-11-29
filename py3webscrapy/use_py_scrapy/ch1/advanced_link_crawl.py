# -*- coding: utf-8 -*-
# @Time       : 2018/11/27 16:38
# @Author     : Philly
# @File       : advanced_link_crawl.py
# @Description: 高级功能的链接爬取
import re
import urllib.request
from urllib import robotparser
from urllib.error import URLError, HTTPError, ContentTooShortError
from urllib.parse import urljoin

from py3webscrapy.use_py_scrapy.ch1.throttle import Throttle


def download(url, user_agent='wswp', num_retries=2, charset='utf-8', proxy=None):
    print('Downloading: ', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        if proxy:
            proxy_support = urllib.request.ProxyHandler({'http': proxy})
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error: ', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries-1)
    return html

def link_crawler(start_url, link_regex, robots_url=None, user_agent='wswp', proxy=None, delay=3, max_depth=4):
    """Crawl from the given start URL following links matched by link_regex"""
    crawl_queue = [start_url]
    # keep track which URL's have seen before
    seen = {}

    if not robots_url:
        robots_url = '{}/robots.txt'.format(start_url)
    rp = get_robots_parser(robots_url)
    throttle = Throttle(delay)
    while crawl_queue:
        url = crawl_queue.pop()
        # check url passes robots.txt restrictions
        if rp.can_fetch(user_agent, url):
            depth = seen.get(url, 0)
            if depth == max_depth:
                print('Skipping %s due to depth' % url)
                continue
            throttle.wait(url)  # 下载限速
            html = download(url, user_agent=user_agent, proxy=proxy)
            if not html:
                continue

            # filter for links matching our regular expression
            for link in get_links(html):
                if re.match(link_regex, link):
                    abs_link = urljoin(start_url, link)  # 解析成绝对路径
                    if abs_link not in seen:
                        seen[abs_link] = depth + 1
                        crawl_queue.append(abs_link)
        else:
            print('Blocked by robots.txt: ', url)

def get_links(html):
    """Return a list of links from html"""
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']""", re.IGNORECASE)
    # webpage_regex = re.compile("""<a href=.*>""", re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

# 解析robots
def get_robots_parser(robots_url):
    """Return the robots parser object using the robots_url"""
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp

if __name__ == '__main__':
    link_crawler('http://example.python-scraping.com', '/places/default/(index|view)/', max_depth=1)



