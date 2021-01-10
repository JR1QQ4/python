#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 41 条: 考虑用 concurrent.futures 来实现真正的平行计算

# 把引发 CPU 性能瓶颈的那部分代码，用 C 语言扩展模块来改写，即可在尽量发挥 Python 特性的前提下，有效提升程序的执行速度。
#   但是，这样做的工作量比较大，而且可能会引入 bug
# multiprocessing 模块提供了一些强大的工具。对于某些类型的任务来说，开发者只需编写少量代码，即可实现平行计算
# 若想利用强大的 multiprocessing 模块，最恰当的做法，就是通过内置的 concurrent.futures 模块及其 ProcessPoolExecutor 类来使用它
# multiprocessing 模块所提供的那些高级功能，都特别复杂，所以开发者尽量不要直接使用它们








