#generator 一个值得的～   一个子弹一个子弹的装！ 
In [11]: def counter(Max):
   ....:     i = 0
   ....:     while i < Max:
   ....:         val = (yield i)
   ....:         if val is not None:
   ....:             i = val
   ....:         else:
   ....:             i += 1
   ....:             
   ....:             

In [12]: counter(8)
Out[12]: <generator object counter at 0xa6f8874>

In [13]: g = counter(8)

In [14]: for i in g:
   ....:     print i,
   ....:     
   ....:     
0 1 2 3 4 5 6 7

In [15]: for i in g:
    print i,
######################send()
In [17]: g = counter(8)

In [18]: g.next()
Out[18]: 0

In [19]: g.send(4)
Out[19]: 4

In [20]: g.next()
Out[20]: 5

################butlt-in map() filter()
Two of Python’s built-in functions, map() and filter(), are somewhat obsolete; they duplicate the features of list comprehensions but return actual lists instead of iterators.

map(f, iterA, iterB, ...) returns a list containing f(iterA[0], iterB[0]), f(iterA[1], iterB[1]), f(iterA[2], iterB[2]), ...

In [21]: def upper(s):
   ....:     return s.upper()
   ....: 

In [22]: map(upper,['sentense','fragment']
   ....: 
   ....: )
Out[22]: ['SENTENSE', 'FRAGMENT']
In [25]: [upper(s) for s in ['sentense','fragment']]
Out[25]: ['SENTENSE', 'FRAGMENT']


filter(predicate, iter) returns a list that contains all the sequence elements that meet a certain condition, and is similarly duplicated by list comprehensions. A predicate is a function that returns the truth value of some condition; for use with filter(), the predicate must take a single value.

In [26]: def iseven(x):
   ....:     return (x%2) == 0
   ....: 

In [27]: filter(iseven, range(19))
Out[27]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

###############list comprehension
In [28]: [x for x in range(19) if iseven(x)]
Out[28]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

reduce()的执行过程：
reduce() takes the first two elements A and B returned by the iterator and calculates func(A, B).
        It then requests the third element, C, calculates func(func(A, B), C), combines this result with the fourth element returned, and continues until the iterable is exhausted.
        If the iterable returns no values at all, a TypeError exception is raised.
        If the initial value is supplied, it’s used as a starting point and func(initial_value, A) is the first calculation.
In [31]: reduce(operator.mul,[1,2,3],4)
Out[31]: 24
4*1*2*3
In [32]: reduce(operator.mul,[1,2,3],1)
Out[32]: 6
1*1*2*3

If you use operator.add() with reduce(), you’ll add up all the elements of the iterable. This case is so common that there’s a special built-in called sum() to compute it:
>>>

>>> reduce(operator.add, [1,2,3,4], 0)
10
>>> sum([1,2,3,4])
10

# Instead of:
product = reduce(operator.mul, [1,2,3], 1)

# You can write:
#内部执行过程！
product = 1
for i in [1,2,3]:
    product *= i

>>> for item in enumerate(['subject', 'verb', 'object']):
...     print item
(0, 'subject')
(1, 'verb')
(2, 'object')

a = 1
In [36]: for i in ['subjec','verb','object']:
    print (a,i)
   ....:     a = a+1
   ....:     
   ....:     
(1, 'subjec')
(2, 'verb')
(3, 'object')

In [8]: lowercase = lambda x:x.lower()

In [9]: print_assign = lambda name,value:name + '=' +str(value)

In [10]: print_assign('zhao',23)
Out[10]: 'zhao=23'

In [12]: lowercase('JFS')
Out[12]: 'jfs'

像lambda这种形式的编程 被我称为口袋似编程 特别实用  这就是lisp的优势

In [13]: adder = lambda x,y:x+y

In [14]: adder(3,5)
Out[14]: 8


lambda 其实用对象来表示的话叫做lambda口袋式表达式！
lambda 返回的就是return的后面！ 就是函数的返回值
#####################python's shortcircute
In [23]: pr = lambda x: x

In [24]: (x==1 and pr ('one')) or (x == 2 and pr ('two')) or (pr('other'))
Out[24]: 'one'
In [26]: name = lambda x:(x == 1 and pr('one')) or (x == 2 and pr('two')) or \
   ....: (pr ('other'))

