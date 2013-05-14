in my opinion, the function call is just like the backreference in the regex

You know,function call is just like a detour in your program. Once the flow
of execution call your function, the first setup it will left a state to pick it up after the function have get its
end,and then execute the statement in the function ,finnaly exit and pick up the state before you entered the function,
    Python is good at keeping track of where it is ,so each time a function
    completes,the program picks up where it left off in the function that
    called it(the entrance of the function == the state),when it gets to the
    end of the program ,it terminates;

In general,you can think the programming in the python,just like the regex 
    working,you can think how to reduce the backreference, how to let the
    "regex" move efficiency? For reading convinience or executing easily,you
    should put ^ $ \b \Getc ,so it can be found easily ,sometimes you can 
    put the pos() and \G to execute it~! sometimes you can grasp the function
    where it is ,so you can pos() it,also it you can recognise what the 
    funtion name is ,so you can (?> name()) or name()+
#(?!) or(?=\b\B) 的效果类似与 break的效果
In [7]: do_four(do_twice,"hello")
hello
hello
hello
hello

In [3]: def do_fource(arg):
   ...:     do_twice(arg)
   ...:     do_twice(arg)

In [5]: def do_four(f,arg):
   ...:     f(arg)
   ...:     f(arg)
   ...:     
一样的结果不同的做法！ 下面更加体现着程序的简化
有点类似 $LevelN 
