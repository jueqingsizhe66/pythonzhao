编码问题

作为中文用户，初学 Python 最容易碰到的问题估计就是编码问题了。明明英文的都可以用到中文的时候就要出问题，而且出错信息难以理解，想要解决问题又不知道从何开始。幸运的是编码问题通过预防性的措施是很好避免的。下面从几个方面来讲讲 Python 中处理中文及 Unicode 容易碰到的问题。
Unicode 编码基础

这里非常简单的讲一下编码知识，此部分表述可能不太准确，如果你对 Unicode 更为了解的话请联系我帮忙纠正。

你可以想象 Unicode 是一个很大的表，里面有着世界上所有的文字的个体，如英文中的字母，中文的汉字。事实上 Unicode 标准中每一个字都有一个唯一对应的编号，好比说 '中'字 对应十六进制 0x4E2D，而字母 'a' 对应的是十六进制 0x0061。这个编号是由 Unicode Consortium 这个组织来确定的。 如果说用这个编码来对应字符来用于表示字符，理论上是可以的，这样的话就是每一个数字编号能对应一个字符。

而实际情况中，不是每篇文章都用得到世界上所有的字符。譬如一篇英文文章就只有英文字母加上一些符号，用 Unicode 来进行存储的话每个字符要浪费太多的空间。所以就有各种类型的编码产生。编码我们这里可以理解就是将一部分的 Unicode (比如说所有的中文，或者所有的日文)字符，以某种方式确定另外一个符号来代表他。中文常用编码有 UTF8 和 GBK，仍然以 '中'字 为例， UTF8 编码将对应 '中'字 的 Unicode 编号 0x4E2D拆成三个的编号的组合，[0xE4, 0xB8, 0xAD]，只有这几个连在一起的时候才会被作为一个 '中'字 显示出来；作为对比，GBK 编码将 '中'字 对应的 Unicode 编号 0x4E2D编码成为两个编号的组合
[0xD6, 0xD0]，在 GBK 编码环境下只有这两个编号一起时，才会显示为 '中'字。

上面的例子中，如果把 UTF8 编码后的 [0xE4, 0xB8, 0xAD]放到 GBK 环境下来显示会怎样？这几个编号跟 '中'字 在 GBK 下的编码 [0xD6, 0xD0]
，不同，则显然不会显示为 '中'字。这三个字符会跟排在其前后的字符一起，按照 GBK 的编码规则找有没有对应的字符。结果有可能显示出一个毫不相关的字符，有时候为符号或者干脆不显示，这种情况就算产生了乱码。
Python 2.x 中的 String 与 Unicode

在 Python 2.x 中是有两种字串符相关类型的，分别为 String 和 Unicode，两者提供的接口非常类似，有时候又能自动转换，蛮容易误导人的。在 Python 3 中 这两个类型分别用 Bytes 和 String 替代了。这个名字更能说明两者的本质：Python 2.x 中的 String 中存储的是没有编码信息的字节序列，也就是说 String 中存储的是已经编码过后的序列，但他并不知道自身是用的哪种编码。相反的 Unicode 中存储的是记载了编码的字串信息，其中存储的就是相应字符的 Unicode 编号。在这里用程序来说明，我们建立一个简单的脚本名字为 encoding.py，代码如下：


#!/usr/bin/python  

# -*- coding: utf-8 -*-    

strs = "这是中文"  

unis = "这也是中文".decode("utf8")    

print strs[0:2]  

print unis[0:2].encode('gbk')    

print len(strs)  

print len(unis)  

前面两行后面会解释到，就是限定运行环境以及该脚本文件的编码格式。此脚本在这里可以下载，如果你要自己写的话请务必确保脚本的编码是 utf8 而不是别的。在 Windows 下的运行结果在这里，我觉得正好能说明问题：


C:\SHARED\Dev\scripts>encoding.py    

这里需要说明，我们的程序是 UTF8 编码，主要意义是该程序中的所有直接写出来的字串符（用"", ''括起来的字串符）是运用 UTF8 格式编码的；然而Windows 下的命令行是 GBK 环境。这里 strs是一个 String。事实上在 Python 2.x 中直接写在程序中的字串符，其类型都是 String(这里不考虑 string literal)。我们先直接输出 strs[0:2]，得到的是一个乱码字符(这个字符只是碰巧凑成是一个字)。如上面说的，String中存储的是没有编码信息的字串序列，这里就是将strs中前两个编号取出并尝试显示。由于命令行环境为 GBK 编码，这里对应的字碰巧凑成了一个字，但是跟原本的字没有任何关系。


