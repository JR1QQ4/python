#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import zipfile


def fileToZip():
    """把文件打包压缩成zip格式的压缩包"""
    newZip = zipfile.ZipFile('new.zip', 'w')

    def writeToZip(file_path):
        """
        循环写入文件
        :param file_path: 需要压缩的文件的相对路径
        """
        for folder_file in os.listdir(file_path):
            folder_file_path = os.path.join(os.getcwd(), file_path, folder_file)
            current_file_path = file_path + '\\' + folder_file
            if os.path.isfile(folder_file_path):
                newZip.write(current_file_path, compress_type=zipfile.ZIP_DEFLATED)
            elif os.path.isdir(folder_file_path):
                newZip.write(current_file_path, compress_type=zipfile.ZIP_DEFLATED)
                writeToZip(current_file_path)
        if len(os.listdir(file_path)) == 0:
            return

    writeToZip('example')
    newZip.close()


fileToZip()
