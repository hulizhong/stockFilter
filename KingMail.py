#!/usr/bin/env python
# coding=utf-8


import smtplib
import chardet
from email.mime.text import MIMEText
from email.header import Header
from ProCommon import logger
 
class KingMail(object):
    """
    email sent class replace sms notify. 
    """
    def __init__(self):
        self.mailhost = "smtp.yeah.net"
        self.user = "rabinhu@yeah.net"
        self.pswd = "---------"
        self.sender = 'rabinhu@yeah.net'
        self.receivers = ['hulizhong@yeah.net', 'hulizhong@skyguard.com.cn']
        self.smtpObj = smtplib.SMTP() 
        self.smtpObj.connect(self.mailhost, 25)
        self.smtpObj.login(self.user, self.pswd)  

    def __del__(self):
        ### bug, Exception smtplib.SMTPServerDisconnected: SMTPServerDisconnected('Connection unexpectedly closed',)
        #self.smtpObj.quit()
        pass

    def sendtxt(self, content):
        try:
            ### text/plain will due to outlook recv mail as txt file.
            message = MIMEText(content, 'plain', 'utf-8')
            message['Subject'] = Header('金花策略中心', 'utf-8')
            message['From'] = self.sender
            ### bug, if receivers is a list, use .join(receivers)
            #message['To'] = self.receivers
            message['To'] = ','.join(self.receivers)
            self.smtpObj.sendmail(self.sender, self.receivers, message.as_string())
        except smtplib.SMTPException, e:
            logger.errLog("Error: 无法发送邮件, cause:", e)
            #print isinstance(e.smtp_error, unicode)
            #print isinstance(e.smtp_error, 'utf-8')
            #print type(e)
            #fencoding=chardet.detect(e.smtp_error)
            #print fencoding

    def sendhtml(self, content):
        try:
            ### text/plain will due to outlook recv mail as txt file.
            message = MIMEText(content, 'html', 'utf-8')
            message['Subject'] = Header('金花策略中心', 'utf-8')
            message['From'] = self.sender
            ### bug, if receivers is a list, use .join(receivers)
            #message['To'] = self.receivers
            message['To'] = ','.join(self.receivers)
            self.smtpObj.sendmail(self.sender, self.receivers, message.as_string())
        except smtplib.SMTPException, e:
            logger.errLog("Error: 无法发送邮件, cause:", e)
            #print isinstance(e.smtp_error, unicode)
            #print isinstance(e.smtp_error, 'utf-8')
            #print type(e)
            #fencoding=chardet.detect(e.smtp_error)
            #print fencoding

#k = KingMail()
#fs = open("/home/stockFilter/dt")
#dt = fs.read()
#k.sendhtml(dt)
