# -*- coding: utf-8 -*
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
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
to_addr = ['hntangqi374@163.com', '821064838@qq.com', '182249923@qq.com', '943262901@qq.com', '181703488@qq.com', '2414057159@qq.com']
smtp_server = 'smtp.qq.com'

msg = MIMEMultipart()
msg.attach(MIMEText('hello, send by Python...', 'plain', 'utf-8'))
msg['From'] = _format_addr(u'七哥 <%s>' % from_addr)
msg['To'] = _format_addr(u'<%s>' % ''.join(to_addr))
msg['Subject'] = Header(u'来自Python星球的美女', 'utf-8').encode()

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
attach_file = "img.tar.gz"
with open('./img.tar.gz', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('application', 'octet-stream')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename=attach_file)
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

print ('send email start')
server = SMTP_SSL(smtp_server)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
print ('send email end')