　　unis是由一个 String调用 decode()方法得到，这正是在 Python 2.x 中取得 Unicode的最基本的方式。由于 String并不知道它本身是由什么编码格式来进行的编码，这里是我们的责任来确定他原来是用哪种编码方式进行编码。我们知道代码中的编码格式是 UTF8，所以我们可以用调用 String的 decode()方法来进行反编码，也就是解码， 把字串符从某种编码后的格式转换为其唯一对应的 Unicode 编号。unis为解码获得的结果，其在 Python 2.x 中对应类型就是 Unicode，其中存储的就是 每个字符对应的 Unicode 编号。

我们尝试输出 unis的前两个字符，在这里我们调用了 Unicode的 encode()方法。这就是编码的过程。我们知道 Windows 命令行下的编码是 GBK，只有采用 GBK 编码的字符才能正确显示。所以在这里我们通过调用 Unicode的 encode()方法，将 unis中存储的 Unicode 编号 按照 GBK 的规则来进行编码，并输出到屏幕上。这里我们看到这里正确的显示了 unis中的前两个字符。要注意的是在命令行中直接 print Unicode的话 Python 会自动根据当前环境进行编码后再显示，但这样掩盖了两者的区别。建议总是手动调用 encode和 decode方法，这样自己也会清楚一些。

后面两者长度的差别也是佐证我们之前的例子。
strs中存储的是 UTF8 编码后的编号序列，上面看到一个中文字符在 UTF8 编码后变成三个连续的，所以 strs长度为 3x4 = 12。你可以想象 strs中存放的并不是中文，而是一系列没有意义的比特序列；而 unis中存储的是对应的中文的 Unicode 编码。我们知道每一个字符对应一个编号，所以五个字对应五个编号，长度为 5。避免，和解决编码产生的问题

了解了 Python Unicode 编码解码的这些概念后，我们来看看如何尽量的避免遇到让人烦心的编码问题。

首先如果你的代码中有中文，那么一定要务必声明代码的编码格式。根据 PEP-0263 中的介绍，在程序的最开始加上以下两行注释就能确定编码：


#!/usr/bin/python  

# -*- coding: utf-8 -*-  

其中 utf-8就是指定的编码格式。事实上你应该总是使用 UTF8 作为你 Python 程序的编码格式，因为未来的 Python 3 所有文件都将默认以 UTF8 编码。另外除了声明，你必须确定你用来编辑 Python 程序的编辑器是不是真的以 UTF8 编码来存储文件。

之后就是养成关于编码解码的好习惯。当你的程序有 String作为输入时，应该尽早的将其转换为 Unicode，再在程序中进行处理。再输出的时候，也要尽可能玩，直到最后输出的时刻才将 Unicode编码为所需编码格式的 String进行输出。同样的你必须保持你程序内部所有参与运算的字串都是 Unicode格式。很多著名的 Python 库例如 django 就是采用的这种方式，效果也蛮好。千万不要依赖 Python 自己进行两者之间的转换，也不要将 String和 Unicode放在一起运算，这些行为一方面十分容易引起错误，另一方面在 Python 3 中已经无法再现。虽说确定 String的编码格式是程序员的责任，但有时候你真的不知道有些字串符到底是什么编码的。这里有一个神奇 chardet 能够帮助你。以下是摘自其页面上的例子，很好了说明了它的作用：读入任意一串字符，猜测其编码格式，并且给出猜测的确信度。


>>> import urllib  

>>> urlread = lambda url: urllib.urlopen(url).read()  

>>> import chardet  

>>> chardet.detect(urlread("http://google.cn/"))  {'encoding': 'GB2312', 'confidence': 0.99}    

>>> chardet.detect(urlread("http://yahoo.co.jp/"))  {'encoding': 'EUC-JP', 'confidence': 0.99}   

>>> chardet.detect(urlread("http://amazon.co.jp/"))  {'encoding': 'SHIFT_JIS', 'confidence': 1}    

>>> chardet.detect(urlread("http://pravda.ru/"))  {'encoding': 'windows-1251', 'confidence': 0.9355}  

如果 confidence 非常低的话或者 chardet 直接报错，多半是字串经过多次错误编码解码，要从别的地方找办法解决问题。

如果上面的介绍还不能让你理解 Unicode 的概念，这里还有几篇关于这个问题的文章：

介绍 Unicode 的两篇文章 [1], [2]。关于 Unicode 有更为详细的解释。

Unicode In Python, Completely Demystified 特别针对 Python 下的 Unicode 处理进行详细的讲解。

其他除了上面几个重要的问题之外，剩下的资源
