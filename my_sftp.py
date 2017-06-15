#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re, paramiko
from my_log import logger
from conf.my_env import envi
from my_mail import send_mail


class sftp_sync(object):
    def __init__(self):
        ldir = envi['cwd'] + 'data/'
        if not os.path.exists(ldir):
            try:
                os.makedirs(ldir)
            except Exception as e:
                logger.error(str(e))
                return False
        self.ldir = ldir
        self.loc_files = os.listdir(ldir)
        self.cmm_files = []
        self.trans_files = []
        logger.debug('loc files:' + str(self.loc_files))

    def pull_from_cmm(self):
        ip = envi['cmm_sftp_ip']
        port = envi['cmm_sftp_port']
        usr = envi['cmm_sftp_user']
        pwd = envi['cmm_sftp_pass']
        rdir = envi['cmm_data_dir']
        p = envi['cmm_data_pattern']
        try:
            target = paramiko.Transport((ip, port))
            target.connect(username=usr, password=pwd)
            sftp = paramiko.SFTPClient.from_transport(target)
            self.cmm_files = sftp.listdir(rdir)
            logger.debug('cmm files:' + str(self.cmm_files))
            # check out which files to transfar
            for f in self.cmm_files:
                if f not in self.loc_files and re.match(p, f) != None:
                    self.trans_files.append(f)
            logger.debug('need files:' + str(self.trans_files))
            # transfar via sftp get
            if self.trans_files == []:
                logger.warn('no data to pull')
                send_mail(u'车满满数据未更新', u'请咨询车满满技术')
            else:
                for f in self.trans_files:
                    sftp.get(rdir + f, self.ldir + f)
                logger.info('pulling from cmm finished')
        except Exception as e:
            logger.error(str(e))
            send_mail(u'自动同步车满满数据失败', str(e))
            return False
        target.close()
        return True

    def push_to_prd(self):
        if self.trans_files == []:
            logger.warn('no data to push')
            return False
        ip = envi['prd_sftp_ip']
        port = envi['prd_sftp_port']
        usr = envi['prd_sftp_user']
        pwd = envi['prd_sftp_pass']
        rdir = envi['prd_data_dir']
        try:
            target = paramiko.Transport((ip, port))
            target.connect(username=usr, password=pwd)
            sftp = paramiko.SFTPClient.from_transport(target)
            # transfar via sftp put
            for f in self.trans_files:
                sftp.put(self.ldir + f, rdir + f)
            logger.info('pushing to prd finished')
        except Exception as e:
            logger.error(str(e))
            send_mail(u'自动同步车满满数据失败', str(e))
            return False
        target.close()
        send_mail(u'自动同步车满满数据成功', u'some thing')
        return True

if __name__ == '__main__':
    s = sftp_sync()
    if s is not None:
        if s.pull_from_cmm():
            s.push_to_prd()
