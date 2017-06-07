# -*- coding: utf-8 -*
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from smtplib import SMTP_SSL


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


# from_addr = raw_input('From: ')
# password = raw_input('Password: ')
# to_addr = raw_input('To: ')
# smtp_server = raw_input('SMTP server: ')

from_addr = '821064838@qq.com'
password = raw_input('Password: ')
to_addr = 'hntangqi374@163.com'
smtp_server = 'smtp.qq.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'七哥 <%s>' % from_addr)
msg['To'] = _format_addr(u'<%s>' % to_addr)
msg['Subject'] = Header(u'来自Python星球的问候……', 'utf-8').encode()

print ('send email start')
server = SMTP_SSL(smtp_server)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
print ('send email end')
