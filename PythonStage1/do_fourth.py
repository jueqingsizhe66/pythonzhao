#!/usr/bin/python
# here you can learn what is flow execution
#do_twice("twice")  # if put here ,will generate the error msg
def print_twice(arg):
    print arg
    print arg



def do_fourth(arg):
    do_twice(arg)
    do_twice(arg)

def do_twice(arg):
    print_twice(arg)
print "now print the twice print~!"


do_twice("twice")

print "now print the Fourth print~!"
do_fourth("Fourth")
