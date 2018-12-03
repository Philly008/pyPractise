# -*- coding: utf-8 -*-
# @Time       : 2018/12/3 11:34
# @Author     : Philly
# @File       : all_scrapers.py
# @Description: 
import re
from bs4 import BeautifulSoup
from lxml.html import fromstring


FIELDS = ('area', 'population', 'iso', 'country_or_district', 'capital',
          'continent', 'tld', 'currency_code', 'currency_name', 'phone',
          'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')
'''
因 language 少写 s 导致 IndexError，先try...except... 再 DEBUG 跟踪到 language 属性少写 s ，巨坑==^崩溃^==
'''


def re_scraper(html):
    results = {}
    for field in FIELDS:
        results[field] = re.search(
                '<tr id="places_%s__row">.*?<td class="w2p_fw">(.*?)</td>'
                % field, html).groups()[0]
    return results


def bs_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = {}
    for field in FIELDS:
        results[field] = soup.find('table').find('tr', id='places_%s__row' %
                                                     field).find('td', class_='w2p_fw').text
    return results


def lxml_scraper(html):
    tree = fromstring(html)
    results = {}
    for field in FIELDS:
        results[field] = tree.cssselect(
                'table > tr#places_%s__row > td.w2p_fw' % field)[0].text_content()
    return results


def lxml_xpath_scraper(html):
    tree = fromstring(html)
    results = {}
    for field in FIELDS:
        results[field] = tree.xpath('//tr[@id="places_%s__row"]/td[@class="w2p_fw"]' % field)[0].text_content()
    return results


# if __name__ == '__main__':
#     html = """
#     <form action="#" enctype="multipart/form-data" method="post"><table><tr id="places_flag_img__row"><td class="w2p_fl"><label class="readonly" for="places_flag_img" id="places_flag_img__label">Flag: </label></td><td class="w2p_fw"><img src="/places/static/images/flags/gb.png" /></td><td class="w2p_fc"></td></tr><tr id="places_area__row"><td class="w2p_fl"><label class="readonly" for="places_area" id="places_area__label">Area: </label></td><td class="w2p_fw">244,820 square kilometres</td><td class="w2p_fc"></td></tr><tr id="places_population__row"><td class="w2p_fl"><label class="readonly" for="places_population" id="places_population__label">Population: </label></td><td class="w2p_fw">62,348,447</td><td class="w2p_fc"></td></tr><tr id="places_iso__row"><td class="w2p_fl"><label class="readonly" for="places_iso" id="places_iso__label">Iso: </label></td><td class="w2p_fw">GB</td><td class="w2p_fc"></td></tr><tr id="places_country_or_district__row"><td class="w2p_fl"><label class="readonly" for="places_country_or_district" id="places_country_or_district__label">Country (District): </label></td><td class="w2p_fw">United Kingdom</td><td class="w2p_fc"></td></tr><tr id="places_capital__row"><td class="w2p_fl"><label class="readonly" for="places_capital" id="places_capital__label">Capital: </label></td><td class="w2p_fw">London</td><td class="w2p_fc"></td></tr><tr id="places_continent__row"><td class="w2p_fl"><label class="readonly" for="places_continent" id="places_continent__label">Continent: </label></td><td class="w2p_fw"><a href="/places/default/continent/EU">EU</a></td><td class="w2p_fc"></td></tr><tr id="places_tld__row"><td class="w2p_fl"><label class="readonly" for="places_tld" id="places_tld__label">Tld: </label></td><td class="w2p_fw">.uk</td><td class="w2p_fc"></td></tr><tr id="places_currency_code__row"><td class="w2p_fl"><label class="readonly" for="places_currency_code" id="places_currency_code__label">Currency Code: </label></td><td class="w2p_fw">GBP</td><td class="w2p_fc"></td></tr><tr id="places_currency_name__row"><td class="w2p_fl"><label class="readonly" for="places_currency_name" id="places_currency_name__label">Currency Name: </label></td><td class="w2p_fw">Pound</td><td class="w2p_fc"></td></tr><tr id="places_phone__row"><td class="w2p_fl"><label class="readonly" for="places_phone" id="places_phone__label">Phone: </label></td><td class="w2p_fw">44</td><td class="w2p_fc"></td></tr><tr id="places_postal_code_format__row"><td class="w2p_fl"><label class="readonly" for="places_postal_code_format" id="places_postal_code_format__label">Postal Code Format: </label></td><td class="w2p_fw">@# #@@|@## #@@|@@# #@@|@@## #@@|@#@ #@@|@@#@ #@@|GIR0AA</td><td class="w2p_fc"></td></tr><tr id="places_postal_code_regex__row"><td class="w2p_fl"><label class="readonly" for="places_postal_code_regex" id="places_postal_code_regex__label">Postal Code Regex: </label></td><td class="w2p_fw">^(([A-Z]\d{2}[A-Z]{2})|([A-Z]\d{3}[A-Z]{2})|([A-Z]{2}\d{2}[A-Z]{2})|([A-Z]{2}\d{3}[A-Z]{2})|([A-Z]\d[A-Z]\d[A-Z]{2})|([A-Z]{2}\d[A-Z]\d[A-Z]{2})|(GIR0AA))$</td><td class="w2p_fc"></td></tr><tr id="places_languages__row"><td class="w2p_fl"><label class="readonly" for="places_languages" id="places_languages__label">Languages: </label></td><td class="w2p_fw">en-GB,cy-GB,gd</td><td class="w2p_fc"></td></tr><tr id="places_neighbours__row"><td class="w2p_fl"><label class="readonly" for="places_neighbours" id="places_neighbours__label">Neighbours: </label></td><td class="w2p_fw"><div><a href="/places/default/iso/IE">IE </a></div></td><td class="w2p_fc"></td></tr></table><div style="display:none;"><input name="id" type="hidden" value="659513" /></div></form>
#     """
#     print(lxml_xpath_scraper(html)['area'])

