"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

"""This is the simplest solution to the problem; I made no effort
to parse the HTML code.  Instead I just search for some key words.

An alternative would be to use the HTMLParser module:
http://docs.python.org/library/htmlparser.html

BUt I type it in 15:31 2013 by Zhao
"""

import urllib

zipcode = '02492'

url = 'http://uszip.com/zip/' + zipcode #uszip.com/zip/
conn = urllib.urlopen(url)

for line in conn.fp:  #not conn(fp) but conn.fp
    line = line.strip()
    if 'Population' in line: #not Population but 'Population'
        print line
    if 'Longitude' in line:
        print line
    if 'latitude' in line:
        print line

conn.close()

