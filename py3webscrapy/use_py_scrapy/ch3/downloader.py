# -*- coding: utf-8 -*-
# @Time       : 2018/12/4 11:42
# @Author     : Philly
# @File       : downloader.py
# @Description: 为链接爬虫添加缓存支持
from py3webscrapy.use_py_scrapy.ch1.throttle import Throttle
from random import choice
import requests


class Downloader:
    def __init__(self, delay=5, user_agent='wswp', proxies=None, cache={}):
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = None     # we will set this per request
        self.cache = cache

    def __call__(self, url, num_retries=2):
        self.num_retries = num_retries
        try:
            result = self.cache[url]
            print('Loaded from cache: ', url)
        except KeyError:
            result = None
        if result and self.num_retries and 500 <= result['code'] < 600:
            # server error so ignore result from cache and re-download
            result = None
        if result is None:
            # result was not loaded from cache so still need to download
            self.throttle.wait(url)
            proxies = choice(self.proxies) if self.proxies else None
            headers = {'User-Agent': self.user_agent}
            result = self.download(url, headers, proxies)
            if self.cache:
                # save result to cache
                self.cache[url] = result
        return result['html']

    def download(self, url, headers, proxies, num_retries):
        print('Downloading: ', url)
        try:
            resp = requests.get(url, headers=headers, proxies=proxies, timeout=self.timeout)
            html = resp.text
            if resp.status_code >= 400:
                print('Download error: ', resp.text)
                html = None
                if self.num_retries and 500 <= resp.status_code < 600:
                    self.num_retries -= 1
                    return self.download(url, headers, proxies)
        except requests.exception.RequestsException as e:
            print('Download error: ', e)
            return {'html': None, 'code': 500}
        return {'html': html, 'code': resp.status_code}