In [27]: 

In [28]: name(3)
Out[28]: 'other'

In [29]: name(2)
Out[29]: 'two'

An alternative is to just use the def statement and define a function in the usual way:

def lowercase(x):
    return x.lower()

def print_assign(name, value):
    return name + '=' + str(value)

def adder(x,y):
    return x + y


Which alternative is preferable? That’s a style question; my usual course is to avoid using lambda.

One reason for my preference is that lambda is quite limited in the functions it can define. The result has to be computable as a single expression, which means you can’t have multiway if... elif... else comparisons or try... except statements. If you try to do too much in a lambda statement, you’ll end up with an overly complicated expression that’s hard to read. Quick, what’s the following code doing?

total = reduce(lambda a, b: (0, a[1] + b[1]), items)[1]


###############到底该选择 
##什么来实现  还真是是好的 问题！

reduce(function, iterable[, initializer])
#http://docs.python.org/2/library/functions.html#reduce
Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
reduce 用一个公式来解释 ((((((((()))))))))无穷多个()运用相同的函数进行二元累加 最后把一个list and friends 削成一个value
#*#相当关键的一句话 ；
---------
--The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable-
这句话讲述了编译器的执行过程！
If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned. Roughly equivalent to:
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value
基本上如果理解了上面的话  就基本上明白了reduce的执行过程！相信我没错的！

In [64]: print reversed(a)
<listreverseiterator object at 0x899edac>

In [65]: for i in reversed(a):
   ....:     print i,
   ....:     
   ....:     
3 6 5 2
从上式可以知道reversed()也是返回一个iterator


In [67]: sorted(reversed(a))
Out[67]: [2, 3, 5, 6]

In [69]: type(sorted(reversed(a)))
Out[69]: <type 'list'>
sorted则不是 而是直接返回值 所以他不是一个iterator


###插入两个decorator:classmethod and staticmethod
#印象我记得两个不同点  receive  and not receive implicit first argument
 classmethod(function)

    Return a class method for function.

    A class method receives the class as implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom:

    class C(object):
        @classmethod
        def f(cls, arg1, arg2, ...):


 staticmethod(function)

    Return a static method for function.

    A static method does not receive an implicit first argument. To declare a static method, use this idiom:

    class C(object):
        @staticmethod
        def f(arg1, arg2, ...):


In [3]: for i in itertools.repeat(5,5):
   ...:     print i,
   ...:     
   ...:     
5 5 5 5 5

In [5]: for i in itertools.repeat([2,5],5):
    print i,
   ...:     
   ...:     
[2, 5] [2, 5] [2, 5] [2, 5] [2, 5]

In [7]: itertools.chain([1,5,3,5],('df','fdfg','fd'))
Out[7]: <itertools.chain object at 0x958d68c>

In [8]: tuple(itertools.chain([1,5,3,5],('df','fdfg','fd')))
Out[8]: (1, 5, 3, 5, 'df', 'fdfg', 'fd')

In [10]: tuple([1,5,3,6],('df','fdf','fd'))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/xinran/<ipython console> in <module>()

TypeError: tuple() takes at most 1 argument (2 given)

用这个chain函数联合起来！


#####方便快捷的产生dict的方法！  利用zip方法！！ itertools模块提供的！
In [12]: itertools.izip(['a','b','c'],(1,2,3))
Out[12]: <itertools.izip object at 0x95a17ec>

In [13]: a = it
iter       itertools  

In [13]: a = itertools.izip(['a','b','c'],(1,2,3))

In [14]: a
Out[14]: <itertools.izip object at 0x95a1a6c>

In [15]: b = dict(a)

In [16]: b
Out[16]: {'a': 1, 'b': 2, 'c': 3}


####内建函数也是可以轻松办到的！！！
In [17]: zip(['a','f','c'],(1,2,3))
Out[17]: [('a', 1), ('f', 2), ('c', 3)]

In [18]: dict(zip(['a','f','c'],(1,2,3)))
Out[18]: {'a': 1, 'c': 3, 'f': 2}

It’s similar to the built-in zip() function, but doesn’t construct an in-memory list and exhaust all the input iterators before returning; instead tuples are constructed and returned only if they’re requested. (The technical term for this behaviour is lazy evaluation.)

