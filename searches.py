__author__ = 'myu2'


from pyes import *
# import sys
# reload(sys)
# sys.setdefaultencoding('gbk')

conn = ES('192.168.1.14:9200')
q = TermQuery("content", "emacs")
results = conn.search(query = q)
for r in results:
   print r