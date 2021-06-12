#!/usr/bin/python
# -*- coding:utf-8 -*-
import re


class ReTest:
    @staticmethod
    def match_test():
        content = "Hello 123 4567 World_This is a Regex Demo"
        rule = "4567"
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


if __name__ == '__main__':
    ReTest.match_test()
