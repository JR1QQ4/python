#!/usr/bin/python
# -*- coding:utf-8 -*-
# 常见端口 WEB_TCP80  Email_TCP25  FTP_TCP21
import optparse
from socket import *

# parser = optparse.OptionParser('usage %prog - H <target host> -p <target port>')
# parser.add_option("-H", dest='tgtHost', type='string', help='specify target host')
# parser.add_option("-p", dest='tgtPort', type='int', help='specify target port')
# (options, args) = parser.parse_args()
# tgtHost = options.tgtHost
# tgtPort = options.tgtPort
# if tgtHost is None or tgtPort is None:
#     print(parser.usage)
#     exit(0)
from threading import Thread, Semaphore

screen_lock = Semaphore(value=1)


def conn_scan(tgt_host, tgt_port):
    conn_skt = None
    try:
        conn_skt = socket(AF_INET, SOCK_STREAM)
        conn_skt.connect((tgt_host, tgt_port))
        conn_skt.send(b"ViolentPython\r\n")
        result = conn_skt.recv(100)
        screen_lock.acquire()
        print("[+]%d/tcp open" % tgt_port)
        print("[+] " + str(result))
        # conn_skt.close()
    except:
        screen_lock.acquire()
        print("[-]%d/tcp closed" % tgt_port)
    finally:
        screen_lock.release()
        conn_skt.close()


def port_scan(tgt_host=gethostname(), tgt_ports=None):
    if tgt_ports is None:
        tgt_ports = ['21', '22', '80']
    try:
        tgt_ip = gethostbyname(tgt_host)
    except:
        print("[-] Cannot resolve '%s': Unknown host" % tgt_host)
        return
    try:
        tgt_name = gethostbyaddr(tgt_ip)
        print("\n[+] Scan Results for: " + tgt_name[0])
    except:
        print("\n[+] Scan Results for: " + tgt_ip)
    setdefaulttimeout(1)
    # for tgt_port in tgt_ports:
    #     print("Scanning port " + tgt_port)
    #     conn_scan(tgt_host, int(tgt_port))
    for tgt_port in tgt_ports:
        t = Thread(target=conn_scan, args=(tgt_host, int(tgt_port)))
        t.start()


def main():
    parser = optparse.OptionParser('usage %prog - H <target host> -p <target port>')
    parser.add_option("-H", dest='tgtHost', type='string', help='specify target host')
    parser.add_option("-p", dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    # print(parser.parse_args())
    # print(options)
    # print(args)
    tgt_host = options.tgtHost
    tgt_ports = str(options.tgtPort).split(',')
    if tgt_host is None or tgt_ports[0] is None:
        # print("[-] Yo must specify a target host and port[s].")
        print(parser.usage)
        exit(0)
    port_scan(tgt_host, tgt_ports)


# cmd 运行：python portscanner.py -H 192.168.1.37 -P 21, 22, 80
if __name__ == '__main__':
    main()
