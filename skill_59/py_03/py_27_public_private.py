#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 27 条: 多用 public 属性，少用 private 属性

# Python 编辑器无法严格保证 private 字段的私密性
# 不要盲目地将属性设为 private，而是应该从一开始就做好规划，并允许子类更多地访问超类地内部 API
# 应该多用 protected 属性，并在文档中把这些字段地合理用法告诉子类的开发者，而不要试图用 private 属性来限制子类访问这些字段
# 只要当子类不受自己控制时，才可以考虑用 private 属性来避免名称冲突


class MyObject(object):
    def __init__(self):
        self.public_filed = 5
        self.__private_filed = 10

    def get_private_filed(self):
        return self.__private_filed


foo = MyObject()
assert foo.public_filed == 5
# foo.__private_filed  # AttributeError: 'MyObject' object has no attribute '__private_filed'


class MyOtherObject(object):
    def __init__(self):
        self.__private_field = 71

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field


bar = MyOtherObject()
assert MyOtherObject.get_private_field_of_instance(bar) == 71


class MyParentObject(object):
    def __init__(self):
        self.__private_field = 71


class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field


baz = MyChildObject()
# baz.get_private_field()  # AttributeError: 'MyChildObject' object has no attribute

assert baz._MyParentObject__private_field == 71
print(baz.__dict__)  # {'_MyOtherObject__private_field': 71}


# class MyBaseClass(object):
#     def __init__(self, value):
#         self.__value = value


class MyClass(object):
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return str(self.__value)


foo = MyClass(5)
assert foo.get_value() == '5'


class MyIntegerSubclass(MyClass):
    def get_value(self):
        return int(self._MyClass__value)


foo = MyIntegerSubclass(5)
assert foo.get_value() == 5


class ApiClass(object):
    def __init__(self):
        self.__value = 5

    def get(self):
        return self.__value


class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'


a = Child()
print(a.get(), 'and', a._value, 'should be different')




































