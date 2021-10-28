#!/usr/bin/python
# -*- coding:utf-8 -*-
import openpyxl
from openpyxl.workbook.workbook import Worksheet

# 方法一
# # 1.加载 excel 文件为工作簿对象
# wb = openpyxl.load_workbook('')
# # 获取所有的表单名
# # print(wb.sheetnames)
# # 2.选中表单
# sh: Worksheet = wb['Sheet1']
# # 3.读取数据
# cl = sh.cell(row=1, column=1)
# print(cl.value)

# 方法二
wb = openpyxl.load_workbook('')
sh: Worksheet = wb['Sheet1']
# rows：按行获取表单中所有的格子，每一行的格子放到一个元组中
rows = list(sh.rows)
for i in rows:
    print(i)
# columns：按列获取表单中所有的格子，每一列的格子放到一个元组中
columns = list(sh.columns)
for j in columns:
    print(j)
# 获取所有数据
title = [row.value for row in rows[0]]
cases = []
for item in rows[1:]:
    data = [i.value for i in item]
    temp = dict(zip(title, data))
    cases.append(temp)
print(cases)


休息。。。
