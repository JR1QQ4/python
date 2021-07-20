#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 33 条: 用元类来验证子类

# 通过元类，我们可以在生成子类对象之前，先验证子类的定义是否合乎规范
# Python2 和 Python3 指定元类的语法略有不同
# Python 系统把子类的整个 class 语句体处理完毕之后，就会调用其元类的 __new__ 方法


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)


class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


print('Before class')


class Line(Polygon):
    print('Before sides')
    sides = 1
    print('After sides')


print('After class')






















