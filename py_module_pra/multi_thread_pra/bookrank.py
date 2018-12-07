# -*- coding: utf-8 -*-
# @Time       : 2018/12/6 14:10
# @Author     : Philly
# @File       : bookrank.py
# @Description:
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen


REGEX = compile('#([\d,]+) in Books ')
AMZN = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals'
}

def getRanking(isbn):
    page = uopen('%s%s' % (AMZN, isbn))
    data = page.read()
    page.close()
    print(type(data))
    return REGEX.findall(str(data))[0]

def _showRanking(isbn):
    print(type(ISBNs[isbn]))
    print(type(getRanking(isbn)))
    print('- %s ranked %s' % (ISBNs[isbn], getRanking(isbn)))

def _main():
    print('At', ctime(), 'on Amazon...')
    for isbn in ISBNs:
        _showRanking(isbn)

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()



