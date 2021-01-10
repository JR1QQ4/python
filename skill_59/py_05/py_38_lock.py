#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 38 条: 在线程中使用 Lock 来防止数据竞争

# Python 确实有全局解释器锁，但是在编写自己地程序时，依然要设法防止多个线程争用同一份数据
# 如果在不加锁地前提下，允许多条线程修改同一个对象，那么程序地数据结构可能会遭到破坏
# 在 Python 内置地 threading 模块中，有个名叫 Lock 的类，它用标准的方式实现了互斥锁









