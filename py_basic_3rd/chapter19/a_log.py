# -*- coding: utf-8 -*-
# @Time       : 2019/5/5 16:34
# @Author     : Philly
# @File       : a_log.py
# @Description: 一个使用模块logging的程序
import logging

logging.basicConfig(level=logging.INFO, filename='mylog.log')
logging.info('Starting program')
logging.info('Trying to divide 1 by 0')
print(1 / 0)
logging.info('The division succeeded')
logging.info('Ending program')

