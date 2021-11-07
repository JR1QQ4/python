#!/usr/bin/python
# -*- coding:utf-8 -*-
from configparser import ConfigParser
import yaml
import json

# # 第一步：创建一个配置文件解析器对象
# cp = ConfigParser()
# # 第二步：读取配置文件中的内容到配置文件解析器中
# cp.read('setting.ini', encoding='utf-8')
# # 第三步：读取配置内容
# res = cp.get('logging', 'file')
# res2 = cp.getint('mysql', 'port')
# # res3 = cp.getboolean()
# # res4 = cp.getfloat()
# # 其他：写入文件
# cp.set('mysql', 'username', 'sa')
# cp.write(fp=open('setting.ini', 'w', encoding='utf-8'))


class Config(ConfigParser):
    def __init__(self, conf_file):
        super(Config, self).__init__()
        self.read(conf_file, encoding='utf-8')


# with open('data.yaml', 'r', encoding='utf-8') as f:
#     r = yaml.load(f, Loader=yaml.Loader)
# print(r)

# 使用 json.load 会把 json 格式的内容自动转换为 python 字典格式的内容
with open('data.json', 'r', encoding='utf-8') as f:
    rs = json.load(f)
print(rs, type(rs))
temp = {'logging': {'level': 'DEBUG', 'file': 'logout.log'}, 'mysql': {'host': '127.0.0.1', 'port': 3306},
        'data': [11, True, False, None]}
print(json.dumps(temp), type(json.dumps(temp)))

if __name__ == '__main__':
    conf = Config('setting.ini')
    level = conf.get('logging', 'level')
