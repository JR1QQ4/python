#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第二部分 自动化任务

print('********* 第 18 章 用 GUI 自动化控制键盘和鼠标 ***********')

import pyautogui

pyautogui.PAUSE = 1  # 每次函数调用后暂停一秒
pyautogui.FAILSAFE = True  # 启动自动防故障功能

# 获取屏幕尺寸
print(pyautogui.size())  # (1920, 1080)
width, height = pyautogui.size()

# 移动鼠标
# for i in range(3):
#     pyautogui.moveTo(100, 100, duration=0.25)  # 右 下 时间
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# 获取鼠标位置
# print(pyautogui.position())

# 点击鼠标
# pyautogui.click(10, 5)  # (x, y, button='鼠标按键 left | middle | right'')

# 拖动鼠标
# import time
# time.sleep(3)
# pyautogui.click()  # click to put drawing program in focus
# distance = 200
# while distance > 0:
#     pyautogui.dragRel(distance, 0, duration=0.2)  # move right
#     distance -= 5
#     pyautogui.dragRel(0, distance, duration=0.2)  # move down
#     pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
#     distance -= 5
#     pyautogui.dragRel(0, -distance, duration=0.2)  # move up

# 滚动鼠标
# pyautogui.scroll(-200)  # 向下

# 获取屏幕快照
# im = pyautogui.screenshot()
# im.getpixel((50, 200))
# pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))

# 图像识别
# 如果你以前获得了屏幕快照，截取了提交按钮的图像， 保存为 submit.png
# pyautogui.locateOnScreen('submit.png')

# 通过键盘发送一个字符串
# pyautogui.click(100, 100); pyautogui.typewrite('Hello world!')

# 键名
# 按 a 键，然后是 b 键，然后是左箭头两次，最后是 X 和 Y 键
# pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

# 热键组合
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('c')
# pyautogui.keyUp('c')
# pyautogui.keyUp('ctrl')

