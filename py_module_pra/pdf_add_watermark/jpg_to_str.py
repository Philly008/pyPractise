# -*- coding: utf-8 -*-
# @Time       : 2019/7/26 10:14
# @Author     : Philly
# @File       : jpg_to_str.py
# @Description: 将图片转换成字符串
import base64
import os
image = 'logo.jpg'

# with open(image, 'rb') as f:
#     str = base64.b64encode(f.read())
# print(type(str))

cur_path = os.getcwd()
print(cur_path)
if not os.path.exists('shuiyin'):
    os.mkdir('shuiyin')

shuiyin_path = cur_path + '\\shuiyin\\'
print(shuiyin_path)