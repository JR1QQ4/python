#!/usr/bin/python
# -*- coding:utf-8 -*-
# Namp 工具包提供 ACK、RST、FIN 或 SYN-ACK 扫描
# 其他端口扫描类型：
#   TCP SYN SCAN--半开放扫描，发送一个SYN宝，启动一个TCP会话，并等待响应的数据包，如果收到一个reset包，表明端口是关闭的，而如果收到一个SYN/ACK包，则表示相应的端口是关闭的
#   TCP NULL SCAN--NULL扫描把TCP头中的所有标志位都设为NULL，如果收到一个RST包，则表示相应的端口是关闭的
#   TCP FIN SCAN--TCP FIN扫描发送一个表示拆除一个活动的TCP连接的FIN包，让对方关闭连接，如果收到了一个RST包，则表示相应的端口是关闭的
#   TCP XMAS SCAN--TCP XMAS扫描发送PSH、FIN、URG和TCP标志位被设为1的数据包，如果收到一个RST包，则表示相应的端口是关闭的


import nmap
import optparse


def nmap_scan(tgt_host, tgt_port):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(tgt_host, tgt_port)
    state = nm_scan[tgt_host]['tcp'][int(tgt_port)]['state']
    print(" [*] " + tgt_host + " tcp/" + tgt_port + " " + state)


def main():
    parser = optparse.OptionParser("usage%prog -H <target host> -p <target port>")
    parser.add_option("-H", dest="tgt_host", type="string", help="specify target host")
    parser.add_option("-p", dest="tgt_port", type="string", help="specify target port[s] separated by comma")
    (options, args) = parser.parse_args()
    print(parser.parse_args())
    tgt_host = options.tgt_host
    tgt_ports = str(options.tgt_port).split(",")
    if tgt_host is None or tgt_ports[0] is None:
        print(parser.usage)
        exit(0)
    for tgt_port in tgt_ports:
        nmap_scan(tgt_host, tgt_port)


if __name__ == '__main__':
    # 使用cmd运行，python *.py -H 10.50.60.125 -p 21,1720
    main()





















