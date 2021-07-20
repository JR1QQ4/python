#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 59 条: 用 tracemalloc 来掌握内存地使用及泄露情况

# Python 程序的内存使用情况和内存泄露情况时很难判断的
# 我们虽然可以通过 gc 模块来了解程序中的对象，但是并不能由此看出这些对象究竟时如何分配出来的
# 内置的 tracemalloc 模块提供了许多强大的工具，使得我们可以找出导致内存使用量增大的根源
# 只有 Python 3.4 及后续版本，才支持 tracemalloc 模块