This iterator is intended to be used with iterables that are all of the same length. If the iterables are of different lengths, the resulting stream will be the same length as the shortest iterable.
上面这段话想说明白的是  如果两个序列不一样长的话 python该怎么办 肯定是最短原则！o

itertools.islice(iter, [start], stop, [step]) returns a stream that’s a slice of the iterator. With a single stop argument, it will return the first stop elements. If you supply a starting index, you’ll get stop-start elements, and if you supply a value for step, elements will be skipped accordingly. Unlike Python’s string and list slicing, you can’t use negative values for start, stop, or step.

itertools.islice(range(10), 8) =>
  0, 1, 2, 3, 4, 5, 6, 7
itertools.islice(range(10), 2, 8) =>
  2, 3, 4, 5, 6, 7
itertools.islice(range(10), 2, 8, 2) =>
  2, 4, 6
In [23]: list(itertools.islice(range(10),2,8))
Out[23]: [2, 3, 4, 5, 6, 7]

In [24]: list(itertools.islice(range(10),2,8,))
Out[24]: [2, 3, 4, 5, 6, 7]

In [25]: list(itertools.islice(range(10),2,8,2))
Out[25]: [2, 4, 6]

In [21]: list(itertools.islice(range(10),8))
Out[21]: [0, 1, 2, 3, 4, 5, 6, 7]

wo functions are used for calling other functions on the contents of an iterable.

itertools.imap(f, iterA, iterB, ...) returns a stream containing f(iterA[0], iterB[0]), f(iterA[1], iterB[1]), f(iterA[2], iterB[2]), ...:

itertools.imap(operator.add, [5, 6, 5], [1, 2, 3]) =>
  6, 8, 8
The operator module contains a set of functions corresponding to Python’s operators. Some examples are operator.add(a, b) (adds two values), operator.ne(a, b) (same as a!=b), and operator.attrgetter('id') (returns a callable that fetches the "id" attribute).

itertools.starmap(func, iter) assumes that the iterable will return a stream of tuples, and calls f() using these tuples as the arguments

#之所以写上上面这两段是因为 我想让自己拓充一下operator的知识面！ 还有就是引入另一个itertools工具 starmap(func,iter)

In [27]: import operator

In [28]: itertools.imap(operator.add,[2,5,2],[72,4,5])
Out[28]: <itertools.imap object at 0x95a1e8c>

In [29]: list(itertools.imap(operator.add,[2,5,2],[72,4,5]))
Out[29]: [74, 9, 7]

In [30]: itertools.starmap(os.path.join,[('/usr','bin','java'),\
   ....: ('usr','bin','perl'),('usr','bin','python')])
Out[30]: <itertools.starmap object at 0x95c4a0c>

In [31]: list(itertools.starmap(os.path.join,[('/usr','bin','java'),\
('usr','bin','perl'),('usr','bin','python')]))
Out[32]: ['/usr/bin/java', 'usr/bin/perl', 'usr/bin/python']
#写上上面这段的目的是 居然还可已从字符串直接生成目录路径 
Selecting elements

Another group of functions chooses a subset of an iterator’s elements based on a predicate.

itertools.ifilter(predicate, iter) returns all the elements for which the predicate returns true:

def is_even(x):
    return (x % 2) == 0

itertools.ifilter(is_even, itertools.count()) =>
  0, 2, 4, 6, 8, 10, 12, 14, ...

itertools.ifilterfalse(predicate, iter) is the opposite, returning all elements for which the predicate returns false:

itertools.ifilterfalse(is_even, itertools.count()) =>
  1, 3, 5, 7, 9, 11, 13, 15, ...

###很难的一个操作

Grouping elements¶

The last function I’ll discuss, itertools.groupby(iter, key_func=None), is the most complicated. key_func(elem) is a function that can compute a key value for each element returned by the iterable. If you don’t supply a key function, the key is simply each element itself.

groupby() collects all the consecutive elements from the underlying iterable that have the same key value, and returns a stream of 2-tuples containing a key value and an iterator for the elements with that key.

city_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'),
             ('Anchorage', 'AK'), ('Nome', 'AK'),
             ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ'),
             ...
            ]

def get_state ((city, state)):
    return state

