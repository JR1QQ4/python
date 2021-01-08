#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 4 条: 用辅助函数来取代复杂的表达式

# 开发者很容易过度运用 Python 的语法特性，从而写出那种特别复杂并且难以理解的单行表达式
# 把复杂的表达式移入辅助函数之中，如果要反复使用相同的逻辑，那就更应该这么做
# 使用 if/else 表达式，要比用 or 或 and 这样的 Boolean 操作符携程的表达式更加清晰

from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)
print(repr(my_values))  # {'red': ['5'], 'blue': ['0'], 'green': ['']}
print('Red: ', my_values.get('red'))  # ['5']
print('Green: ', my_values.get('green'))  # ['']
print('Opacity: ', my_values.get('opacity'))  # None

red = my_values.get('red', ['1'])
green = my_values.get('green', ['3'])
opacity = my_values.get('opacity', ['5'])
print('Red: ', my_values.get('red'))  # ['5']
print('Green: ', my_values.get('green'))  # ['']
print('Opacity: ', my_values.get('opacity'))  # None


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


green = get_first_int(my_values, 'green')
print(green)





