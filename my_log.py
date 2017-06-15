#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from conf.my_env import envi

# ------------logging for python-script
logger = logging.getLogger('mylog')
logger.setLevel(envi['log_lvl'])
File1 = envi['cwd'] + 'log/python.log'
num = envi['log_rotate_num']
size = envi['log_size']
FM = '%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s'
DF = '%Y-%m-%d %H:%M:%S'
# 定义RotatingFileHandler，最多备份(num)个日志文件，每个日志文件(size)MB
RH = RotatingFileHandler(File1, 'a', size*1024*1024, num)
RH.setLevel(logging.DEBUG)
RH.setFormatter(logging.Formatter(FM, DF))
logger.addHandler(RH)
# 定义StreamHandler，输出到屏幕
SH = logging.StreamHandler()
SH.setLevel(logging.DEBUG)
SH.setFormatter(logging.Formatter(FM, DF))
logger.addHandler(SH)

if __name__ == '__main__':
    logger.error('this is a error!')
    logger.debug('this is a debug!')
