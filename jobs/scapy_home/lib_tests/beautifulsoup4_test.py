#!/usr/bin/python
# -*- coding:utf-8 -*-
# pip install beautifulsoup4
from bs4 import BeautifulSoup


class Bs4Test:
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """
    soup = BeautifulSoup(html_doc, 'lxml')

    @classmethod
    def test1(cls):
        print(cls.soup.prettify())  # 格式化代码，容错处理
        print(cls.soup.title.string)  # The Dormouse's story

    @classmethod
    def test2(cls):
        """选择元素"""
        print(cls.soup.title)  # <title>The Dormouse's story</title>
        print(type(cls.soup.title))  # <class 'bs4.element.Tag'>
        print(cls.soup.head)  # <head><title>The Dormouse's story</title></head>
        print(cls.soup.p)  # <p class="title"><b>The Dormouse's story</b></p>

        # 获取名称
        print(cls.soup.name)  # [document]

        # 获取属性
        print(cls.soup.p.attrs['class'])
        print(cls.soup.p['class'])

        # 获取内容
        print(cls.soup.p.string)  # The Dormouse's story

        # 嵌套选择
        print(cls.soup.head.title.string)

        # 子节点和子孙节点
        print(cls.soup.p.contents)  # [<b>The Dormouse's story</b>]
        print(cls.soup.p.children)  # <list_iterator object at 0x0000023233C3DF48>
        for i, child in enumerate(cls.soup.p.children):
            print(i, child)  # 0 <b>The Dormouse's story</b>

    @classmethod
    def test3(cls):
        # find_all(name, attrs, recursive, text, **kwargs)
        # 标签选择器
        # print(cls.soup.find_all("p"))
        # print(type(cls.soup.find_all("p")))  # <class 'bs4.element.ResultSet'>
        for p in cls.soup.find_all("p"):
            print(p)

        # 属性选择，传入字典形式
        print(cls.soup.find_all(attrs={"class": "title"}))

        print(cls.soup.find_parents())
        print(cls.soup.find_parent())
        print(cls.soup.find_next_siblings())
        print(cls.soup.find_next_sibling())
        print(cls.soup.find_previous_siblings())
        print(cls.soup.find_previous_sibling())
        print(cls.soup.find_previous_siblings())

        # CSS选择器
        print(cls.soup.select('p.story'))


if __name__ == '__main__':
    # Bs4Test.test1()

    # Bs4Test.test2()

    Bs4Test.test3()
