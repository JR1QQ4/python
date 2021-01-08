#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 13 条: 合理利用 try/except/else/finally 结构中的每个代码块

# 无论 try 块是否发生异常，都可利用 try/finally 复合语句中的 finally 块来执行清理工作
# else 块可以用来缩减 try 块中的代码量，并把没有发生异常时所要执行的语句与 try/except 代码块隔开
# 顺利运行 try 块后，若想使某些操作能在 finally 块的清理代码之前执行，则可将这些操作写到 else 块中

handle = open('./random_data.txt')
try:
    data = handle.read()
finally:
    handle.close()

import json
def load_json(data, key):
    try:
        result_dict = json.loads(data)
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]


UNDEFINED = object()
def divide_json(path):
    handle = open(path, 'r+')
    try:
        data = handle.read()
        op = json.loads(data)
        value = (
                op['numerator'] /
                op['denominator']
        )
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return value
    finally:
        handle.close()




