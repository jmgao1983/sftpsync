#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CRITICAL=50> ERROR=40> WARNING=30> INFO=20> DEBUG=10> NOTSET=0
# Important: directories here must end with '/'
envi = {
  # log config
  'log_lvl': 10,
  'log_size': 5,
  'log_rotate_num': 5,
  # cmm config
  'cmm_sftp_ip': '1.1.1.1',
  'cmm_sftp_port': 22,
  'cmm_sftp_user': 'user',
  'cmm_sftp_pass': 'pass',
  'cmm_data_dir': '/path/',
  'data_src_name': u'xxxx数据',
  'cmm_data_pattern': 'some_[0-9]{14}\.((md5)|(tar\.gz))',
  # prd config
  'prd_sftp_ip': '2.2.2.2',
  'prd_sftp_port': 22,
  'prd_sftp_user': 'user2',
  'prd_sftp_pass': 'pass2',
  'prd_data_dir': '/path2/',
  # local config
  # program working direcotry, must end with '/'
  'cwd': '/home/xxx/sftpsync/',
  'smtp_server': 'xx.xx.xx',
  'smtp_usr': 'someuser@somedomain',
  'smtp_pwd': 'somepass',
  'mail_receiver': ['xxxx@xxx.com', '137*****451@139.com']
}
