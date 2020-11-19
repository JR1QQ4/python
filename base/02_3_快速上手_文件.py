#!/usr/bin/python
# -*- coding:utf-8 -*-

# 第二部分 自动化任务

print('********* 第 8 章 读写文件 ***********')

import os

print(os.path.join('usr', 'bin', 'spam'))
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

# 当前工作目录
print(os.getcwd())
# os.chdir('C:\\Windows\\System32')
# print(os.getcwd())

# 创建文件夹
# os.makedirs('.\\delicious\\walnut\\waffles')  # 当文件已存在时，无法创建该文件

# 绝对路径和相对路径
print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))
print(os.path.isabs('.'))  # False
print(os.path.isabs(os.path.abspath('.')))  # True
print(os.path.relpath('C:\\Windows', 'C:\\'))  # Windows
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))  # ..\..\Windows
print(os.getcwd())

path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))  # calc.exe
print(os.path.dirname(path))  # C:\Windows\System32

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(calcFilePath))  # ('C:\\Windows\\System32', 'calc.exe')
print(calcFilePath.split(os.path.sep))  # ['C:', 'Windows', 'System32', 'calc.exe']
print(os.path.sep)  # \\

# 文件的字节数和文件夹内容
print(os.path.getsize(os.getcwd()))  # 27648
print(os.listdir(os.getcwd()))

# totalSize = 0
# for filename in os.listdir('C:\\Windows\\System32'):
#     totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
# print(totalSize)

# 检查路径有效性
# print(os.path.exists('C:\\Windows'))
# print(os.path.exists('C:\\some_made_up_folder'))
# print(os.path.isdir('C:\\Windows\\System32'))
# print(os.path.isfile('C:\\Windows\\System32'))
# print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))
# print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))

# “纯文本文件” 只包含基本文本字符，不包含字体、大小和颜色信息
# “二进制文件” 是所有其他文件类型

# baconFile = open('data\\bacon.txt', 'w')
# baconFile.write('Hello world!\n')
# baconFile.close()
# baconFile = open('data\\bacon.txt', 'a')
# baconFile.write('Bacon is not a vegetable.')
# baconFile.close()
# baconFile = open('data\\bacon.txt')
# content = baconFile.read()
# baconFile.close()
# print(content)

# 用 shelve 模块保存变量，处理二进制文件
# import shelve
#
# shelfFile = shelve.open('data\\mydata')  # 在当前工作目录下有 3 个新文件，.bak .dat .dir
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()
#
# shelfFile = shelve.open('data\\mydata')
# print(type(shelfFile))  # <class 'shelve.DbfilenameShelf'>
# print(shelfFile['cats'])  # ['Zophie', 'Pooka', 'Simon']
# shelfFile.close()
#
# shelfFile = shelve.open('data\\mydata')
# print(list(shelfFile.keys()))  # ['cats']
# print(shelfFile.keys())  # KeysView(<shelve.DbfilenameShelf...
# print(list(shelfFile.values()))  # [['Zophie', 'Pooka', 'Simon']]
# print(shelfFile.values())  # ValuesView(<shelve.DbfilenameShelf...
# shelfFile.close()

# 用 pprint.pformat()函数保存变量
# import pprint
# cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# print(pprint.pformat(cats))
# fileObj = open('.\\data\\myCats.py', 'w')
# fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
# fileObj.close()
#
# import data.myCats as myCats
# print(myCats.cats[0])  # {'desc': 'chubby', 'name': 'Zophie'}

