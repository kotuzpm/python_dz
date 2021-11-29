import datetime
from datetime import time

today9am = datetime.time(9,00,00)
today19pm = datetime.time(19,00,00)

log = open('/home/serg/Python_Dev/logs/auth.log.1')
for line in log:
    data= line.split()
    time = data[0] + ' ' + data[1]+ ' ' + data[2]
    tw = data[2]
    worktime = datetime.time(int(tw[0:2]), int(tw[3:5]), int(tw[6:8]))
    host = data[3]
    if today9am > worktime and today19pm > worktime:
        cmd = line[line.find('session opened for'): -1]
        if cmd is not '':
            print(time, host, cmd)
