"""
邮件发送
"""

import yagmail

class SendEMail():
    def __init__(self):
        self.host = "smtp.163.com" #邮件服务器
        self.user = " " #发件人的邮箱地址
        self.passwd = " "  #授权码
    
    def sendmail(self, receivers, subject, content): 
        with yagmail.SMTP(user=self.user, password=self.passwd, host=self.host) as yg:
            for receiver in receivers:
                yg.send(receiver, subject, content)
        

if __name__ == '__main__':
    receivers = []  #收件人列表
    subject = " "   #邮件主题
    content = " "   #邮件正文
    sender = SendEMail()
    sender.sendmail(receivers, subject, content)