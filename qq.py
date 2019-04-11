import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"
mail_user = "xxxxxx@qq.com"
mail_pass = "xxxxxx"

sender = 'xxxxxx@qq.com'
receivers = ['xxxxxx@aliyun.com']

message = MIMEText('EOS hash notification...', 'plain', 'utf-8')
message['From'] = Header("JeroQQ", 'utf-8')
message['To'] = Header("JeroAliyun", 'utf-8')
subject = 'EOS hash notification...'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, "465") #465 or 587
    #smtpObj.set_debuglevel(1)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print("Mail has been sent successfully.")    
except smtplib.SMTPException as e:
    print(e)