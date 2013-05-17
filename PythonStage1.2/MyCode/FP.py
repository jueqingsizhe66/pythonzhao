#!-*-author:zhaoliang-*-
#!-*-coding:utf8-*-
#Date: 2013年 05月 16日 星期四 21:36:28 CST
#From:http://docs.python.org/2/howto/functional.html
1:I think FP is good ,so I study it
2:how good?
3:proof :my little map compare with for
    
4:Do it

 4.1:an important foundation for writing functional-style programs: iterators;What is iterator?--->
    An iterator is an object representing a stream of data; this object returns the data one element at a time
How to generate iterator?----->
The built-in iter() function takes an arbitrary object and tries to return an iterator that will return the object’s contents or elements, raising TypeError if the object doesn’t support iteration.
**********************************************************
In [2]: L
Out[2]: [1, 2, 3]

In [3]: type(L)
Out[3]: <type 'list'>

In [4]: it = iter(L)

In [5]: type(it)
Out[5]: <type 'listiterator'>

In [6]: L = (1,3,5)

In [7]: it = iter(L)

In [8]: type(it)
Out[8]: <type 'tupleiterator'>
In [9]: it.next()
Out[9]: 1

In [10]: it.next()
Out[10]: 3

In [11]: it.next()
Out[11]: 5

In [12]: it.next()
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)

/home/xinran/<ipython console> in <module>()

StopIteration:

Python expects iterable objects in several different contexts, the most important being the for statement. In the statement for X in Y, Y must be an iterator or some object for which iter() can create an iterator. 

In [21]: it = iter([5,6,7])

In [22]: for i in it:
   ....:     print i,
   ....:     
   ....:     
5 6 7
????????????????????????????how to resize the iter position!!
I think [iter] as 单向链
 不是有list  dict  tuple 还需要他干嘛 因为他天生支持next()
 虽然他们几个都可以用for循环  单向链如果当他到头的话就出来了！无法
 继续next()

In [40]: max(L)
Out[40]: 12

In [41]: min(L)
Out[41]: 3
In [42]: L = [1,3,6]

In [43]: max(L)
Out[43]: 6
####################################################
    Note that you can only go forward in an iterator; there’s no way to get the previous element, reset the iterator, or make a copy of it.
    the iterator protocol only specifies the next() method. Functions may therefore consume all of the iterator’s output, and if you need to do something different with the same stream, you’ll have to create a new iterator
    也就是说iter就是一串子弹 打完了就得换子弹夹；
##################iter()的多种运用场所
We’ve already seen how lists and tuples support iterators. In fact, any Python sequence type, such as strings, will automatically support creation of an iterator.

Calling iter() on a dictionary returns an iterator that will loop over the dictionary’s keys

In [47]: m = {'jan':1, 'Feb':2, 'March':3, 'April':4, 'May':5, 'June':6}

In [48]: for key in m:
    print key,m[key]
   ....:     
   ....:     
March 3 #恨随意的顺序 the order of print is random,because it’s based on the hash ordering of the objects in the dictionary
May 5
June 6
jan 1
April 4
Feb 2

Applying iter() to a dictionary always loops over the keys, but dictionaries have methods that return other iterators. If you want to iterate over keys, values, or key/value pairs, you can explicitly call the iterkeys(), itervalues(), or iteritems() methods to get an appropriate iterator
1:iterkeys()
2:itervalues()
3:iteritems()
o#####其实iter就是FP函数式编程  指向一个方向发展

L  = iter(m) === dict.iterkeys(m) #前提m是一个dict类型
L = dict.itervalues(m)
L = dict.iteritems(m)

In [63]: for i in L:
    print i
   ....:     
   ....:     
('May', 5)
('June', 6)
('jan', 1)
('April', 4)
('Feb', 2)
都一样的特点 不支持L[i]的形式  否则报错  都变为了tuple的形式输出了，当输出完一遍iter之后就没用了  无法回收就像一次性筷子


**********************************************************

[Generator expressions] and  [list comprehensions]
line_list = ['  line 1\n', 'line 2  \n', ...]
形式是 ：( for  in   if) == generator
        [for in if] == list

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]
In [79]: type(stripped_list)
Out[79]: <type 'list'>

In [80]: type(stripped_iter)
Out[80]: <type 'generator'>

