#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from unittestreport import TestRunner

# 用于执行多个测试集
# 第一步：创建测试套件，加载测试用例套件

# # 1.创建套件
# suite = unittest.TestSuite()
# # 2.创建一个用例加载器
# loader = unittest.TestLoader()
# # 3.加载测试用例套件
# suite.addTest(loader.discover(r'C:\ZZZZZZ\python\base\homework'))
# print(suite)

# 上面三行代码的一种简写形式
suite = unittest.defaultTestLoader.discover(r'C:\ZZZZZZ\python\base\homework')

# 第二步：创建一个测试用例运行程序
# runner = unittest.TextTestRunner()
# 使用unittest report代替
runner = TestRunner(suite)

# 第三步：运行测试用例
# runner.run(suite)
# 使用unittest report的区别
runner.run()

# unittest 的执行顺序
# 1.同一个【用例类】中是根据用例【方法名】按照 ASCII 码进行排序
# 2.同一个【用例文件】中的测试类型是根据【类名】按照 ASCII 码进行排序
# 3.同一个【文件夹】中的测试用例文件是根据【文件名】按照 ASCII 码进行排序

