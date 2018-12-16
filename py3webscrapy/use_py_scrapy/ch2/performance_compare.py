# -*- coding: utf-8 -*-
# @Time       : 2018/12/3 11:50
# @Author     : Philly
# @File       : performance_compare.py
# @Description: 不同方式爬虫性能对比，强烈建议使用 lxml 解析，lxml 是抓取数据的最佳选择
import time
import re
from py3webscrapy.use_py_scrapy.ch2.all_scrapers import re_scraper, bs_scraper, lxml_scraper,lxml_xpath_scraper
from py3webscrapy.use_py_scrapy.ch1.advanced_link_crawl import download


NUM_ITERATIONS = 5000  # number of times to test each scraper
html = download('http://example.python-scraping.com/places/default/view/United-Kingdom-233')

scrapers = [
    ('Regular expressions', re_scraper),
    ('BeautifulSoup', bs_scraper),
    ('Lxml', lxml_scraper),
    ('Xpath', lxml_xpath_scraper)
]

for name, scraper in scrapers:
    # record start time of scrape
    start = time.time()
    for i in range(NUM_ITERATIONS):
        if scraper == re_scraper:
            re.purge()  # 清除正则表达式缓存
        result = scraper(html)
        # check scraped result is as expected
        assert result['area'] == '244,820 square kilometres'
    # record end time of scrape and output the total
    end = time.time()
    print('%s: %.2f seconds' % (name, end - start))


