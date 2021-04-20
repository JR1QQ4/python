#!/usr/bin/python
# -*- coding:utf-8 -*-

# 1.*args 和 **kwargs
def use_args(*args, a=1): pass
def user_kwargs(b=1, **kwargs): pass

# 2.继承
class A:
    def __init__(self, a):
        pass
class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)

# 3.unittest 可通过类名、模块名、目录三种方式去收集用例
# class TestU:
#     # 方法一：目录（常用）
#     import unittest
#     suite = unittest.TestLoader().discover('搜索目录')  # 默认在 test*.py 中搜索用例
#     # 方法二：类名（了解）
#     suite = unittest.TestLoader().loadTestsFromTestCase('测试类名')  # 测试类名不需要加引号
#     # 方法三：模块名（了解）
#     suite = unittest.TestLoader().loadTestsFromModule('模块名')  # 模块名不需要加引号（注意导入模块）
#     # 执行 suite 的三种方式
#     # 方法一： TextTestRunner，生成 txt 文件
#     with open("test_result.txt", "w") as fs:
#         runner = unittest.TextTestRunner(fs)
#         runner.run(suite)
    # 方法二： HtmlTestRunner，生成 html 文件
    # from HtmlTestRunnerNew import HTMLTestRunner
    # with open("report.html", "wb") as fs:
    #     runner = HTMLTestRunner(fs, title="title", tester="name")
    #     runner.run(suite)
    # 方法三： BeautifulReport
    # from BeautifulReport import BeautifulReport
    # result = BeautifulReport(suite)
    # #  log_path: 生成report的文件存储路径; filename: 生成文件的filename; description: 生成文件的注释
    # result.report(filename='测试报告', description='测试deafult报告', log_path='report')

# 4.ddt
# import ddt
# @ddt
# class C:
#     datas = [{},{},{}]
#     @ddt.data(*datas)
#     def test_login(self, case):
#         pass

# 5.excel
class HandleExcel:
    def __init__(self, file_path, sheet_name):
        from openpyxl import load_workbook
        from openpyxl.workbook import workbook
        from openpyxl.worksheet import worksheet
        self.wb: workbook = load_workbook(file_path)
        self.sh: worksheet = self.wb[sheet_name]
    def __read_titles(self):
        titles = []
        for item in list(self.sh.rows)[0]:
            titles.append(item.value)
        return titles
    def read_all_data(self):
        all_data = []
        titles = self.__read_titles()
        for item in list(self.sh.rows)[1:]:
            values = []
            for val in item:
                values.append(val.value)
            res = dict(zip(titles, values))
            all_data.append(res)
        return all_data
    def close_file(self):
        self.wb.close()
# if __name__ == '__main__':
#     import os
#     file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases.xlsx")
#     exc = HandleExcel(file_path, "login")
#     cases = exc.read_all_data()
#     exc.close_file()
#     for case in cases:
#         print(case)

# titles = ["id", "desc"]
# data = ["1", "登录成功"]
# r = dict(zip(titles, data))
# print(r)

# 6.log
import logging
class MyLogger(logging.Logger):
    def __init__(self, name, level=logging.INFO, file=None):
        # 设置输出级别、输出渠道、输出日志格式
        super(MyLogger, self).__init__(name, level)

        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line: %(message)s'
        formatter = logging.Formatter(fmt)

        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)
# if __name__ == '__main__':
#     from configparser import ConfigParser
#     conf = ConfigParser()
#     conf.read("my_logger.ini", "utf-8")
#     if bool(conf.getboolean("log", "is_load")):
#         file_name = conf.get("log", "file_name")
#     else:
#         file_name = None
#     logger = MyLogger(conf.get("log", "name"), conf.get("log", "level"), file_name)
#     logger.info("测试！！！")

# 7.config_parse
from configparser import ConfigParser
import time
conf = ConfigParser()
result = conf.read("my_logger.ini", "utf-8")
val = conf.get("log", "name")
b1 = conf.get("log", "is_load")
b2 = conf.getboolean("log", "is_load")
sections = conf.sections()
options = conf.options(sections[0])
items = conf.items(sections[0])
# 修改，写入
conf.set(sections[0], options[0], str(time.time()))
conf.write(open("my_logger.ini", "w", encoding="utf-8"))
new_sections = conf.sections()
# print(result)
# print(val, type(val))
# print(b1, type(val))
# print(b2, type(val))
# print(sections)
# print(options)
# print(items)
# print(new_sections)

# 8.json
import json
a_json = '{"a":"111", "b":"222", "c": ["d", "e", "f"]}'
json_to_obj = json.loads(a_json, encoding='utf-8')
obj_to_json = json.dumps(json_to_obj)
# print(json_to_obj)
# print(obj_to_json)

# 9.eval
# o = eval('{"a":"111", "b":"222", "c": ["d", "e", "f"]}')
# print(o)
# str1 = "[{11,22},{22,33},{33,44},{44,55}]"
# print(type(str1))
# list1 = eval(str1)
# print(type(list1))
# x = '7'
# print(type(x))
# a = eval(x)
# print(type(a))

# 10.MySQL
# import pymysql
# conn = pymysql.connect(
#     user=None,
#     password="",
#     host=None,
#     database=None,
#     unix_socket=None,
#     port=0,
#     charset="utf8",
#     cursorclass=pymysql.cursors.DictCursor  # 返回字典类型的值
# )
# cursor = conn.cursor()
# sql1 = ''
# count = cursor.execute(sql1)
# one = cursor.fetchone()
# two = cursor.fetchone()
# all = cursor.fetchall()
# cursor.close()
# conn.close()

# 11.json_path
import jsonpath
import json
a_json = {"a":"111", "b":"222", "c": ["d", "e", "f"]}
a_str = '{"a":"111", "b":"${username}", "c": ["d", "e", "f"]}'
res = jsonpath.jsonpath(a_json, "$.c[1]")
res1 = jsonpath.jsonpath(json.loads(a_str), "$..*")
# print(res)
print(res1)

