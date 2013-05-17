#!/usr/bin/python -w
import re
import time
import fpformat

Regex1 = re.compile("^(a|b|c|d|e|f|g)+$");
Regex2 = re.compile("^[abcdefg]+$");

TimesToDo = 1250;
TestString = "abababdedfg"*800;
#for i in range(800): TestString +="abababdefg"
StartTime = time.time()
for i in range(TimesToDo):
    Regex1.search(TestString)
Seconds = time.time() - StartTime
print "Alternation takes "+ fpformat.fix(Seconds,3) + "seconds\n"

StartTime = time.time()
for i in range(TimesToDo):
    Regex2.search(TestString)
Seconds = time.time() - StartTime
print "Character class takes "+ fpformat.fix(Seconds,3) + "seconds\n"

