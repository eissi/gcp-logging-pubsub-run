#!/usr/bin/env python

import signal
import time
import os
def alarm_handler(signum, stack):
    print('Alarm at:', time.ctime())
    exit(0) 

dur=os.environ.get("TIME_TO_RUN_IN_MINUTE")
if dur is None:
    dur = 3
else:
    dur = int(dur)
print("running duration: {0} at {1}".format(dur,time.ctime()))

signal.signal(signal.SIGALRM, alarm_handler)  # assign alarm_handler to SIGALARM
signal.alarm(dur*60)  # set alarm after 4 seconds

i=0
while True:
    #print('Current time:', time.ctime())
    print(i)
    i+=1
    #time.sleep(1)  # make sufficient delay for the alarm to happen
