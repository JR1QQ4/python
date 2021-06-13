#!/usr/bin/python
# -*- coding:utf-8 -*-
import re


class ReTest:
    @staticmethod
    def match_test():
        content = "Hello 123 4567 World_This is a Regex Demo"
        # match(pattern, string, flags=0)
        # 尝试从字符串的起始位置匹配
        res0 = re.match("World", content)
        print(res0)  # None
        res1 = re.match(r"^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$", content)
        print(res1)
        print(res1.group())
        print(res1.span())

        # 泛匹配
        res2 = re.match(r"Hello.*Demo", content)
        print(res2.group(0))
        print(res2.span())

        # 匹配目标
        res3 = re.match(r"^Hello\s(\d+).*Demo$", content)
        print(res3.group(1))  # 123

        # 贪婪匹配
        res4 = re.match(r"He.*(\d+).*Demo$", content)
        print(res4.group(1))  # 7

        # 非贪婪匹配
        res5 = re.match(r"He.*?(\d+).*Demo$", content)
        print(res5.group(1))  # 123

        # 匹配模式
        res6 = re.match(r"He.*?(\d+).*?Demo$", """Hello 1234567 World_This 
                                               is a Regex Demo""")
        print(res6)  # None
        res7 = re.match(r"He.*?(\d+).*?Demo$", """Hello 1234567 World_This 
                                                       is a Regex Demo""", re.S)
        print(res7)  # None

        # 转义
        res8 = re.match(r"price is $5.00", "price is $5.00")
        print(res8)  # None
        res9 = re.match(r"price is \$5\.00", "price is $5.00")
        print(res9)

    @staticmethod
    def search_test():
        content = "Extra strings Hello 1234567 World_This is a Regex Demo Extra strings"
        # search(pattern, string, flags=0)
        # 全文查找，不像match只会从第一个字符开始查找
        res0 = re.search("Hello", content)
        print(res0)

        html_test = """<div class="Aside-menu-block">
            <div class="Aside-menu-head">
                <a class="Aside-menu-whole" href="/directory?shortName=PCgame">全部+</a>
                <a class="Aside-menu-title" href="/directory/columnRoom/PCgame">网游竞技</a>
            </div>
            <div class="Aside-menu-list">
                <a class="Aside-menu-item is-active" href="/g_LOL" title="英雄联盟">英雄联盟</a>
                <a class="Aside-menu-item" href="/g_jdqs" title="绝地求生">绝地求生</a>
                <a class="Aside-menu-item" href="/g_How" title="炉石传说">炉石传说</a>
                <a class="Aside-menu-item" href="/g_Overwatch" title="守望先锋">守望先锋</a>
            </div>
        </div>
        """
        res1 = re.search("<div.*?is-active.*?title=\"(.*?)\">(.*?)</a>", html_test, re.S)
        print(res1.group())
        print(res1.group(1), res1.group(2))

    @staticmethod
    def findall_test():
        html_test = """<div class="Aside-menu-block">
                    <div class="Aside-menu-head">
                        <a class="Aside-menu-whole" href="/directory?shortName=PCgame">全部+</a>
                        <a class="Aside-menu-title" href="/directory/columnRoom/PCgame">网游竞技</a>
                    </div>
                    <div class="Aside-menu-list">
                        <a class="Aside-menu-item is-active" href="/g_LOL" title="英雄联盟">英雄联盟</a>
                        <a class="Aside-menu-item" href="/g_jdqs" title="绝地求生">绝地求生</a>
                        <a class="Aside-menu-item" href="/g_How" title="炉石传说">炉石传说</a>
                        <a class="Aside-menu-item" href="/g_Overwatch" title="守望先锋">守望先锋</a>
                    </div>
                </div>
                """
        res0 = re.findall("<a.*?title=\"(.*?)\">(.*?)</a>", html_test, re.S)
        print(res0, type(res0))  # <class 'list'>

    @staticmethod
    def sub_test():
        """替换字符串中每一个匹配的子串后返回替换后的字符串"""
        content = "Extra strings Hello 1234567 World_This is a Regex Demo Extra strings"
        # sub(pattern, repl, string, count=0, flags=0)
        res = re.sub(r"\d+", "", content)
        print(res)

        # \1表示将匹配到的字符串的第一个分组
        res1 = re.sub(r"(\d+)", r"\1abc", content)
        print(res1)

    @staticmethod
    def compile_test():
        """将正则字符串编译成正则表达式对象"""
        content = """Hello 1234567 World_This
        is a Regex Demo"""
        pattern = re.compile("Hello.*Demo", re.S)
        res1 = re.match(pattern=pattern, string=content)
        res2 = re.match("Hello.*Demo", content, re.S)
        print(res1)
        print(res2)



if __name__ == '__main__':
    # ReTest.match_test()

    # ReTest.search_test()

    # ReTest.findall_test()

    # ReTest.sub_test()

    ReTest.compile_test()