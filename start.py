#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from my_log import logger
from my_sftp import sftp_sync
from conf.my_env import envi


def start():
    logger.debug('Program begin: auto sync files via sftp')
    logger.debug('step 0: start a vpn tunnel')
    vpn_log = envi['cwd'] + 'log/vpn.log'
    vpn_conf = envi['cwd'] + 'conf/client.ovpn'
    cmd = 'openvpn --config %s > %s 2>&1 &' % (vpn_conf, vpn_log)
    try:
        os.system(cmd)
        time.sleep(30)
        sync = sftp_sync()
        if sync is not None:
            logger.debug('step 1: pull data from cmm')
            if sync.pull_from_cmm():
                logger.debug('step 2: push data to prd')
                sync.push_to_prd()
    finally:
        logger.debug('step 3: stop the vpn tunnel')
        cmd = "kill `ps -ef|grep openvpn|grep -v 'grep'|awk '{print $2}'`"
        os.system(cmd)
        time.sleep(10)
        logger.debug('Program end')

if __name__ == '__main__':
    start()
