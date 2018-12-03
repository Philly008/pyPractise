# -*- coding: utf-8 -*-
# @Time       : 2018/11/29 17:11
# @Author     : Philly
# @File       : beautifu_soup.py
# @Description: 
from bs4 import BeautifulSoup
from pprint import pprint


broken_html = '<u class=country_or_district><li>Area<li>Population</ul>'
# parser the HTML
soup = BeautifulSoup(broken_html, 'html.parser')
fixed_html = soup.prettify()
pprint(fixed_html)

soup2 = BeautifulSoup(broken_html, 'html5lib')  # 使用html5lib解析器
fixed_html2 = soup.prettify()
pprint(fixed_html2)


