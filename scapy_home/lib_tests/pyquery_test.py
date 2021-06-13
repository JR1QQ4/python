#!/usr/bin/python
# -*- coding:utf-8 -*-
# pip install pyquery
from pyquery import PyQuery as pq


class PyQueryTest:
    @staticmethod
    def test1():
        """字符串初始化"""
        html = """
            <div>
                <ul>
                    <li class="item-0">li-1</li>
                    <li class="item-1"><a href="link1.html">li-2</a></li>
                    <li class="item-0 active"><a href="link2.html"><span>li-3</span></a></li>
                    <li class="item-1 active"><a href="link3.html">li-4</a></li>
                    <li class="item-0"><a href="link3.html">li-5</a></li>
                </ul>
            </div>
        """
        doc = pq(html)
        print(doc('li'))

    @staticmethod
    def test2():
        """URL初始化"""
        doc = pq(url="http://www.baidu.com")
        print(doc('head'))

    @staticmethod
    def test3():
        """文件初始化"""
        doc = pq(filename="demo.html")
        print(doc('li'))

    @staticmethod
    def test4():
        """基本选择器"""
        html = """
<div id="container">
<ul class="list-items">
<li class="item-0">li-1</li>
<li class="item-1"><a href="link1.html">li-2</a></li>
<li class="item-0 active"><a href="link2.html"><span>li-3</span></a></li>
<li class="item-1 active"><a href="link3.html">li-4</a></li>
<li class="item-0"><a href="link3.html">li-5</a></li>
</ul>
</div>
        """
        doc = pq(html)
        print(doc("#container .list-items li.active"))
        print("*" * 50)

        # 查找元素
        print(type(doc(".list-items")))  # <class 'pyquery.pyquery.PyQuery'>
        print(doc(".list-items"))
        print("*" * 50)

        lis = doc(".list-items").find("li")
        print(type(lis))  # <class 'pyquery.pyquery.PyQuery'>
        print(lis)
        print("*" * 50)

        lis = doc(".list-items").children()
        print(type(lis))  # <class 'pyquery.pyquery.PyQuery'>
        print(lis)
        print("*" * 50)

        lis = doc(".list-items").children(".active")
        print(type(lis))  # <class 'pyquery.pyquery.PyQuery'>
        print(lis)
        print("*" * 50)

        container = doc(".list-items").parent()
        print(type(container))  # <class 'pyquery.pyquery.PyQuery'>
        print(container)
        print("*" * 50)

        container = doc(".list-items").parents()
        print(type(container))  # <class 'pyquery.pyquery.PyQuery'>
        print(container)
        print("*" * 50)

        li = doc(".list-items .item-0.active")
        print(li)
        print(li.siblings())
        print(li.siblings(".active"))
        print("*" * 50)

        # 遍历
        for li in doc("li").items():
            print(li)

        print("*" * 50)
        li = doc("li:first-child")
        print(li)
        li = doc("li:last-child")
        print(li)
        li = doc("li:nth-child(2)")
        print(li)
        li = doc("li:gt(2)")
        print(li)
        li = doc("li:contains(li-2)")
        print(li)

    @staticmethod
    def test5():
        """属性操作"""
        html = """
<div id="container">
<ul class="list-items">
<li class="item-0">li-1</li>
<li class="item-1"><a href="link1.html">li-2</a></li>
<li class="item-0 active"><a href="link2.html"><span>li-3</span></a></li>
<li class="item-1 active"><a href="link3.html">li-4</a></li>
<li class="item-0"><a href="link3.html">li-5</a></li>
</ul>
</div>
"""
        doc = pq(html)
        a = doc(".item-0.active a")
        print(a)
        print(a.attr('href'))
        print(a.attr.href)
        print(a.text())
        print(a.html())

    @staticmethod
    def test6():
        """DOM操作"""
        html = """
<div id="container">
<ul class="list-items">
<li class="item-0">li-1</li>
<li class="item-1"><a href="link1.html">li-2</a></li>
<li class="item-0 active"><a href="link2.html"><span>li-3</span></a></li>
<li class="item-1 active"><a href="link3.html">li-4</a></li>
<li class="item-0"><a href="link3.html">li-5</a></li>
</ul>
</div>
"""
        doc = pq(html)
        li = doc(".item-0.active")
        print(li)
        li.remove_class("active")
        print(li)
        li.add_class("active")
        print(li)

        li.attr("name", "link")
        print(li)
        li.css("font-size", "14px")
        print(li)
        print("*" * 50)

        html1 = """
        <div class="wrap">
            Hello World
            <p>This is a paragraph</p>
        </div>
        """
        doc1 = pq(html1)
        wrap = doc1(".wrap")
        print(wrap.text())
        wrap.find("p").remove()
        print(wrap)
        print(wrap.text())


if __name__ == '__main__':
    # PyQueryTest.test1()
    # PyQueryTest.test2()

    PyQueryTest.test4()

    # PyQueryTest.test5()

    # PyQueryTest.test6()
