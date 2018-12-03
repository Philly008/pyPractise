# -*- coding: utf-8 -*-
# @Time       : 2018/11/29 17:27
# @Author     : Philly
# @File       : lxml_prac.py
# @Description: 
from lxml.html import fromstring, tostring
from py3webscrapy.use_py_scrapy.ch1.advanced_link_crawl import download

broken_html = '<ul class=country_or_district><li>Area<li>Population</ul>'
tree = fromstring(broken_html)  # parse the HTML
fixed_html = tostring(tree, pretty_print=True)
print(fixed_html)


url = 'http://example.python-scraping.com/view/UnitedKingdom-239'
html = download(url)
tree = fromstring(html)
td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
area = td.text_content()
print(area)

"""常用的CSS选择器：
select any tag: *
select by tag <a>: a
select by class of "link":  .link
select by tag <a> with class "link":    a.link
select by tag <a> with ID "home": a#home
select by child <span> of tag <a>: a > span
select by descendant(后代，后裔) <span> of tag <a>: a span
select by tag <a> with attribute title of "Home": a[title=Home]
"""
table = tree.xpath('//table')[0]
print(table.getchildren())  # 查看所有子元素
prev_sibling = table.getprevious()  # 查看兄弟元素
print('左兄弟元素是：' + str(prev_sibling))
next_sibling = table.getnext()
print('右兄弟元素是：' + str(next_sibling))
print('父元素是：' + str(table.getparent()))




