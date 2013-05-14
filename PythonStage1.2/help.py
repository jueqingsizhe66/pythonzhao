help(tuple) and find the __hash__ and __iter__
In [18]: hash(y)
Out[18]: -1452785839

In [19]: x = iter(y)

In [20]: for i in x:
   ....:     print i
   ....:     
   ....:     
2
5
6
3

