# -*- coding: utf-8 -*-
# @Time       : 2018/11/27 13:34
# @Author     : Philly
# @File       : down_webpage.py
# @Description: 下载网页
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError


def download(url, user_agent='wswp', num_retries=2):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)    # 设置用户代理
    try:
        html = urllib.request.urlopen(request).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries-1)
    return html


if __name__ == '__main__':
    download('http://httpstat.us/500')
















