#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 20 条: 用 None 和文档字符串来描述具有动态默认值的参数

# 参数的默认值，只会在程序加载模块并督导本函数的定义时评估一次。对于 {} 或 [] 等动态的值，这可能会导致奇怪的行为
# 对于以动态值作为实际默认值的关键字参数来说，应该把形式上的默认值写为 None，并在函数的文档字符串里面描述该默认值所对应的实际行为

import json
from datetime import datetime
from time import sleep


def log(message, when=datetime.now()):
    print('%s: %s' % (when, message))


log('Hi there!')
sleep(0.1)
log('Hi again!')


def log1(message, when=None):
    """ Log a message with a timestamp.
    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    when = datetime.now() if when is None else when
    print('%s: %s' % (when, message))


log1('Hi there!')
sleep(0.1)
log1('Hi again!')


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['map'] = 1
print('Foo:', foo)  # Foo: {'stuff': 5, 'map': 1}
print('Bar:', bar)  # Bar: {'stuff': 5, 'map': 1}
assert foo is bar


def decode1(data, default=None):
    """ Load JSON data from a string
    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode1('bad data')
foo['stuff'] = 5
bar = decode1('also bad')
bar['meep'] = 1
print('Foo:', foo)  # Foo: {'stuff': 5}
print('Bar:', bar)  # Bar: {'meep': 1}










