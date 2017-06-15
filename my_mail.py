#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from conf.my_env import envi
from my_log import logger


def send_mail(sub, content):
    receiver = envi['mail_receiver']
    if receiver == ['']:
        logger.warn('mail[' + sub + '] fail, empty receive list!')
        return False

    sender = "netmon<%s>" % envi['smtp_usr']
    msg = MIMEText(content, 'plain', 'gbk')
    msg['Subject'] = Header(sub, 'gbk')
    msg['From'] = sender

    try:
        smtp = smtplib.SMTP()
        smtp.connect(envi['smtp_server'])
        smtp.login(envi['smtp_usr'], envi['smtp_pwd'])
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception as e:
        logger.error(str(e))
        return False
    else:
        logger.info('success sending mail [' + sub + '] to ' + str(receiver))
        return True

if __name__ == '__main__':

    send_mail(u'这是python测试邮件22', u'python发送邮件')
