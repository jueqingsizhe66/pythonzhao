#!/usr/bin/python
#-*-coding:utf8 -*-
# python当中是不能用for(int i = 0; i< times; i++
def printplusmins(times):
    print "+", #comma的作用是防止换行！
    for i in range(0,times):
        print "-",
    print "+",
    for i in range(0,times):
        print "-",
    print "+"

def printPine(times):
    print "|",
    for i in range(0,times):
        print " ",
    print "|",
    for i in range(0,times):
        print " ",
    print "|"

def printTimesPine(f,ok): 
    for i in range(0,ok):
        f(5);
printplusmins(5)
printTimesPine(printPine,4)
printplusmins(5)
printTimesPine(printPine,4)
printplusmins(5)
