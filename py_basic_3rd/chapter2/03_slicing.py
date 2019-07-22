# -*- coding: utf-8 -*-
# @Time       : 2019/3/26 13:18
# @Author     : Philly
# @File       : 03_slicing.py
# @Description: 切片操作示例

# 从类似于http://www.something.com的URL中提起域名
url = input('Please enter the URL: ')
domain = url[11:-4]

print("Domain name: " + domain)

