# -*- coding: utf-8 -*-
# @Time       : 2019/7/24 16:24
# @Author     : Philly
# @File       : 16.py
# @Description: 16 lines: csv module, tuple unpacking
import csv, operator

# write stocks data as comma-separated values
# writer = csv.writer(open('stocks.csv', 'w', newline=''))
# writer.writerows([
#     ('GOOG', 'Google, Inc.', 505.24, 0.47, 0.09),
#     ('YHOO', 'Yahoo! Inc.', 27.38, 0.33, 1.22),
#     ('CNET', 'CNET Networks, Inc.', 8.62, -0.13, -1.49)
# ])

# read stocks data, print status messages
stocks = csv.reader(open('stocks.csv', 'r'))

status_labels = {-1: 'down', 0: 'unchanged', 1: 'up'}
print(stocks)
for ticker, name, price, change, pct in stocks:     # 文件存在空行导致没有进入for
    status = status_labels[operator.eq(float(change), 0.0)]
    print('%s is %s (%s%%)' % (name, status, pct))

