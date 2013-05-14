
IPython 替代 Python Shell

在学习 Python 的时候应该都接触过 Python 的 Shell，能够输入 Python 语句并且立即返回结果。而 IPython就是一个豪华加强版的 Python Shell。如果你安装了 Python(x, y) 的话，那 IPython 已经在你的机器上了。如果没有的话那么请在这里下载 Windows Installer 进行安装。在安装这个之后还需要安装 pyreadline 让 IPython 开启高亮和自动补全功能。

之后你在命令行下需要 python 的时候改为输入 ipython就能使用它了。开启 IPython 看看，首先感觉的不同应该是这个是有颜色的。我们来看看它提供的一些基础而实用的功能吧。首先是自动补全，一种是简单的关键字补全，另外一种是对象的方法和属性补全。作为例子，我们先引入 sys模块，之后再输入 sys.(注意有个点)，此时按下 tab 键，IPython 会列出所有 sys 模块下的方法和属性。因为是在互动模式下进行的，此时的 Python 语句实实在在的被执行了，所以对普通 object 的补全也是很完好的。

IPython

接着上面的例子，我们输入 sys?，这样会显示出 sys模块的 docstring及相关信息。很多时候这个也是很方便的功能。

IPython 另外还有很多方便的功能，可以自己参阅文档来发掘。这里另外介绍一个很神奇的功能。如果你的程序是由命令行开始执行的，即在命令行下输入
python foo.py（大部分 Python 程序都是），那么你还可以利用 IPython 在你的程序任意地方进行断点调试！在你程序中任意地方，加入如下语句：


from IPython.Shell import IPShellEmbed  IPShellEmbed([])()  

再和平常一样运行你的程序，你会发现在程序运行到插入语句的地方时，会转到 IPython 环境下。你可以试试运行些指令，就会发现此刻 IPython 的环境就是在程序的那个位置。你可以逐个浏览当前状态下的各个变量，调用各种函数，输出你感兴趣的值来帮助调试。之后你可以照常退出 IPython，然后程序会继续运行下去，自然地你在当时 IPython 下执行的语句也会对程序接下来的运行造成影响。

 

这个方法我是在这里看到的。想象一下，这样做就像让高速运转的程序暂停下来，你再对运行中的程序进行检查和修改，之后再让他继续运行下去。这里举一个例子，比如编写网页 bot ，你在每取回一个页面后你都得看看它的内容，再尝试如何处理他获得下一个页面的地址。运用这个技巧，你可以在取回页面后让程序中断，再那里实验各种处理方法，在找到正确的处理方式后写回到你的代码中，再进行下一步。这种工作流程只有像 Python 这种动态语言才可以做到。
ipython与Linux的完美结合

　　当然Ipython最NB的地方在于和Linux系统的无缝连接，简单介绍一下在Ubuntu下的使用，首先需要安装Ipython:

　　root@3414-mainsrv:~# sudo apt-get install ipython

　　接着就可以在终端下使用了，有个一个称为是magic的函数：

In [1]: magic

IPython's 'magic' functions
===========================

The magic function system provides a series of functions which allow you to
control the behavior of IPython itself, plus a lot of system-type
features. All these functions are prefixed with a % character, but parameters
are given without parentheses or quotes.

NOTE: If you have 'automagic' enabled (via the command line option or with the
%automagic function), you don't need to type in the % explicitly. By default,
IPython ships with automagic on, so you should only rarely need the % escape.

Example: typing '%cd mydir' (without the quotes) changes you working directory
to 'mydir', if it exists.

You can define your own magic functions to extend the system. See the supplied
ipythonrc and example-magic.py files for details (in your ipython
configuration directory, typically $HOME/.ipython/).

You can also define your own aliased names for magic functions. In your
ipythonrc file, placing a line like:

execute __IPYTHON__.magic_pf = __IPYTHON__.magic_profile

will define %pf as a new name for %profile.

You can also call magics in code using the ipmagic() function, which IPython
automatically adds to the builtin namespace. Type 'ipmagic?' for details.

For a list of the available magic functions, use %lsmagic. For a description
of any of them, type %magic_name?, e.g. '%cd?'.

 

　　我们来举个例子把，例如有一个称为是bg的魔法函数，它的作用是用来在后台进行计算，我们需要计算一下2的10次方，只需要按下面输入即可交给bg函数把计算丢到后台去计算而不影响你的继续操作，你只要记得job的序号是1，需要结果时，只要把jobs[1]中的result输出就可以了

In [10]: bg pow(2,10)
Starting job # 1 in a separate thread.

In [11]: print jobs[1].result
1024

　　此外，使用rehash函数，你完成可以把ipython当做是shell使用，你可以使用任何命令，例如:

In [15]: ps aux|grep DarwinStreamingSrvr
root 17496 0.0 0.0 2040 508 pts/0 S+ 10:12 0:00 sh -c ps aux|grep DarwinStreamingSrvr
root 17498 0.0 0.0 7368 852 pts/0 S+ 10:12 0:00 grep DarwinStreamingSrvr
