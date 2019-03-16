# -*- coding: utf-8 -*-
# @Time       : 2019/3/12 22:31
# @Author     : Philly
# @File       : interface_test.py
# @Description: 
import requests
import unittest


class GetEventListTest(unittest.TestCase):
    ''' 查询发布会接口测试 '''
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"

    def test_get_event_null(self):
        ''' 发布会 id 为空 '''
        r = requests.get(self.url, params={'eid':''})
        result = r.json()
        print(result)
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], "parameter error")

    def test_get_event_success(self):
        r = requests.get(self.url, params={'eid':'1'})
        result = r.json()
        print(result)
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],"success")
        self.assertEqual(result['data']['name'],"红米发布会")

if __name__ == '__main__':
    unittest.main()









