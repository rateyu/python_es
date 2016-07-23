__author__ = 'myu2'

import poplib
import sys

import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

reload(sys)
sys.setdefaultencoding('utf8')

# email = raw_input('Email: ')
# password = raw_input('Password: ')
# pop3_server = raw_input('POP3 server: ')

email = 'y81212@163.com'
password = 'ym=999526'
pop3_server = 'pop.163.com'


server = poplib.POP3(pop3_server)
print(server.getwelcome())

server.user(email)
server.pass_(password)

print('Messages: %s. Size: %s' % server.stat())

resp, mails, octets = server.list()

print(mails)

index = len(mails)
resp, lines, octets = server.retr(index)
msg_content = '\r\n'.join(lines)

msg = Parser().parsestr(msg_content)




server.quit()