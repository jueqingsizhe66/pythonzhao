#!-*-coding:utf8-*-
#Date: 2013年 05月 15日 星期三 21:53:09 CST

# Remove as many leading spaces as possible from whole block
from re import findall,sub
# What is the minimum line indentation of a block?
indent = lambda s: reduce(min,map(len,findall('(?m)^ *(?=\S)',s)))
# Remove the block-minimum indentation from each line?
flush_left = lambda s: sub('(?m)^ {%d}' % indent(s),'',s)
if __name__ == '__main__':
    import sys
    print flush_left(sys.stdin.read())


