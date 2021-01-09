#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 21 条: 用只能以关键字形式指定的参数来确保代码明晰

# 关键字参数能够使函数调用的意图更加明确
# 对于各参数之间很容易混淆的函数，可以声明只能以关键字形式指定的参数，以确保调用者必须关键字来指定它们
#   对于接受多个 Boolean 标志的函数，更应该这样做
# 在编写函数时，Python3 有明确的语法来定义这种只能以关键字形式指定的参数
# Python2 的函数可以接受 **kwargs 参数，并手工抛出 TypeError 异常，以便模拟只能以关键字形式来指定的参数


def safe_division(number, divisor,
                  ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


result = safe_division(1.0, 10**500, True, False)
print(result)  # 0,  float 溢出

result = safe_division(1, 0, False, True)
print(result)  # inf,  返回无穷


def safe_division_b(number, divisor,
                  ignore_overflow=False,
                  ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


print(safe_division_b(1, 10**500, ignore_overflow=True))  # 0.0
print(safe_division_b(1, 0, ignore_zero_division=True))  # inf

print(safe_division_b(1, 10**500, True, False))  # 0.0


# 推荐
def safe_division_c(number, divisor, *,
                  ignore_overflow=False,
                  ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# print(safe_division_c(1, 10**500, True, False))  # TypeError: safe_division_c() takes 2 positional arguments...
print(safe_division_c(1, 0, ignore_zero_division=True))  # inf

print('*' * 50)


# Python 2
def safe_division_d(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_division = kwargs.pop('ignore_zero_division', False)
    print(kwargs)
    if kwargs:
        raise TypeError('Unexpected **kwargs: %r' % kwargs)
    pass


safe_division_d(1, 10)
safe_division_d(1, 10, ignore_zero_division=True)
safe_division_d(1, 10**500, ignore_overflow=True)

# safe_division_d(1, 0, False, True)

safe_division_d(0, 0, unexpected=True)















