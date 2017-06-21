# -*- coding: utf-8 -*
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from smtplib import SMTP_SSL


class SendEmail(object):
    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((
            Header(name, 'utf-8').encode(),
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    def send_email(self, msg):
        from_addr = 'hntangqi374@163.com'
        password = raw_input('Password: ')
        to_addr = ['hntangqi374@163.com']
        smtp_server = 'smtp.163.com'

        msg['From'] = self._format_addr(u'七哥 <%s>' % from_addr)
        msg['To'] = self._format_addr(u'<%s>' % ','.join(to_addr))
        msg['Subject'] = Header(u'来自Python星球的问候……', 'utf-8').encode()

        print ('send email start')
        server = SMTP_SSL(smtp_server)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        print ('send email end')

    def send_html(self, html):
        msg = MIMEText(html, 'html', 'utf-8')
        self.send_email(msg)

    def send_text(self, text):
        msg = MIMEText(text, 'plain', 'utf-8')
        self.send_email(msg)


# send_email = SendEmail()
# send_email.send_text("hello, send by Python..")
