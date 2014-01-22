send_mail_host = 'smtp.gmail.com'
send_mail_user = 'goodman'
send_mail_user_name = u'goodman bbs'
send_mail_pswd = '12345678'
send_mail_postfix = 'gmail.com'
get_mail_user = 'goodman'
charset = 'utf-8'

get_mail_postfix = 'gmail.com'
get_mail_host = 'smtp.gmail.com'
def send(sub, content, reciver = get_mail_user + get_mail_postfix):
send_mail_address = send_mail_user_name + '<' + send_mail_user + '@' + send_mail_postfix + '>'
msg = email.mime.text.MIMEText(content,'html',charset)
msg['Subject'] = email.Header.Header(sub,charset)
msg['From'] = send_mail_address
msg['to'] = to_adress = reciver
try:
#smtp = smtplib.SMTP(smtp_google, smtp_port)
stp = smtplib.SMTP(send_mail_host,587)
stp.connect(send_mail_host)
stp.login(send_mail_user,send_mail_pswd)
stp.sendmail(send_mail_address,to_adress,msg.as_string())
stp.close()
return True
except Exception,e:
print(e)
return False
