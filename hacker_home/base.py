#!/usr/bin/python
# -*- coding:utf-8 -*-
import crypt


def test_pass(crypt_pass):
    """第一个程序：UNIX口令破解机"""
    slat = crypt_pass[0:2]
    dict_file = open("dictionary.txt", "r")
    for word in dict_file.readlines():
        word = word.strip('\n')
        crypt_word = crypt.crypt(word, slat)
        if crypt_word == crypt_pass:
            print("[+] Found Password: " + word + "\n")
            return
    print("[-] Password Not Found.\n")
def main():
    pass_file = open("passwords.txt")
    for line in pass_file.readlines():
        if ":" in line:
            user = line.split(":")[0]
            crypt_pass = line.split(":")[1].strip(" ")
            print("[*] Cracking Password For: " + user)
            test_pass(crypt_pass)