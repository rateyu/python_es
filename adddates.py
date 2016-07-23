__author__ = 'myu2'
import pyes

conn = pyes.ES('192.168.1.14:9200')
conn.index({"name":"Joe Tester", "parsedtext":"Joe Testere nice guy","content":"test", "uuid":"11111", "position":1}, "test-index", "test-type", 1)
conn.index({"name":"Bill Baloney", "parsedtext":"Joe Testere nice guy", "uuid":"22222", "position":2}, "test-index", "test-type", 2)
