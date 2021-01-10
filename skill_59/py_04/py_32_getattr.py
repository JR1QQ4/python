#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 32 条: 用 __getattr__、__getattribute__ 和 __setattr__ 实现按需生成的属性

# 通过 __getattr__ 和 __setattr__，我们可以用惰性的方式来加载并保存对象的属性
# 要理解 __getattr__ 与 __getattribute__ 的区别: 前者只会在待访问的属性缺失时触发，而后者则会在每次访问属性时触发
# 如果要在 __getattribute__ 和 __setattr__ 方法中访问实例属性，那么应该直接通过 super()
#   （也就是 object 类的同名方法）来做，以避免无限递归


class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value


data = LazyDB()
print('Before:', data.__dict__)  # Before: {'exists': 5}
print('foo:', data.foo)  # foo: Value for foo
print('After:', data.__dict__)  # After: {'exists': 5, 'foo': 'Value for foo'}


class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)


data = LoggingLazyDB()
print('exists:', data.exists)  # exists: 5，不会触发 getattr
print('foo:', data.foo)  # foo: Value for foo，触发 getattr
print('foo:', data.foo)  # foo: Value for foo

print('*' * 50)


class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value


data = ValidatingDB()
print('exists:', data.exists)  # exists: 5，会调用 getattribute
print('foo:', data.foo)  # foo: Value for foo，会调用 getattribute
print('foo:', data.foo)  # foo: Value for foo，会调用 getattribute

print('*' * 50)


class BrokenDictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, item):
        print('Called __getattribute__(%s)' % item)
        # return self._data[item]  # RecursionErro，无限递归调用

        data_dict = super().__getattribute__('_data')
        return data_dict[item]


data = BrokenDictionaryDB({'foo': 3})
data.foo
