#!/usr/bin/python
# -*- coding:utf-8 -*-
import re
import time
from pprint import pprint

import requests
import bs4
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
# soup = BeautifulSoup(demo, 'html.parser')
# print(soup.head)
# print(soup.head.contents)
# print(soup.body.contents)
# print(soup.body.contents[1])
# print(soup.p.parent)
# print(soup.p.parents)
# print(soup.a.next_sibling)
# print(soup.a.previous_sibling)

# 9
# soup = BeautifulSoup(demo, 'html.parser')
# all_a = soup.find_all('a')
# print(all_a)
# all_a_b = soup.find_all(['a', 'b'])
# print(all_a_b)
# for tag in soup.find_all(True):
#     print(tag.name)
# 以 b 开始的标签
# for tag in soup.find_all(re.compile('b')):
#     print(tag.name)
# 包含某个字符串
# contains_str = soup.find_all('p', 'course')
# print(contains_str)
# contains_id = soup.find_all(id='link1')
# print(contains_id)
# contains_id = soup.find_all(id=re.compile('link'))
# print(contains_id)
# 获取文本
# get_str = soup.find_all(string='Basic Python')
# print(get_str)
# get_str = soup.find_all(string=re.compile('python'))
# print(get_str)

# 10
# def getHTMLText(url):
#     # noinspection PyBroadException
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return ""
# def fillUnivList(uList, html):
#     soup = BeautifulSoup(html, 'html.parser')
#     for tr in soup.find('tbody').children:
#         if isinstance(tr, bs4.element.Tag):
#             tds = tr('td')
#             uList.append([tds[0].string.strip(), tds[1].find(class_='name-cn').string, tds[4].string.strip()])
# def printUnivList(uList, num):
#     tplt = "{0:<6}\t{1:{3}<10}\t{2:<6}"
#     print(tplt.format("排名", "学校名称", "总分", chr(12288)))
#     for i in range(num):
#         u = uList[i]
#         print(tplt.format(u[0], u[1], u[2], chr(12288)))
# def main():
#     uInfo = []
#     url = 'https://www.shanghairanking.cn/rankings/bcur/2021'
#     html = getHTMLText(url)
#     fillUnivList(uInfo, html)
#     printUnivList(uInfo, 20)
# if __name__ == '__main__':
#     main()

# 11
# match = re.search(r'[1-9]\d{5}', 'BIT 100081')
# if match:
#     print(match.group(0))  # 100081
# match1 = re.match(r'[1-9]\d{5}', 'BIT 100081')
# if match1:  # 空，match 从头开始
#     print(match1.group(0))
# match2 = re.match(r'[1-9]\d{5}', '100081 BIT')
# if match2:
#     print(match2.group(0))  # 100081
# match3 = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# print(match3)  # ['100081', '100084']
# match4 = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# print(match4)  # ['BIT', ' TSU', '']
# match5 = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
# print(match5)  # ['BIT', ' TSU100084']
# for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
#     if m:
#         print(m.group(0))  # 100081  100084
# match6 = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084')
# print(match6)  # BIT:zipcode TSU:zipcode

# 12
# m = re.search(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# print(m.string)  # BIT100081 TSU100084
# print(m.re)  # re.compile('[1-9]\\d{5}')
# print(m.pos)  # 0
# print(m.endpos)  # 19
# print(m.group(0))  # 100081
# print(m.start())  # 3
# print(m.end())  # 9
# print(m.span())  # (3, 9)

# 13
# match = re.search(r'PY.*N', 'PYANBNCNDN')
# print(match.group(0))  # PYANBNCNDN
# match1 = re.search(r'PY.*?N', 'PYANBNCNDN')
# print(match1.group(0))  # PYAN






