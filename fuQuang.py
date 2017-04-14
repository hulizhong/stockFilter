#!/usr/bin/env python
# coding=utf-8

from ConfigParse import ConfigParse
from HttpClient import HttpClient
from PgClient import PgClient

'''
import sl4a
droid = sl4a.Android()
droid.smsSend("18501960037","sms")
'''


'''
import lxml.etree  
doc = lxml.etree.parse("/home/stockFilter/201612")

import libxml2
doc = libxml2.parseFile

try: 
    import xml.etree.cElementTree as ET 
except ImportError: 
    import xml.etree.ElementTree as ET 
    import sys

try:
    tree = ET.parse("/home/stockFilter/201612")     #打开xml文档 
    #root = ET.fromstring(country_string) #从字符串传递xml 
    root = tree.getroot()         #获得root节点  
    print root
except Exception, e: 
    print "Error:cannot parse file, cause ", e
'''

'''
import xml.dom.minidom as domparse

try:
    dom = domparse.parse("/home/stockFilter/201612")  
except Exception, e:
    print "Will exit, cause ", e
    raise e
'''
#root = dom.documentElement
#print root
#itemlist = root.getElementsByTagName('login')
#item = itemlist[0]
#print item.getAttribute("username")
#print item.getAttribute("passwd")
#
#itemlist = root.getElementsByTagName("item")
#item = itemlist[0]                   #通过在itemlist中的位置区分
#print item.getAttribute("id") 
#
#item2 = itemlist[1]                  #通过在itemlist中的位置区分
#print item2.getAttribute("id")

'''
conf = ConfigParse("./conf.xml")
print conf.getValue("config.http.isssl")
print conf.getValue("config.http.processtimeout")
print conf.getValue("config.http.cacert")
'''



httpcli = HttpClient("./conf.xml")
res = httpcli.sendRequest("GET", "/", body=None, head=None)
print res.getheaders()
#print res.read()

pgcli = PgClient("./conf.xml")
res = pgcli.query("select * from deadlock.t_transaction");
print res
