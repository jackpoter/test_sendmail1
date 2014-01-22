# -*- coding: utf-8 -*-
import smtplib, email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(sub, text, smtp_debug, content, send_mail_host, send_mail_port, send_mail_user_name, send_mail_pswd, send_mail_postfix, get_mail_user, get_mail_postfix, charset):
    send_mail_address = send_mail_user_name + '@' + send_mail_postfix
    to_adress = get_mail_user + '@' + get_mail_postfix
    msg = MIMEMultipart()
    msg['Subject'] = email.Header.Header(sub,charset)
    msg['From'] = send_mail_address
    msg['To'] = to_adress
    #Contents = MIMEText(sub,'plain')      #
    Contents = MIMEText(text,'html',charset)     #
    msg.attach(Contents)
    #msg = email.mime.text.MIMEText(content,'html',charset)
    try:
        smtp = smtplib.SMTP(send_mail_host, send_mail_port)
        if smtp_debug == 1:
            smtp.set_debuglevel(1)
        smtp.ehlo()  
        smtp.starttls()  
        smtp.ehlo()  
        smtp.login(send_mail_user_name, send_mail_pswd)  
        print 'login ok'
        smtp.sendmail(send_mail_address, to_adress, msg.as_string())
        print 'send ok'
        return True
    except Exception,e:
        print 'sendmail Error:', e
        return False
    finally:
        smtp.quit()

if __name__ == "__main__":
    
    send_mail_host = 'smtp.gmail.com'
    send_mail_port = 587
    #send_mail_user = 'goodman'
    #send_mail_user_name = u'goodman bbs'
    send_mail_user_name = 'goodman'
    send_mail_pswd = '123321123'
    send_mail_postfix = 'gmail.com'
    smtp_debug = 1
    charset = 'GBK'
    #sub = u'中文测试用'.encode(charset)
    #sub = u'中文测试用'
    sub = '中文测试用'
    #sub = unicode("中文测试").encode('utf-8')
    #sub = u'中文测试用'
    #text = u'邮件内容中'.encode(charset)
    text = '邮件内容中'

    get_mail_user = 'goodman_save'
    get_mail_postfix = 'gmail.com'
    get_mail_host = 'pop.gmail.com'
    send(sub, text, smtp_debug, content, send_mail_host, send_mail_port, send_mail_user_name, send_mail_pswd, send_mail_postfix, get_mail_user, get_mail_postfix, charset)

