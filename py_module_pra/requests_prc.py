# -*- coding: utf-8 -*-
# @Time       : 2018/11/26 11:40
# @Author     : Philly
# @File       : requests_prc.py
# @Description: requests模块练习：http://docs.python-requests.org/en/master/user/quickstart/
import requests

# get请求网页
r = requests.get('https://api.github.com/events', stream=True)
# POST请求
r1 = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(r.text)
print(r.encoding)
print(r.content)
r.encoding = 'ISO-8859-1'
print(r.content)
print(r.encoding)
print(r.json())
print(r.status_code)
print(r.raise_for_status())
print(r.raw)
print(r.raw.read())
print(r.iter_content(chunk_size=128))
print(r.headers)
print('headers:啦啦啦')
print(r.headers.get('content-type'))

print(r1)

with open(r'E:\workspace\pyPractise\py_module_pra\filename', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r2 = requests.get('https://httpbin.org/get', params=payload)
print(r2.url)

#
# from PIL import Image
# from io import BytesIO
#
# i = Image.open(BytesIO(r.content))  # Binary Response Content

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r4 = requests.get(url, headers=headers)  # Custom Headers

payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
# send some form-encoded data
r5 = requests.post('https://httpbin.org/post', data=payload_tuples)
print(r5.text)


import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
# json.dumps()  把对象转换成json字符串
r6 = requests.post(url, data=json.dumps(payload))


url = 'https://httpbin.org/post'
# files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
files = {'file':('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
r7 = requests.post(url, files=files)
print(r7.text)


url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)
print(r.cookies)  # cookies are returned in a RequestsCookieJar


r = requests.get('http://github.com/', allow_redirects=True)
print(r.url, '\n', r.history)


requests.get('https://github.com/', timeout=0.001)



