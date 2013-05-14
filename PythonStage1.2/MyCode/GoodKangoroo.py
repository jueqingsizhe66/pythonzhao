#!/usr/bin/python
"""

This program is part of an exercise in
Think Python: An Introduction to Software Design
Allen B. Downey

This program explains and corrects a bug in BadKangaroo.py.
Before reading this, you should try to debug BadKangaroo.

"""

class Kangoroo():
    def __init__(self, contents = None):
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
#define the first item of t ,you can learn object.__str__(self)
#override the __str__ method,to export the better outcome
        t = [object.__str__(self) + ' with pouch contents:']
        for obj in self.pouch_contents:
            s = '   ' + object.__str__(obj) #des the obj's name
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)
#every list have the append method

kanga = Kangoroo()
roo = Kangoroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car')
kanga.put_in_pouch(roo)

print kanga
print ''