stripped_list = [line.strip() for line in line_list
                 if line != ""]

With a list comprehension, you get back a Python list; stripped_list is a list containing the resulting lines, not an iterator. Generator expressions return an iterator that computes the values as necessary, not needing to materialize all the values at once. This means that list comprehensions aren’t useful if you’re working with iterators that return an infinite stream or a very large amount of data. Generator expressions are preferable in these situations.
##也就是说iterator不包含现成结果？还是什么   还有iter是一次流
Generator expressions are surrounded by parentheses (“()”) and list comprehensions are surrounded by square brackets (“[]”). Generator expressions have the form:

( expression for expr in sequence1
             if condition1
             for expr2 in sequence2
             if condition2
             for expr3 in sequence3 ...
             if condition3
             for exprN in sequenceN
             if conditionN )
The elements of the generated output will be the successive values of expression. The if clauses are all optional; if present, expression is only evaluated and added to the result when condition is true.

#错误的形式！ 少了() 或者[]
In [81]: stripped_iter = line.strip() for line in line_list
------------------------------------------------------------
   File "<ipython console>", line 1
     stripped_iter = line.strip() for line in line_list
                                    ^
SyntaxError: invalid syntax

Generator expressions always have to be written inside parentheses, but the parentheses signalling a function call also count. If you want to create an iterator that will be immediately passed to a function you can write:

obj_total = sum(obj.count for obj in list_all_objects())

The for...in clauses contain the sequences to be iterated over. The sequences do not have to be the same length, because they are iterated over from left to right, not in parallel. For each element in sequence1, sequence2 is looped over from the beginning. sequence3 is then looped over for each resulting pair of elements from sequence1 and sequence2.

To put it another way, a list comprehension or generator expression is equivalent to the following Python code:

#generator or list comprehension 的python替代形式！
for expr1 in sequence1:
    if not (condition1):
        continue   # Skip this element
    for expr2 in sequence2:
        if not (condition2):
            continue    # Skip this element
        ...
        for exprN in sequenceN:
             if not (conditionN):
                 continue   # Skip this element

             # Output the value of
             # the expression.

In [82]: seq1 = 'abc'

In [83]: seq2 = [2,3,5]

In [84]: [(x,y) for x in seq1 for y in seq2]
Out[84]: 
[('a', 2),
 ('a', 3),
 ('a', 5),
 ('b', 2),
 ('b', 3),
 ('b', 5),
 ('c', 2),
 ('c', 3),
 ('c', 5)]


# 你可以看到由于使用了generator or list comperation省略了好多的if
To avoid introducing an ambiguity into Python’s grammar, if expression is creating a tuple, it must be surrounded with parentheses. The first list comprehension below is a syntax error, while the second one is correct:

# Syntax error
[ x,y for x in seq1 for y in seq2]
# Correct
[ (x,y) for x in seq1 for y in seq2]



Generators的来源：
You’re doubtless familiar with how regular function calls work in Python or C. When you call a function, it gets a private namespace where its local variables are created. When the function reaches a return statement, the local variables are destroyed and the value is returned to the caller. A later call to the same function creates a new private namespace and a fresh set of local variables. But, what if the local variables weren’t thrown away on exiting a function? What if you could later resume the function where it left off? This is what generators provide; they can be thought of as resumable functions.

Here’s the simplest example of a generator function:

def generate_ints(N):
    for i in range(N):
        yield i

When you call a generator function, it doesn’t return a single value; instead it returns a generator object that supports the iterator protocol. On executing the yield expression, the generator outputs the value of i, similar to a return statement. The big difference between yield and a return statement is that on reaching a yield the generator’s state of execution is suspended and local variables are preserved. On the next call to the generator’s .next() method, the function will resume executing.

In [85]: def generate_list(N):
   ....:     for i in range(N):
   ....:        yield i
   ....:        
   ....:        

In [86]: generate_list(3)
Out[86]: <generator object generate_list at 0xa6ab4b4>

In [87]: gen = generate_list(6)

In [88]: gen.next()
Out[88]: 0

In [89]: gen.next()
Out[89]: 1

In [90]: for i in gen:
   ....:     print i
   ....:     
   ....:     
2
3
4
5
上面证明了 这个函数的返回值的确是一个iterator 也是一次性使用的
