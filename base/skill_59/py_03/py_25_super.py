#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 25 条: 用 super 初始化父类

# Python 采用标准地方法解析顺序来解决超类初始化次序及钻石继承问题
# 总是应该使用内置的 super 函数来初始化父类


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)


class TimesTwo(object):
    def __init__(self):
        self.value *= 2


class PlusFive(object):
    def __init__(self):
        self.value += 5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


foo = OneWay(5)
print('First ordering is (5 * 2) + 5 =', foo.value)  # First ordering is (5 * 2) + 5 = 15


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


bar = AnotherWay(5)
print('Second ordering still is', bar.value)  # Second ordering still is 15

print('--------------------------------------')


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2


class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)


foo = ThisWay(5)
print('Should be (5 * 5) + 2 = 27 but is', foo.value)  # 7

print('===========================================')


class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


foo = GoodWay(5)
print('Should be 5 * (5 + 2) = 35 and is', foo.value)  # 35

from pprint import pprint
pprint(GoodWay.mro())
# [<class '__main__.GoodWay'>,
#  <class '__main__.TimesFiveCorrect'>,
#  <class '__main__.PlusTwoCorrect'>,
#  <class '__main__.MyBaseClass'>,
#  <class 'object'>]

print('++++++++++++++++++++++++++++++++++')


class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)


class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)























