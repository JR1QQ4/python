#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 35 条: 用元类来注解类的属性

# 借助元类，我们可以在某个类完全定义好之前，率先修改该类的属性
# 描述符与元类能够有效地组合起来，以便对某种行为作出修饰，或在程序进行时探查相关信息
# 如果把元类与描述符相结合，那就可以在不使用 weakref 模块的前提下避免内存泄露


class Field(object):
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Customer(object):
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')


foo = Customer()
print('Before:', repr(foo.first_name), foo.__dict__)  # Before: '' {}
foo.first_name = 'Euclid'
print('After:', repr(foo.first_name), foo.__dict__)  # After: 'Euclid' {'_first_name': 'Euclid'}


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


class DatabaseRow(object, metaclass=Meta):
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name


class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()


foo = BetterCustomer()
print('Before:', repr(foo.first_name), foo.__dict__)
foo.first_name = 'Euler'
print('After:', repr(foo.first_name), foo.__dict__)







