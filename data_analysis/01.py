#!/usr/bin/python
# -*- coding:utf-8 -*-
import time

import requests
from bs4 import BeautifulSoup

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
# kv = {'key1': 'val1', 'key2': 'val2'}
# r1 = requests.request('GET', 'http://httpbin.org/get', params=kv)
# print(r1.url)
# fs = {'file': open('data.xls', 'wb')}
# r2 = requests.request('POST', 'http://httpbin.org/post', files=fs)
# pxs = {'http': 'ip1', 'https': 'ip2'}
# r3 = requests.request('GET', 'http://httpbin.org/get', proxies=pxs)

# 5
# def getHTMLText(url):
#     try:
#         r = requests.get('https://www.icourse163.org/', time=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "产生异常"
# if __name__ == "__main__":
#     url = "http://www.httpbin.org/"
#     totaltime = 0
#     for i in range(100):
#         # starttime = time.perf_counter()
#         starttime = time.time()
#         getHTMLText(url)
#         # endtime = time.perf_counter()
#         endtime = time.time()
#         totaltime = totaltime + endtime - starttime
#     print("TotalTime:", totaltime)

# 6
# url = 'https://item.jd.com/100009691096.html'
# try:
#     kv = {'user-agent': 'Mozilla/5.0'}
#     r = requests.get(url, headers=kv)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[:1000])
# except:
#     print('爬取失败')


# r = requests.get("http://python123.io/ws/demo.html")
# print(r.text)

demo = """<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>
</body></html>"""

# 7
# soup = BeautifulSoup(demo, 'html.parser')
# print(soup)
# print(soup.a.name)
# print(soup.a.parent.name)
# print(soup.a.parent.parent.name)
# print(soup.a.attrs)
# print(soup.a.attrs['href'])
# print(soup.a.string)
# print(soup.p.string)
# print(soup.select('p'))
# soup2 = BeautifulSoup(open("D://demo.html"), 'html.parser')

# 8
soup = BeautifulSoup(demo, 'html.parser')
# print(soup.head)
# print(soup.head.contents)
# print(soup.body.contents)
# print(soup.body.contents[1])
# print(soup.p.parent)
# print(soup.p.parents)
print(soup.a.next_sibling)
print(soup.a.previous_sibling)












