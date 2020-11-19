#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第二部分 自动化任务

print('********* 第 11 章 从 Web 抓取信息 ***********')

# webbrowser：是 Python 自带的，打开浏览器获取指定页面
# requests：从因特网上下载文件和网页
# Beautiful Soup：解析 HTML，即网页编写的格式
# selenium：启动并控制一个 Web 浏览器。 selenium 能够填写表单，并模拟鼠标在这个浏览器中点击

# import webbrowser
# webbrowser.open('http://www.baidu.com')  # 打开一个网页，正常返回 True
# window_default = webbrowser.get()
# print(window_default.basename)
# print(window_default.name)
# print(window_default.args)


import requests

# 用 requests.get()函数下载一个网页
# res = requests.get('http://www.baidu.com')
# print(type(res))
# print(res.status_code, res.status_code == requests.codes.ok)
# print(len(res.text))
# print(res.text[:250])

# 检查错误
# res = requests.get('http://www.baidu.comm')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: %s' % exc)

# 将下载的文件保存到硬盘，必须用“写二进制”模式打开该文件
# res = requests.get('http://www.baidu.com')
# res.raise_for_status()
# playFile = open('data\\RomeoAndJuliet.html', 'wb')
# for chunk in res.iter_content(100000):  # 100000指定返回多少数据
#     playFile.write(chunk)
# playFile.close()

# 从 HTML 创建一个 BeautifulSoup 对象
# import bs4
# res = requests.get('http://www.baidu.com')
# res.raise_for_status()
# res.encoding = 'utf-8'
# noStarchSoup = bs4.BeautifulSoup(res.text, features="lxml")
# print(type(noStarchSoup))  # <class 'bs4.BeautifulSoup'>
# elems = noStarchSoup.select(".mnav")
# print(type(elems))  # <class 'bs4.element.ResultSet'>
# print(len(elems))
# print(type(elems[0]))  # <class 'bs4.element.Tag'>
# print(elems[0])
# print(elems[0].getText())
# print(elems[0].attrs)
# print(elems[0].get('class'))  # get获取属性值
