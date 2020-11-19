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

# 需要把对应浏览器驱动放到 python\\script 目录下，geckodriver.exe
# from selenium import webdriver
# firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
# browser = webdriver.Firefox()
# print(type(browser))
# browser.get('https://www.baidu.com')

# 使用 CSS 类 name 的元素：
#     browser.find_element_by_class_name(name)
#     browser.find_elements_by_class_name(name)
# 匹配 CSS selector 的元素：
#     browser.find_element_by_css_selector(selector)
#     browser.find_elements_by_css_selector(selector)
# 匹配 id 属性值的元素：
#     browser.find_element_by_id(id)
#     browser.find_elements_by_id(id)
# 完全匹配提供的 text 的<a>元素：
#     browser.find_element_by_link_text(text)
#     browser.find_elements_by_link_text(text)
# 包含提供的 text 的<a>元素：
#     browser.find_element_by_partial_link_text(text)
#     browser.find_elements_by_partial_link_text(text)
# 匹配 name 属性值的元素：
#     browser.find_element_by_name(name)
#     browser.find_elements_by_name(name)
# 匹配标签 name 的元素(大小写无关， <a>元素匹配'a'和'A')：
#     browser.find_element_by_tag_name(name)
#     browser.find_elements_by_tag_name(name)

# tag_name             标签名，例如 'a'表示<a>元素
# get_attribute(name)  该元素 name 属性的值
# text                 该元素内的文本，例如<span>hello</span>中的'hello'
# clear()              对于文本字段或文本区域元素，清除其中输入的文本
# is_displayed()       如果该元素可见，返回 True，否则返回 False
# is_enabled()         对于输入元素，如果该元素启用，返回 True，否则返回 False
# is_selected()        对于复选框或单选框元素，如果该元素被选中，选择 True，否则返回 False
# location             一个字典，包含键'x'和'y'，表示该元素在页面上的位置

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://www.bilibili.com/')
# try:
#     elem = browser.find_element_by_class_name('sortable')
#     print('Found <%s> element with that class name!' % elem.tag_name)
#     print(type(elem))
#     elem.click()
#     search_elem = browser.find_element_by_class_name('nav-search-keyword')
#     search_elem.send_keys('原神')
#     btn_elem = browser.find_element_by_class_name('nav-search-submit')
#     btn_elem.click()
# except:
#     print('Was not able to find an element with that name.')

# selenium.webdriver.common.keys 模块中常用的变量:
# Keys.DOWN, Keys.UP, Keys.LEFT,Keys.RIGHT      键盘箭头键
# Keys.ENTER, Keys.RETURN                       回车和换行键
# Keys.HOME, Keys.END,
# Keys.PAGE_DOWN,Keys.PAGE_UP                   Home键,End键,PageUp键和Page Down键
# Keys.ESCAPE, Keys.BACK_SPACE,Keys.DELETE Esc  Backspace和字母键
# Keys.F1, Keys.F2, . . . , Keys.F12            键盘顶部的 F1到 F12键
# Keys.TAB                                      Tab 键

# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# browser = webdriver.Firefox()
# browser.get('https://www.acfun.cn/')
# time.sleep(3)
# htmlElem = browser.find_element_by_tag_name('html')
# htmlElem.send_keys(Keys.END)  # scrolls to bottom
# htmlElem.send_keys(Keys.HOME)  # scrolls to top

# 点击浏览器按钮:
# browser.back()      点击“返回”按钮
# browser.forward()   点击“前进”按钮
# browser.refresh()   点击“刷新”按钮
# browser.quit()      点击“关闭窗口”按钮







