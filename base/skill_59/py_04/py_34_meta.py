#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 34 条: 用元类来注册子类

# 在构建模块化的 Python 程序时，类的注册是一种很有用的模式
# 开发者每次从基类中继承子类时，基类的元类都可以自动运行注册代码
# 通过元类来实现类的注册，可以确保所有子类都不会遗漏，从而避免后续的错误
import json


class Serializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args})


class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point2D(%d, %d)' % (self.x, self.y)


point = Point2D(5, 3)
print('Object:    ', point)  # Object:     Point2D(5, 3)
print('Serialized:', point.serialize())  # Serialized: {"args": [5, 3]}


class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])


class BetterPoint2D(Deserializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point2D(%d, %d)' % (self.x, self.y)


point = BetterPoint2D(5, 3)
print('Before:', point)  # Before: Point2D(5, 3)
data = point.serialize()
print('Serialized:', data)  # Serialized: {"args": [5, 3]}
after = BetterPoint2D.deserialize(data)
print('After:', after)  # After: Point2D(5, 3)













