#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第二部分 自动化任务

print('********* 第 16 章 发送电子邮件和短信 ***********')

# 正如 HTTP 是计算机用来通过因特网发送网页的协议
# 简单邮件传输协议（SMTP）是用于发送电子邮件的协议
import smtplib
from email.mime.text import MIMEText

mail_host = ""  # 设置服务器
mail_user = ""    # 用户名
mail_order = ""   # 口令
from_addr = ""  # 发件人
to_addr = ""  # 收件人
send_msg = 'Subject: Solong.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob'  # 要发送的信息

# msg = MIMEText(send_msg, 'plain', 'utf-8')
# msg['Subject'] = '我是 Subject'
# msg['From'] = from_addr
# msg['To'] = to_addr

# smtpObj = smtplib.SMTP(host=mail_host, port=25)
# # smtpObj.connect(mail_host, 25)
# print(smtpObj.ehlo())  # (250, b'mail\n...
# print(smtpObj.starttls())  # (220, b'Ready to start TLS')
# print(smtpObj.login(mail_user, mail_order))  # (235, b'Authentication successful')
# print(smtpObj.sendmail(from_addr, [from_addr, to_addr], msg.as_string()))
# print(smtpObj.quit())

# 用 IMAP 获取和删除电子邮件
from imapclient import IMAPClient

# context manager ensures the session is cleaned up
# with IMAPClient(mail_host) as client:
#     client.login(mail_user, mail_order)
#     client.select_folder('INBOX')

    # search criteria are passed in a straightforward way
    # (nesting is supported)
    # messages = client.search(['NOT', 'DELETED'])
    # print(messages)

    # fetch selectors are passed as a simple list of strings.
    # response = client.fetch(messages, ['FLAGS', 'RFC822.SIZE'])

    # `response` is keyed by message id and contains parsed,
    # converted response items.
    # for message_id, data in response.items():
    #     print('{id}: {size} bytes, flags={flags}'.format(
    #         id=message_id,
    #         size=data[b'RFC822.SIZE'],
    #         flags=data[b'FLAGS']))



