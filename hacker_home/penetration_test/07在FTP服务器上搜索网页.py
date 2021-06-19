#!/usr/bin/python
# -*- coding:utf-8 -*-
# 测试以下服务器是否提供 Web 服务
import ftplib


def return_default(ftp):
    try:
        dir_list = ftp.nlst()
    except:
        dir_list = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        return
    ret_list = []
    for filename in dir_list:
        fn = filename.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn or '.html' in fn:
            print('[+] Found default page: ' + filename)
            ret_list.append(filename)
    return ret_list


host = '192.168.0.1'
username = 'guest'
password = 'guest'
ftp = ftplib.FTP(host)
ftp.login(username, password)
return_default(ftp)



