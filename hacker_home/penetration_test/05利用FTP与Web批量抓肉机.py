#!/usr/bin/python
# -*- coding:utf-8 -*-
import ftplib


def anon_login(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Faild.')
        return False


# python *.py
host = '192.168.0.1'
anon_login(host)




