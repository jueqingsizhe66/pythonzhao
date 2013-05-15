
#Date: 2013年 05月 15日 星期三 19:52:48 CST
# Create an HTML chart of Unicode characters by codepoint
import sys
head = '<html><head><title>Unicode Code Points</title>\n' +\
    '<META HTTP-EQUIV="Content-Type" ' +\
        'CONTENT="text/html; charset=UTF-8">\n' +\
    '</head><body>\n<h1>Unicode Code Points</h1>'
foot = '</body></html>'
fp = sys.stdout#以显示屏为平台 进行显示
fp.write(head)#读取网页头部到字符显示屏！
num_blocks = 32 # Up to 256 in theory, but IE5.5 is flaky
#256为一个块间隔
for block in range(0,256*num_blocks,256): #256为一块 16为一行进行显示
    fp.write('\n\n<h2>Range %5d-%5d</h2>' % (block,block+256))
    start = unichr(block).encode('utf-16')
    fp.write('\n<pre> ')
    for col in range(16): fp.write(str(col).ljust(3))
    fp.write('</pre>')
    for offset in range(0,256,16):
        fp.write('\n<pre>')
        fp.write('+'+str(offset).rjust(3)+' ')
        line = ' '.join([unichr(n+block+offset) for n in range(16)])
#最关键的一行 unicode的codepoint由这三个组成 16进制的n 256进制的offset 256*num_blocks进制的block
        fp.write(line.encode('UTF-8')) #以UTF-8格式写入
        fp.write('</pre>')
fp.write(foot)
fp.close()

