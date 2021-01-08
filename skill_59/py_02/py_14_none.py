#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 14 条: 尽量用异常来表示特殊情况，而不要返回 None

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

result = dici   
