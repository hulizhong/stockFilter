#!/usr/bin/env python
# coding=utf-8

## for pyquery test

import sys
from pyquery import PyQuery as pq
from lxml import etree

#url v_source=pq(url='http://yunvs.com/list/mai_1.html')
#str v_source=pq("")
v_source = pq(filename="./pqTestData.html")
for data in v_source('tr'):
    ##各种打印
    print "--------------data\n", data
    print "-------pq(data).html()\n", pq(data).html()
    print "--------pq(data)\n", pq(data)
    print "--------pq(data).text()\n", pq(data).text()
    print "++++++++++++++"

sys.exit()
'''
trdata = v_source('tr')
print trdata

for data in trdata:
    ##打印每段
    for i in range(len(data)):
        #print pq(data).find('td').eq(i)
        print pq(data).find('td').eq(i).text()
    #print pq(data).find('td').eq(5).text()
    ##打印每个概念
    v_ind = pq(data).find('td').eq(5)
    for i in range(len(pq(v_ind).find('a'))):
        print pq(v_ind).find('a').eq(i).text()
    print '---------------------'
'''

