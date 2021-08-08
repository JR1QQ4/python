#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests

# 1
# res = requests.get('http://www.baidu.com')
# print(res.text)
# print(res.encoding)  # ISO-8859-1
# print(res.apparent_encoding)  # utf-8
# res.encoding = res.apparent_encoding
# print(res.text)

# 2
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "产生异常"
# if __name__ == '__main__':
#     url = 'www.baidu.com'
#     print(getHTMLText(url))

# 3
# r1 = requests.head("http://httpbin.org/head")
# print(r1.headers)
# print(r1.text)
# payload = {'key1': 'val1', 'key2': 'val2'}
# r2 = requests.post('http://httpbin.org/post', data=payload)
# print(r2.text)
# r3 = requests.post('http://httpbin.org/post', data='ABC')
# print(r3.text)

# 4
kv = {'key1': 'val1', 'key2': 'val2'}
r1 = requests.request('GET', 'http://httpbin.org/get', params=kv)
print(r1.url)
fs = {'file': open('data.xls', 'wb')}
r2 = requests.request('POST', 'http://httpbin.org/post', files=fs)
pxs = {'http': 'ip1', 'https': 'ip2'}
r3 = requests.request('GET', 'http://httpbin.org/get', proxies=pxs)









