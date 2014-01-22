# -*- coding: utf-8 -*-
import smtplib, email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(sub, smtp_debug, content, send_mail_user_name, send_mail_pswd, send_mail_postfix, get_mail_user, get_mail_postfix, charset):
    send_mail_address = send_mail_user_name + '@' + send_mail_postfix
    to_adress = get_mail_user + '@' + get_mail_postfix
    #msg = email.mime.text.MIMEText(content,'html',charset)
    msg = MIMEMultipart()
    msg['Subject'] = email.Header.Header(sub,charset)
    msg['From'] = send_mail_address
    msg['To'] = to_adress
    Contents = MIMEText(sub,'plain')      #
    msg.attach(Contents)
    try:
        smtp = smtplib.SMTP(send_mail_host, 587)
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

if __name__ == "__main__":
    
    send_mail_host = 'smtp.gmail.com'
    #send_mail_user = 'goodman'
    #send_mail_user_name = u'goodman bbs'
    send_mail_user_name = 'goodman_bbs'
    send_mail_pswd = '123123123'
    send_mail_postfix = 'gmail.com'
    smtp_debug = 1
    charset = 'utf-8'
    sub = 'Hi there'

    get_mail_user = 'goodman_save'
    get_mail_postfix = 'gmail.com'
    get_mail_host = 'pop.gmail.com'
    send(sub, smtp_debug, content, send_mail_user_name, send_mail_pswd, send_mail_postfix, get_mail_user, get_mail_postfix, charset)
