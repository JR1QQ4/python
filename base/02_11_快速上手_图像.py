#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第二部分 自动化任务

print('********* 第 17 章 操作图像 ***********')

# from PIL import ImageColor
#
# print(ImageColor.getcolor('red', 'RGBA'))  # (255, 0, 0, 255)
# print(ImageColor.getcolor('RED', 'RGBA'))  # (255, 0, 0, 255)
# print(ImageColor.getcolor('Black', 'RGBA'))  # (0, 0, 0, 255)
# print(ImageColor.getcolor('chocolate', 'RGBA'))  # (210, 105, 30, 255)
# print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))  # (100, 149, 237, 255)

from PIL import Image

# 处理 Image 数据类型
img = Image.open('data\\catlogo.png')

# print(img.size)  # (808, 768)
# width, height = img.size
# print(width, height)
# print(img.filename)  # data\catlogo.png
# print(img.format)  # PNG
# print(img.format_description)  # Portable network graphics
# print(img.save('data\\catlogo.png'))  # None

# im = Image.new('RGBA', (100, 200), 'purple')
# im.save('data\\purpleImage.png')
# im2 = Image.new('RGBA', (20, 20))
# im2.save('data\\transparentImage.png')

# 裁剪图片
# croppedIm = img.crop((335, 345, 565, 560))
# croppedIm.save('data\\cropped.png')

# 复制和粘贴图像到其他图像
# catCopyIm = img.copy()
# faceIm = img.crop((335, 345, 565, 560))
# catCopyIm.paste(faceIm, (0, 0))
# catCopyIm.paste(faceIm, (400, 500))
# catCopyIm.save('data\\pasted.png')

# 平铺
# faceIm = img.crop((335, 345, 565, 560))
# catImWidth, catImHeight = img.size
# faceImWidth, faceImHeight = faceIm.size
# catCopyTwo = img.copy()
# for left in range(0, catImWidth, faceImWidth):
#     for top in range(0, catImHeight, faceImHeight):
#         # print(left, top)
#         catCopyTwo.paste(faceIm, (left, top))
# catCopyTwo.save('data\\pasted2.png')

# 调整图像大小
# width, height = img.size
# quartersizedIm = img.resize((int(width / 2), int(height / 2)))
# quartersizedIm.save('data\\quartersized.png')

# 旋转和翻转图像
# img.rotate(90).save('data\\rotated90.png')
# img.rotate(90, expand=True).save('data\\rotated90_2.png')
# img.transpose(Image.FLIP_LEFT_RIGHT).save('data\\horizontal_flip.png')

# 更改单个像素
# im = Image.new('RGBA', (100, 100))
# im.getpixel((0, 0))
# for x in range(100):
#     for y in range(50):
#         im.putpixel((x, y), (210, 210, 210))
# from PIL import ImageColor
# for x in range(100):
#     for y in range(50, 100):
#         im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
# print(im.getpixel((0, 0)))
# print(im.getpixel((0, 50)))
# im.save('data\\putPixel.png')

# 在图像上画画
# from PIL import Image, ImageDraw
# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)
# draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
# draw.rectangle((20, 30, 60, 60), fill='blue')
# draw.ellipse((120, 30, 160, 60), fill='red')
# draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),
#              fill='brown')
# for i in range(100, 200, 10):
#     draw.line([(i, 0), (200, i - 100)], fill='green')
# im.save('data\\drawing.png')

# 绘制字体
# from PIL import Image, ImageDraw, ImageFont
# import os
# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)
# draw.text((20, 150), 'Hello', fill='purple')
# fontsFolder = 'FONT_FOLDER'
# arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
# draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
# im.save('data\\text.png')

