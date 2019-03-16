# -*- coding: utf-8 -*-
# @Time       : 2019/3/16 21:02
# @Author     : Philly
# @File       : run_tests.py
# @Description: 
import time, sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from pyrequests.HTMLTestRunner import HTMLTestRunner
import unittest
from pyrequests.db_fixture import test_data


# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == '__main__':
    test_data.init_data()   # 出啊石化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Guest Manage System Interface Test Report',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()


