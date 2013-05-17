#!/usr/bin/python -w
import time
import fpformat


TimesToDo = 1250;
nums = (1,2,3,4)*1000
#for i in range(800): TestString +="abababdefg"
str_num = []
StartTime = time.time()
for i in range(TimesToDo):
    for n in nums:
        str_num.append(str(n)) #the sama formulate a list
Seconds = time.time() - StartTime
print "for takes "+ fpformat.fix(Seconds,16) + "seconds\n"

StartTime = time.time()
for i in range(TimesToDo):
    str_num = map(str,nums)  #map into a list
Seconds = time.time() - StartTime
print "Map loops takes "+ fpformat.fix(Seconds,16) + "seconds\n"

