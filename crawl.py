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


class ReqSessionClient(object):
    """
    http session client with requests package.
    """
    def __init__(self, argsHeaders):
        '''
        argsHeaders must include 
            "Host": "www.zhihu.com",
        '''
        self.session = requests.Session()
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        }
        for key in argsHeaders.keys():
            self.headers[key] = argsHeaders[key]

    def __del__(self):
        self.session.close()

    def getPage(self, url):
        """
        """
        try:
            response = self.session.get(url, headers=self.headers, timeout=10, verify=False)
            response.encoding = 'utf8'
        except RequestException as e:
            print('{} error {}'.format(url, e))
            return None
        else:
            if response.ok:
                return response.text
        return None

    def savePage(self, url, file):
        """
        """
        try:
            response = self.session.get(url, headers=self.headers, timeout=10, verify=False)
            response.encoding = 'utf8'
        except RequestException as e:
            print('{} error {}'.format(url, e))
        else:
            if response.ok:
                time.sleep(1)
                fp = open(file, 'wb')
                fp.write(response.text)
                fp.close()
                return True
        return False


    def parsePageFile(self, file):
        """
        """
        if not file:
            print('invalid content')
            return None
        try:
            pg = PQ(filename=file)
        except Exception as e:
            print('parse error: {}'.format(e))


    def parsePage(self, page):
        """
        """
        if not page:
            print('invalid content')
            return None
        try:
            pg = PQ(page)
        except Exception as e:
            print('parse error: {}'.format(e))


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


##### www.weather.com.cn WeatherForecast Demo.
#class WeatherForecast(ReqClient):
#    """
#    BeiJing Weather forecast.
#    """
#    def __init__(self, argsHeaders):
#        super(WeatherForecast, self).__init__(argsHeaders)
#
#    def parsePage(self):
#        """
#        """
#        if self.doc == None:
#            print('invalid content')
#            return None
#        try:
#            pg = PQ(self.doc)
#            v_source = PQ(resp)
#            for data in v_source('li'):
#                if PQ(data).attr('class') == 'sky skyid lv2 on':
#                    break
#            dt = PQ(data).text()
#            print dt
#            #mail = KingMail()
#            #mail.sendhtml(dt)
#        except Exception as e:
#            print('parse error: {}'.format(e))
#
#itpubHeader = {"Host":"www.weather.com.cn"}
#req = WeatherForecast(itpubHeader )
#resp = req.getPage("http://www.weather.com.cn/weather/101010100.shtml")
#req.parsePage()


##### www.itpub.net/star ItpubReqClient Demo
#class ItpubReqClient(ReqClient):
#    """
#    www.itpub.net BBS star person.
#    """
#    def __init__(self, argsHeaders):
#        super(ItpubReqClient, self).__init__(argsHeaders)
#
#    def parsePage(self):
#        """
#        """
#        if self.doc == None:
#            print('invalid content')
#            return None
#        try:
#            resp = re.sub("meta charset=\"gb2312\"", "meta charset=\"utf8\"", self.doc)
#            v_list = PQ(resp)
#            for data in v_list('div'):
#                if PQ(data).attr('class') == 'bor1':
#                    for it in PQ(data).children():
#                        print '--->', PQ(it).text()
#                    print '\n\n-----------------------------------------------------'
#        except Exception as e:
#            print('parse error: {}'.format(e))
#
#
#baseurl = "http://www.itpub.net/star/?page="
#urls = []
#for i in range(1,18):
#    url = baseurl + str(i)
#    urls.append(url)
#print urls
#
#itpubHeader = {"Host":"www.itpub.net"}
#req = ItpubReqClient(itpubHeader)
#req.getPage("http://www.itpub.net/star/?page=1", 'gbk')
#req.parsePage()

