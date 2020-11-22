#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第二部分 自动化任务

print('********* 第 15 章 保持时间、计划任务和启动程序 ***********')

import time

# time 模块用于取得 Unix 纪元时间戳，并加以处理
# print(time.time())  # 1970年1月1日0点(UTC) 以来的秒数
# print(time.ctime())  # Sun Nov 22 13:29:39 2020

# def calcProd():
#     product = 1
#     for i in range(1, 100000):
#         product *= i
#     return product
# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('The result is %s digits long.' % len(str(prod)))
# print('Took %s seconds to calculate.' % (endTime - startTime))

# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)

# now = time.time()
# print(now)  # 1606023550.345779
# print(round(now, 2))  # 1606023600.21
# print(round(now, 4))  # 1606023600.2078
# print(round(now))  # 1606023621

# 超级秒表
# print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. '
#       'Press "Ctrl-C to quit."')
# input()
# print('Started.')
# startTime = time.time()
# lastTime = startTime
# lapNum = 1
# try:
#     while True:
#         input()
#         lapTime = round(time.time() - lastTime, 2)
#         totalTime = round(time.time() - startTime, 2)
#         print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
#         lapNum += 1
#         lastTime = time.time()
# except KeyboardInterrupt:
#     print('\nDone.')

import datetime

# 以更方便的格式显示日期，或对日期进行算术运算
# print(datetime.datetime.now())
# dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
# print(dt.year, dt.month, dt.day)
# print(dt.hour, dt.minute, dt.second)
# print(datetime.datetime.fromtimestamp(1000000))  # 1970-01-12 21:46:40
# print(datetime.datetime.fromtimestamp(time.time()))
# halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
# newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
# oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
# print(halloween2015 == oct31_2015)
# print(halloween2015 > newyears2016)
# print(newyears2016 > halloween2015)
# print(newyears2016 != oct31_2015)

# timedelta 数据类型，它表示一段时间，而不是一个时刻
# delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(str(delta))

# dt = datetime.datetime.now()
# print(dt)  # 2020-11-22 23:03:55.317409
# thousandDays = datetime.timedelta(days=1000)
# print(dt + thousandDays)  # 2023-08-19 23:03:55.317409

# oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
# aboutThirtyYears = datetime.timedelta(days=365 * 30)
# print(oct21st)  # 2015-10-21 16:29:00
# print(oct21st - aboutThirtyYears)  # 1985-10-28 16:29:00
# print(oct21st - (2 * aboutThirtyYears))  # 1955-11-05 16:29:00

# halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
# while datetime.datetime.now() < halloween2016:
#     time.sleep(1)

# 将 datetime 对象转换为字符串，strftime 中的 f 表示 format
# oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
# print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))  # 2015/10/21 16:29:00
# print(oct21st.strftime('%I:%M %p'))  # 04:29 PM
# print(oct21st.strftime("%B of '%y"))  # October of '15

# 将字符串转换成 datetime 对象，strptime 中的 p 表示 parse 解析
# print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
# print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
# print(datetime.datetime.strptime("October of '15", "%B of '%y"))
# print(datetime.datetime.strptime("November of '63", "%B of '%y"))

# 多线程
import threading

# print('Start of program.')
# def takeANap():
#     time.sleep(5)
#     print('Wake up!')
# threadObj = threading.Thread(target=takeANap)
# threadObj.start()
# print('End of program.')

# threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],
#                              kwargs={'sep': ' & '})
# threadObj.start()  # Cats & Dogs & Frogs

# threadObjs = []
# for i in range(0, 1400, 100):
#     threadObj = threading.Thread(target=print, args=['Thread1'])
#     threadObjs.append(threadObj)
#     threadObj.start()
# for threadObj in threadObjs:
#     threadObj.join()  # 所有的 join()调用返回后， 'Done.'字符串才会打印
# print('Done.')

# 从 Python 启动其他程序
import subprocess

# calc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
# print(calc)  # <subprocess.Popen object at 0x0000020B364D8608>
# print(calc.poll() is None)  # True
# print(calc.wait())  # 0
# print(calc.poll())  # 0

# 向 Popen()传递命令行参数，用记事本打开文件
# subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\install.ini'])

# 打开 Firefox 浏览器
# subprocess.Popen(r'C:\Program Files\Mozilla Firefox\\firefox.exe')

# 运行 Python 脚本
# print(subprocess.Popen([r'C:\python37\python.exe', '01_1_入门与实践.py']))

# 用默认的应用程序打开文件
# 根据操作系统，向 Popen()传入'start'、 'open'或'see'
# Windows 上的'start'
# 在 OS X 上，open 程序用于打开文档文件和程序
# fileObj = open('data\\hello.txt', 'w')
# fileObj.write('Hello world!')
# fileObj.close()
# subprocess.Popen(['start', 'data\\hello.txt'], shell=True)

# 简单的倒计时程序
# timeLeft = 60
# while timeLeft > 0:
#     print(timeLeft, end='')
#     time.sleep(1)
#     timeLeft = timeLeft - 1
# subprocess.Popen(['start', 'data\\alarm.wav'], shell=True)