itertools.groupby(city_list, get_state) =>
  ('AL', iterator-1),
  ('AK', iterator-2),
  ('AZ', iterator-3), ...

where
iterator-1 =>
  ('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL')
iterator-2 =>
  ('Anchorage', 'AK'), ('Nome', 'AK')
iterator-3 =>
  ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')

groupby() assumes that the underlying iterable’s contents will already be sorted based on the key. Note that the returned iterators also use the underlying iterable, so you have to consume the results of iterator-1 before requesting iterator-2 and its corresponding key.


#一个高级函数 A higher-order function = functools.partial()
The constructor for partial takes the arguments (function, arg1, arg2, ... kwarg1=value1, kwarg2=value2). The resulting object is callable, so you can just call it to invoke function with the filled-in arguments.
之所以写上上面这段话是想说明白他的语法！
In [65]: def log(message, subsytem):
    "Write the contesn"
    print '%s, %s' % (subsytem, message)
   ....:     
   ....:     

In [68]: server_log = functools.partial(log,subsytem = 'server')

In [69]: server_log('Unable to open socket')
server, Unable to open socket

你可以看到partial的作用相当与是预输上了一些需要的固定的参数  而把那些变化的需要用户自己再去更改的函数
留给我们经过partial之后的函数 这相当于节约了用户输入的效率！！！！！！


The operator module¶

The operator module was mentioned earlier. It contains a set of functions corresponding to Python’s operators. These functions are often useful in functional-style code because they save you from writing trivial functions that perform a single operation.

Some of the functions in this module are:

    Math operations: add(), sub(), mul(), div(), floordiv(), abs(), ...
    Logical operations: not_(), truth().
    Bitwise operations: and_(), or_(), invert().
    Comparisons: eq(), ne(), lt(), le(), gt(), and ge().
    Object identity: is_(), is_not().

Consult the operator module’s documentation for a complete list.

#之所以把这段话也给贴上去是因为 我想着是不是该再深入地学习一下operator模块所包含的一些玩意！o

In computer science, functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids state and mutable data. It emphasizes the application of functions, in contrast to the imperative programming style, which emphasizes changes in In computer science, functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids state and mutable data. It emphasizes the application of functions, in contrast to the imperative programming style, which emphasizes changes in state.[state.[
    这段话我摘自http://en.wikipedia.org/wiki/Functional_programming 为什么我要copy他呢？ 原因在于 这边有两个两avoid
    state and mutable data and emphasizes changes in state
    两种对立面需要我们去了解.还有说明了他更像一些数学公式的形式！！也就是更加的原始！
Higher-order functions are functions that can either take other functions as arguments or return them as results. In calculus, an example of a higher-order function is the differential operator d/dx, which returns the derivative of a function f.
#之所以我摘下这段是因为 他略微解释了higher-order functions 利用微积分！
Higher-order functions are closely related to first-class functions in that higher-order functions and first-class functions both allow functions as arguments and results of other functions. The distinction between the two is subtle: "higher-order" describes a mathematical concept of functions that operate on other functions, while "first-class" is a computer science term that describes programming language entities that have no restriction on their use (thus first-class functions can appear anywhere in the program that other first-class entities like numbers can, including as arguments to other functions and as their return values).
    也就是说Higher-order functions 更接近与自然语言的形式 相当于我们代数中用的 f(g())之类的函数也是当作参数！
    或者说叫做复合函数！ 而不叫做递归函数！

Recursion
Main article: Recursion (computer science)

Iteration (looping) in functional languages is usually accomplished via recursion. Recursive functions invoke themselves, allowing an operation to be performed over and over until the base case is reached. Though some recursion requires maintaining a stack, tail recursion can be recognized and optimized by a compiler into the same code used to implement iteration in imperative languages
#讲述了recursive 在functional中就好象是Iteration

In [75]: print len([2+1, 3*2, 1/5, 5-4])
4

###灰不垃圾居然还可以这样！
# Fibonacci numbers, imperative style
def fibonacci(iterations):
    first, second = 0, 1  # seed values
    for i in range(iterations - 1):  # Perform the operation iterations - 1 times.
        theSum, first, second = first + second, second, theSum  # Assign all the new values.
    return first  # Return the value when done.
