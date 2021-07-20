#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第二部分 自动化任务

print('********* 第 14 章 处理 CSV 文件和 JSON 数据 ***********')

import csv

# 读取数据
# exampleFile = open('data\\example.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# # print(exampleData)
# # print(exampleReader)
# for row in exampleData:
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

# 写入数据
# outputFile = open('data\\output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# print(outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']))  # 21
# print(outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham']))  # 32
# print(outputWriter.writerow([1, 2, 3.141592, 4]))  # 16
# outputFile.close()

import json

# 用 loads() 函数读取 JSON
# stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
# jsonDataAsPythonValue = json.loads(stringOfJsonData)
# print(jsonDataAsPythonValue)

# 用 dumps 函数写出 JSON
# pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
# stringOfJsonData = json.dumps(pythonValue)
# print(stringOfJsonData)


# for excelFile in os.listdir('.'):
#     # Skip non-xlsx files, load the workbook object.
#     for sheetName in wb.get_sheet_names():
#         # Loop through every sheet in the workbook.
#         sheet = wb.get_sheet_by_name(sheetName)
#         # Create the CSV filename from the Excel filename and sheet title.
#         # Create the csv.writer object for this CSV file.
#         # Loop through every row in the sheet.
#         for rowNum in range(1, sheet.get_highest_row() + 1):
#                 rowData = [] # append each cell to this list
#                 # Loop through each cell in the row.
#                 for colNum in range(1, sheet.get_highest_column() + 1):
#                 # Append each cell's data to rowData.
#         # Write the rowData list to the CSV file.
#         csvFile.close()




