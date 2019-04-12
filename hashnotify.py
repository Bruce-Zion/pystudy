from datetime import datetime
import time
from eospy.cleos import Cleos
import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_host = "smtp.qq.com"
mail_user = "jero2008@qq.com"
mail_pass = "xxxxxx"

sender = 'jero2008@qq.com'
receivers = ['jero2008@aliyun.com']

message = MIMEText('EOS hash notification...', 'plain', 'utf-8')
message['From'] = Header("JeroQQ", 'utf-8')
message['To'] = Header("JeroAliyun", 'utf-8')
subject = 'EOS hash notification...'
message['Subject'] = Header(subject, 'utf-8')


ce = Cleos(url='https://api.eosnewyork.io')    


def blockT(x):
    return int(x[17:19] + x[20:])

lhFlag = 3 #0 for L, 1 for H, 2 for Tie; 3 is start value
lhCount =0 #count continous numbers
tieNum = 0 #continuous tie number just before
lhMap = {'0':10, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':11, 'b':11, 'c':12, 'd':12, 'e':13, 'f':13}


while 1:
    now = datetime.now()

    while now.second != 0:
        time.sleep(0.1)
        now = datetime.now()
        
    resp = ce.get_info()
    blockTime = resp['head_block_time']
    blockNum = resp['head_block_num']
    lhdStr = resp['head_block_id'][-2:]
    
    #print(blockNum, blockTime, lhdStr)
    
    if blockT(blockTime) != 0:
        newBlockNum = blockNum - 1
        respNew = ce.get_block(newBlockNum)
        newBlockTime = respNew['timestamp']
                
        #print(newBlockNum, newBlockTime, lhdStr)
    
        while blockT(newBlockTime) < blockT(blockTime):
            blockNum = newBlockNum
            blockTime = newBlockTime
            lhdStr = respNew['id'][-2:]
        
            newBlockNum = blockNum - 1
            respNew = ce.get_block(newBlockNum)
            newBlockTime = respNew['timestamp']
            
            #print(newBlockNum, newBlockTime, lhdStr)
        
    lNum = lhMap[lhdStr[0]]
    hNum = lhMap[lhdStr[1]]

    if lNum > hNum:
                
        if lhFlag == 3 or lhFlag == 1: #Start or Previous H
            lhFlag = 0
            lhCount = 1 + tieNum
        else:                          #Previous Tie or L
            lhFlag = 0
            lhCount += 1
            
        tieNum = 0
                    
    elif lNum < hNum:
                
        if lhFlag == 3 or lhFlag == 0:
            lhFlag = 1
            lhCount = 1 + tieNum
        else:
            lhFlag = 1
            lhCount += 1
            
        tieNum = 0
        
    else:
        tieNum += 1
        
        if lhFlag == 3:
            lhFlag = 2
        lhCount += 1
        
    #if lhCount >= 5, send a mail to notify
    print(lhFlag, lhCount)
    
    #send notify email
    if lhCount >= 3:
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, "465") #465 or 587
            #smtpObj.set_debuglevel(1)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            smtpObj.quit()
            print("Mail has been sent successfully.")    
        except smtplib.SMTPException as e:
            print(e)
    
    time.sleep(2) #sleep to prevent quick repeat again    