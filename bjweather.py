#!/usr/bin/env python
# coding=utf-8

from KingMail import KingMail
import sys
import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as PQ
#from lxml import etree
import codecs
import chardet
import time
import re

'''
Python在安装时，默认的编码是ascii，当程序中出现非ascii编码时，python的处理常常会报这样的错
    UnicodeDecodeError: 'ascii' codec can't decode byte 0x?? in position 1: ordinal not in range(128)，
python没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。`
'''
print 'sys.getdefaultencoding', sys.getdefaultencoding()  
reload(sys)
sys.setdefaultencoding('utf8')  
print 'sys.setdefaultencoding utf8'
print 'sys.getdefaultencoding', sys.getdefaultencoding()  
##sys.setdefaultencoding('gb2312')  


class ReqClient(object):
    """
    http client with requests package.
    """
    def __init__(self, argsHeaders):
        '''
        argsHeaders must include 
            "Host": "www.zhihu.com",
        '''
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        }
        for key in argsHeaders.keys():
            self.headers[key] = argsHeaders[key]
        self.doc = None

    def __del__(self):
        pass


    def getPage(self, url, charset='utf8'):
        """
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10, verify=False)
        except RequestException as e:
            print('{} error {}'.format(url, e))
            self.doc = None
            return None
        else:
            if response.ok:
                if charset == 'utf8':
                    response.encoding = 'utf8'
                    self.doc = response.text
                else:
                    #maybe gbk, gb2312, utf8.
                    self.doc = (response.content.decode(charset)).encode('utf8')
                return self.doc
            else:
                print "Error: get ", url, " return ", response.code
                self.doc = None
                return None


    def savePage(self, url, file, charset='utf8'):
        """
        """
        if self.doc == None:
            res = self.getPage(url, charset)
            if (res == None):
                return False
        fp = open(file, 'wb')
        fp.write(self.doc)
        fp.close()
        return True


    def parsePage(self):
        """
        """
        if self.doc == None:
            print('invalid content')
            return None
        try:
            pg = PQ(self.doc)
        except Exception as e:
            print('parse error: {}'.format(e))



class WeatherForecast(ReqClient):
    """
    BeiJing Weather forecast.
    """
    def __init__(self, argsHeaders):
        super(WeatherForecast, self).__init__(argsHeaders)

    def parsePage(self):
        """
        """
        if self.doc == None:
            print('invalid content')
            return None
        try:
            pg = PQ(self.doc)
            v_source = PQ(resp)
            for data in v_source('li'):
                if PQ(data).attr('class') == 'sky skyid lv2 on':
                    break
            dt = PQ(data).text()
            print dt
            mail = KingMail()
            mail.sendhtml(dt)
        except Exception as e:
            print('parse error: {}'.format(e))

itpubHeader = {"Host":"www.weather.com.cn"}
req = WeatherForecast(itpubHeader )
resp = req.getPage("http://www.weather.com.cn/weather/101010100.shtml")
req.parsePage()

