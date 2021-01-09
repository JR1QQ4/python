#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 14 条: 尽量用异常来表示特殊情况，而不要返回 None

# 用 None 这个返回值来表示特殊意义得函数，很容易使用调用者犯错，因为 None 和 0 及空字符串之类的值，在条件表达式里都会评估为 False
# 函数在遇到特殊情况时，应该抛出异常，而不要返回 None。调用者看到该函数的文档中所描述的异常之后，应该就会编写相应的代码来处理它们了


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


result = divide(0, 5)
if result is None:
    print('divide Invalid inputs, result: %s' % result)
if not result:
    print('divide Invalid inputs, not result: %s' % result)
result = divide(5, 0)
if result is None:
    print('divide Invalid inputs， None')
if not result:
    print('divide Invalid inputs')


def divide1(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None
success, result = divide1(5, 0)
if not success:
    print('divide1 Invalid inputs, success: %s' % success)
success, result = divide1(0, 5)
if not success:
    print('divide1 Invalid inputs, success: %s' % success)
_, result = divide1(0, 5)
if not result:
    print('divide1 Invalid inputs')


def divide2(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e
x, y = 5, 2
try:
    result = divide2(x, y)
except ValueError:
    print('divide2 Invalid inputs')
else:
    print('divide2 Result is %.1f' % result)
