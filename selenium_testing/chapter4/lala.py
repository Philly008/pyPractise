# -*- coding: utf-8 -*-
# @Time       : 2018/12/17 17:16
# @Author     : Philly
# @File       : lala.py
# @Description: 
from time import gmtime, strftime


user_name = "user_" + strftime("%Y%m%d%H%M%S", gmtime())
# print(user_name)


desired_caps = {}
desired_caps['platform'] = "2"
desired_caps['browser'] = "3"
print(str(desired_caps))