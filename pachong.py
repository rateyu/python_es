__author__ = 'myu2'
# coding=utf-8 获取url里面的内容，需要过滤html标签
import urllib
import sys
import re
import pyes
conn = pyes.ES('192.168.1.14:9200')

type = sys.getfilesystemencoding()

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://rateyu.github.io/2014/11/11/emacs%E5%AD%A6%E4%B9%A0%E4%BD%BF%E7%94%A8.html")

# 过滤html标签
dr = re.compile(r'<[^>]+>',re.S)
dd = dr.sub('',html)
# myhtml = dd.decode('utf-8').encode(type)
print dd.decode('utf-8').encode(type)

conn.index({"name":"Joe Tester2", "parsedtext":"Joe Testere nice guy","content":dd, "uuid":"11111", "position":1}, "test-index", "test-type", 1)

# import re
# html='<a href="http://www.jb51.net">脚本之家</a>,Python学习！'
# dr = re.compile(r'<[^>]+>',re.S)
# dd = dr.sub('',html)
# print(dd)

# print "--------------------"
# print html.decode('utf-8').encode('gbk')