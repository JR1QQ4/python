#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 43 条: 考虑以 contextlib 和 with 语句来改写可复用的 try/finally 代码

# 可以用 with 语句来改写 try/finally 块中的逻辑，以便提升复用程度，并使代码更加整洁
# 内置的 contextlib 模块提供了名叫 contextmanager 的修饰器，开发者只需用它来修饰自己的函数，即可令该函数支持 with 语句
# 情境管理器可以通过 yield 语句向 with 语句返回一个值，此值会赋给 as 关键字所指定的变量。该机制阐明了这个特殊情境的编写冬季，
#   并令 with 块中的语句能够直接访问这个目标变量








