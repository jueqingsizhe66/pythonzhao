from URLLister import URLLister
import urllib2
from FileRead import readFile

#!/usr/bin/python -W
#-*- coding = utf-8 -*-
# usock = urllib.urlopen("www.baidu.com")

parser = URLLister() # inside the class ,there are somelisten for all  <a> 
#parser.feed(usock.read())

#text = readFile("http://www.greenteapress.com/thinkpython/code/")

usock = urllib2.urlopen("http://www.greenteapress.com/thinkpython/code/")

parser.feed(usock.read())

usock.close()

for url in parser.urls:
    print url