# import random
#
# capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
#             'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
#             'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
#             'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
#             'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
#             'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
#             'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
#             'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
#             'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
#             'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New '
#             'Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
#             'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
#             'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
#             'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
#             'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
#             'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West'
#             'Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# for quizNum in range(3):
#     # Create the quiz and answer key files.
#     quizFile = open('randomQuizGenerator\\capitalsquiz%s.txt' % (quizNum + 1), 'w')
#     answerKeyFile = open('randomQuizGenerator\\capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
#     # Write out the header for the quiz.
#     quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
#     quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
#     quizFile.write('\n\n')
#     # Shuffle the order of the states.
#     states = list(capitals.keys())
#     random.shuffle(states)
#     for questionNum in range(50):
#         # Get right and wrong answers.
#         correctAnswer = capitals[states[questionNum]]
#         wrongAnswers = list(capitals.values())
#         del wrongAnswers[wrongAnswers.index(correctAnswer)]
#         wrongAnswers = random.sample(wrongAnswers, 3)
#         answerOptions = wrongAnswers + [correctAnswer]
#         random.shuffle(answerOptions)
#         # Write the question and the answer options to the quiz file.
#         quizFile.write('%s. What is the capital of %s? [ ]\n' % (questionNum + 1, states[questionNum]))
#         for i in range(4):
#             quizFile.write('  %s. %s' % ('ABCD'[i], answerOptions[i]))
#             quizFile.write('\n')
#             # Write the answer key to a file.
#         quizFile.write('\n')
#         answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
#                 answerOptions.index(correctAnswer)]))
#     quizFile.close()
#     answerKeyFile.close()

# 复制文件和文件夹，会将源文件覆盖
# import shutil
# print(shutil.copy(os.path.join(os.getcwd(), 'programming.txt'), os.path.realpath(__file__)))
# print(shutil.copy('programming.txt', os.path.realpath(__file__)))

# 文件和文件夹的移动与改名，源文件消失
# import shutil
# print(shutil.move('programming.txt', 'programming.txt.bak'))
# print(shutil.move('programming.txt.bak', os.path.join(os.getcwd(), 'data')))

# 永久删除文件和文件夹
# for filename in os.listdir():
#     if filename.endswith('.rxt'):
#         # os.unlink(filename)
#         print(filename)

# shutil.rmtree()函数不可恢复地删除文件和文件
# 用 send2trash 模块安全地删除，可以在 回收站 里查看
# from send2trash import send2trash
# baconFile = open('bacon.txt', 'a')
# baconFile.write('Bacon is not a vegetable.')
# baconFile.close()
# send2trash('bacon.txt')

# os.walk()函数每次遍历返回：
# - 当前文件夹名称的字符串
# - 当前文件夹中子文件夹的字符串的列表
# - 当前文件夹中文件的字符串的列表
# for folderName, subfolders, filenames in os.walk(os.getcwd()):
#     print('The current folder is ' + folderName)
#     print(subfolders)
#     print(filenames)
#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': ' + filename)
#     print('')

# 读取 ZIP 文件
# import zipfile
# exampleZip = zipfile.ZipFile('example.zip')
# print(exampleZip.namelist())
# spamInfo = exampleZip.getinfo('spam.txt')
# print(spamInfo.file_size)
# print(spamInfo.compress_size)
# print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
#                                                  .compress_size, 2)))
# exampleZip.close()

# 从 ZIP 文件中解压缩
# import zipfile
# exampleZip = zipfile.ZipFile('example.zip')
# # exampleZip.extract('spam.txt')  # 解压单个文件
# exampleZip.extractall('example')  # 全部解压，可以指定解压路径，不存在就创建
# exampleZip.close()

# 创建和添加到 ZIP 文件
# import zipfile
# newZip = zipfile.ZipFile('new.zip', 'w')
# newZip.write('example\\spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()
# for folderName, subfolders, filenames in os.walk(os.getcwd()):
#     for subfolder in subfolders:
#         newZip.write(subfolder, compress_type=zipfile.ZIP_DEFLATED)
#     for filename in filenames:
#         newZip.write(filename, compress_type=zipfile.ZIP_DEFLATED)

# def fileToZip():
#     import zipfile
#     newZip = zipfile.ZipFile('new.zip', 'w')
#     def writeToZip(file_path):
#         for folder_file in os.listdir(file_path):
#             folder_file_path = os.path.join(os.getcwd(), file_path, folder_file)
#             current_file_path = file_path + '\\' + folder_file
#             if os.path.isfile(folder_file_path):
#                 newZip.write(current_file_path, compress_type=zipfile.ZIP_DEFLATED)
#             elif os.path.isdir(folder_file_path):
#                 newZip.write(current_file_path, compress_type=zipfile.ZIP_DEFLATED)
#                 writeToZip(current_file_path)
#         if len(os.listdir(file_path)) == 0:
#             return
#     writeToZip('example')
#     newZip.close()
# fileToZip()
