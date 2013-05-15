#!-*-author:zhaoliang-*-
#!-*-coding:utf8-*-
#Date: 2013年 05月 15日 星期三 22:00:50 CST

import re

text = "python re module contains match sub split findall search compiler,re.compiler is good for optimization"

print "#################################################"
print "re.match(pattern, string, flags)"
print "match experient!\n"
m = re.match(r'(\w+)\s',text)#only check on the front of the line
if m:
    print "find the match\n","m.group(0) is ",m.group(0),"\tm.group(1) is ",m.group(1),"\n"
else:
    print "Not matched.\n"


m = re.match(r'^py\w*\b',text)
print "几种查看match方式！！！ 适合re模块！\n"
print m,"\n","\tm.group()=",m.group(),"\tm.start() = ",m.start(),"\tm.end() =",m.end(),"\tm.groups()=",m.groups(),"\tm.groupdict() = ",m.groupdict(),"\n"



print "#################################################"
print " re.search(pattern, string, flags)"
print "search experient!\n" # in the string, find the first match string ,only first!

m = re.search(r'\scon(tain)s\s',text)
if m:
    print "find the match\n","m.group(0) is ",m.group(0),"\tm.group(1) is ",m.group(1)
else:
    print "Not matched.\n"



print "#################################################"
print "re.sub(pattern, repl, string, count=0, flags=0)"
print "sub experient!\n"

print re.sub(r'\s+','-',text),"\n"


print "#################################################"
print "re.split(pattern, string, maxsplit=0, flags=0)"
print "split experient!\n"

#print text

fia = re.split(r'\s*',text)
for i in fia:
    print i,"\t*-----*\t"

home = """Ross McFluff: 834.345.1254 155 Elm Street
Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way
Heather Albrecht: 548.326.4584 919 Park Place"""
#http://docs.python.org/2/library/re.html
entries = re.split(r'\n+',home)
print entries,"\n"

print "split with maxsplit = 3"
print "***************"
print [re.split(r':? ', entry, 3) for entry in entries]

print "split with maxsplit = 4"
print "***************"
print [re.split(r':? ', entry, 4) for entry in entries]


print "#################################################"
print "re.findall(pattern, string, flags=0)"
print "findall experient!\n"

fia = re.findall(r'\w*on\w*',text) # find the whole matches in the string!the all matches
for i in fia:
    print i,"\t"



print "#################################################"
print " re.compile(pattern)"
print "compile experient!\n"

regex = re.compile(r'\w*on\w*')
print regex.findall(text) 
print regex.sub(lambda m:'[' + m.group(0) + ']',text) # if the word include on ,put the [] around the match word

print "#################################################"
print " re.finditer(pattern, string, flags=0)¶"
print "finditer experient!\n"
text = "He was carefully disguised but captured quickly by police."
for m in re.finditer(r"\w+ly", text):
     print '%02d-%02d: %s' % (m.start(), m.end(), m.group(0))



print "+-----------------------------------------------------------------+"
print "|Describe:compile的作用是把re模块中的第一个参数给一个对象的形式来表|||达然后再用这个参数|对象来引用re模块中的函数！sub函数的第二个参数是准备替换的单词（就是目的字符串） 第三个是元字符串，这是需要区分清楚的！|\n"
print "+-----------------------------------------------------------------+"
print "+-----------------------------------------------------------------+"
print "|Describe:compile的作用是把re模块中的第一个参数给一个对象的形式来表|||达然后再用这个参数|对象来引用re模块中的函数！sub函数的第二个参数是准备替换的单词（就是目的字符串） 第三个是元字符串，这是需要区分清楚的！|\n"
print "+-----------------------------------------------------------------+"
