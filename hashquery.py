from eospy.cleos import Cleos
import time

ce = Cleos(url='https://api.eosnewyork.io')

f = open('result.txt', 'a')



#print(resp['id'])
#print(resp['timestamp'])


#Start from block num 30,000,000
bnStart = 30837944
bn = bnStart

while 1:
    resp = ce.get_block(bn)
    testStr = resp['timestamp'][17:]
    print(testStr)
    
    if testStr=='00.000' or testStr=='00.500':
        f.write(str(resp['block_num']) +'  '+ resp['timestamp'] +'  '+ resp['id'][-2:] +'\n')
        break
    else:
        bn += 1
        time.sleep(0.5)

countRe = 1
bn += 115

while countRe < 1000:
        
    while 1:
        resp = ce.get_block(bn)
        testStr = resp['timestamp'][17:]
        print(testStr)
        print(bn)
        
        if testStr=='00.000' or testStr=='00.500':
            f.write(str(resp['block_num']) +'  '+ resp['timestamp'] +'  '+ resp['id'][-2:] +'\n')
            bn += 115
            break
        else:
            minT = int(testStr[0:2])
            bn += max(int((118 - 2*minT)/2), 1)
            time.sleep(0.5)
        
    countRe += 1 
    
localtime = time.asctime( time.localtime(time.time()) )
print(localtime)
    
f.close()    