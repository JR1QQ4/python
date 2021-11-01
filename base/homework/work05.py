#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging


def create_log(name='MyLog', level='DEBUG', filename='logout.log', fh_level='WARNING', sh_level='DEBUG'):
    # 1、创建日志收集器
    log = logging.getLogger(name)
    # 2、设置收集器等级
    log.setLevel(level)
    # 3、设置日志输出渠道
    # 3.1、输出文件的配置
    fh = logging.FileHandler(filename, encoding='utf-8')
    fh.setLevel(fh_level)
    log.addHandler(fh)
    # 3.2、输出控制台
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)
    # 4、设置日志输出的格式
    formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
    log_format = logging.Formatter(formats)
    fh.setFormatter(log_format)
    sh.setFormatter(log_format)
    # 5、返回一个日志收集器
    return log


if __name__ == '__main__':
    log1 = create_log()
    log1.info('info')
    log1.debug('debug')
    log1.warning('warning')
    log1.error('error')

