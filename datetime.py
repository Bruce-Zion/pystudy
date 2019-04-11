from datetime import datetime




now=datetime.now()
now.second() #int



import time
time.ctime() #string
time.sleep(5)


import time, datetime

startTime = datetime.datetime(2016, 6, 8, 16, 45, 0)
print('Program not starting yet...')
while datetime.datetime.now() < startTime:
    time.sleep(1)
print('Program now starts on %s' % startTime)
print('Executing...')


from datetime import datetime, timedelta
now = datetime.now()

datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
now + timedelta(hours=10)
datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
now - timedelta(days=1)
datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
now + timedelta(days=2, hours=12, seconds=37)
datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)