### 第1章 快速上手：基础知识
整数总是向下圆整，而round圆整到最接近的整数，并在两个整数一样近时圆整到偶数。如round(1.5)输出2  
使用import导入模块，再以module.function的方式使用模块中的函数。  
使用命令import的变种from module import function，可在调用函数时不指定模块前缀。  
Python标准库提供了一个专门用于处理复数的模块。  
```  
>>> import cmath
>>> cmath.sqrt(-1)
1j
```
注意到这里没有使用from ... import ...。如果使用了这种import命令，将无法使用常规函
数sqrt。类似这样的名称冲突很隐蔽，因此除非必须使用from版的import命令，否则应坚持使用
常规版import命令。  
**注释务必言而有物，不要重复去讲通过代码很容易获得的信息。无用而重复的注释还不如没有。**  
使用str能以合理的方式将值转换为用户能够看懂的字符串。使用repr时，通常会获得值的合法Python表达式表示。  
```Python 
>>> print(repr("Hello,\nworld!"))
'Hello,\nworld!'
>>> print(str("Hello,\nworld!"))
Hello,
world!
```
- 长字符串：表示很长的字符串（跨越多行的字符串），可使用三引号。
- 常规字符串也可跨多行。只要在行尾加上反斜杠，反斜杠和换行符将被转义，即被忽略。
- 原始字符串：用前缀**r**表示，不能以单个反斜杠结尾。如果要指定以反斜杠结尾的原始字符串，基本技巧是将反斜杠单独作为一个字符串。
``` 
>>> print(r'C:\Program Files\foo' '\\')
C:\Program Files\foo\
```
``` 
abs(number) 返回指定数的绝对值
bytes(string, encoding[, errors]) 对指定的字符串进行编码，并以指定的方式处理错误
cmath.sqrt(number) 返回平方根；可用于负数
float(object) 将字符串或数字转换为浮点数
help([object]) 提供交互式帮助
input(prompt) 以字符串的方式获取用户输入
int(object) 将字符串或数转换为整数
math.ceil(number) 以浮点数的方式返回向上圆整的结果
math.floor(number) 以浮点数的方式返回向下圆整的结果
math.sqrt(number) 返回平方根；不能用于负数
pow(x, y[, z]) 返回x的y次方对z求模的结果
print(object, ...) 将提供的实参打印出来，并用空格分隔
repr(object) 返回指定值的字符串表示
round(number[, ndigits]) 四舍五入为指定的精度，正好为5时舍入到偶数
str(object) 将指定的值转换为字符串。用于转换bytes时，可指定编码和错误处理方式
```
### 第2章 列表和元组
列表和元组的区别：列表可以修改，元组不可更改。  
序列中的所有元素都有编号——从0开始递增。  
通用的序列操作：索引、切片、相加、相乘和成员资格检查。  
第一个索引指定的元素包含在切片内，但第二个索引指定的元素不包含在切片内。  
一般而言，不能拼接不同类型的序列。  
函数len返回序列包含的元素个数，而min和max分别返回序列中最小和最大的元素。  
要将字符列表转换为字符串，可使用下面的表达式： ''.join(somelist)  
方法append用于将一个对象附加到列表末尾。  
方法clear就地清空列表的内容。  
方法extend能够同时将多个值附加到列表末尾。  
方法pop从列表中删除一个元素，并返回这一元素。  
**pop是唯一既修改列表又返回一个非None值的列表方法**  
方法reverse按相反的顺序排列列表中的元素。如果要按相反的顺序迭代序列，可使用函数reversed。  
方法sort用于对列表就地排序。为获取排序后的列表的副本，使用函数sorted。  
只要将一些值用逗号分隔，就能自动创建一个元组。  
``` 
len(seq) 返回序列的长度
list(seq) 将序列转换为列表
max(args) 返回序列或一组参数中的最大值
min(args) 返回序列和一组参数中的最小值
reversed(seq) 让你能够反向迭代序列
sorted(seq) 返回一个有序列表，其中包含指定序列中的所有元素
tuple(seq) 将序列转换为元组
```
### 第3章 使用字符串
%s称为**转换说明符**，指出了要将值插入什么地方。s意味着将值视为字符串形式格式设置。  
每个值都被插入字符串中，以替换用花括号括起的替换字段。要在最终结果中包含花括号，可在格式字符串中使用两个花括号来指定。  
``` 
>>> "{{replacement field}}".format()
"{replacement field}"
>>> from math import pi
>>> "{name} is approximately {value:.2f}.".format(value=pi, name="π")
'π is approximately 3.14.'
>>> print("{pi!s}{pi!r}{pi!a}".format(pi="π"))
π'π''\u03c0'
```
上述三个标志（s、r和a）指定分别使用str、repr和ascii进行转换。  
要指定左对齐、右对齐和剧中，可分别使用<、>和^。  
``` 
>>> print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi))
3.14
   3.14
      3.14
>>> '{:010.2f}'.format(pi)
'0000003.14'
```
方法join的作用与split相反，用于合并序列的元素。  
方法split用于将字符串拆分为序列。  
``` 
string.capwords(s[, sep]) 使用split根据sep拆分s，将每项的首字母大写，再以空格为分隔符将它们合并起来
ascii(obj) 创建指定对象的ASCII表示
```
### 第4章 当索引不通过时  
基本的字典操作： 
- len(d)返回字典d包含的项（键-值对）数。
- d[k]返回与键k相关联的值。
- d[k] = v将值v关联到键k。
- del d[k]删除键为k的项。
- k in d检查字典d是否包含键为k的项。
- 键的类型：可以是任何不可变的类型。
- 自动添加：即便是字典中没有的键，也可以给它赋值，这将在字典中创建一个新项。
- 成员资格：表达式k in d(其中d是一个字典)查找的是键而不是值，而表达式v in l(其中l是一个列表)查找的是值而不是索引。  

将字符串格式设置功能用于字典：  
``` 
>>> phonebook
{'Beth': '9022', 'Cecil': '3258'}
>>> "Cecil's phone number is {Cecil}.".format_map(phonebook)
"Cecil's phone number is 3258."
```
方法fromkeys创建一个新字典，其中包含指定的键，且每个键对应的值都是None。  
``` 
>>> {}.fromkeys(['name','age'])
{'age': None, 'name': None}
```
方法items返回一个包含所有字典项的列表，其中每个元素都为(key, value)的形式。字典项在列表中的排列顺序不确定。  
方法setdefault有点像get，因为它也获取与指定键相关联的值，但除此之外，setdefault还在字典不包含指定的键时，在字典中添加指定的键-值对。  
``` 
>>> d = {}
>>> d.setdefault('name', 'N/A')
'N/A'
>>> d
{'name': 'N/A'}
>>> d['name'] = 'Gumby'
>>> d.setdefault('name', 'N/A')
'Gumby'
>>> d
{'name': 'Gumby'}
```
方法update使用一个字典中的项来更新另一个字典。  
### 第5章 条件、循环及其他语句
print可自定义分隔符、自定义结束字符串。
``` 
>>> print('hello',"world!",end='\n\n',sep="_")
hello_world!

>>>
```
在语句末尾添加as子句并指定别名：import math as foobar  
序列解包（或可迭代对象解包）：将一个序列（或任何可迭代对象）解包，并将得到的值存储到一系列变量中。  
赋值语句的右边可以是任何类型的序列，但带星号的变量最终包含的总是一个列表。
``` 
>>> a, *b, c = "abc"
>>> a,b,c
('a', ['b'], 'c')
```
链式赋值：将多个变量关联到同一个值。x = y = somefunction()  
增强赋值：x += 1  
缩进：标准做法是只使用空格来缩进，且每级缩进4个空格。  
在Python中，使用冒号（:）指出接下来是一个代码块，并将该代码块中的每行代码都缩进相同的程度。  
status = "friend" if name.endswith("Gumby") else "stranger"  
==用来检查两个对象是否相等，而is用来检查两个对象是否相同（是同一个对象）。  
要获悉字母的顺序值，可使用函数ord。这个函数的作用与函数chr相反。  
如果知道必须满足特定条件，程序才能正确地运行，可在程序中添加assert语句充当检查点。  
``` 
>>> age = -1
>>> assert 0 < age < 100, 'The age must be realistic'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: The age must be realistic

>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
要让映射记住其项的插入顺序，可使用模块collections中的OrderedDict类。  
内置函数zip将两个序列“缝合”起来，并返回一个由元组组成的序列。当序列的长度不同时，将在最短的序列用完后停止“缝合”。  
内置函数enumerate能够迭代索引-值对，其中的索引是自动提供的。  
``` 
for index, string in enumerate(strings):
    if 'xxx' in string:
        strings[index] = '[censored]'
```
列表推导是一种从其他列表创建列表的方式。  
```  
>>> [x*x for x in range(10) if x % 3 == 0]
[0, 9, 36, 81]
>>> [(x,y) for x in range(3) for y in range(3)]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```
可使用花括号来执行字典推导。  
```  
>>> squares = {i:"{} squared is {}".format(i, i**2) for i in range(10)}
>>> squares[8]
'8 squared is 64'
```
使用del语句不仅会删除对象的引用，还会删除名称本身。  
函数exec将字符串作为代码执行，主要用于动态地创建代码字符串。  
eval计算用字符串表示的Python表达式的值，并返回结果。  
```  
>>> exec("print('Hello, world!')")
Hello, world!
>>> eval(input("Enter an arithmetic expression: "))
Enter an arithmetic expression: 6 + 18 * 2
42
```
```  
chr(n) 返回一个字符串，其中只包含一个字符，这个字符对应于传入的顺序值n（0 ≤
n < 256）
eval(source[,globals[,locals]]) 计算并返回字符串表示的表达式的结果
exec(source[, globals[, locals]]) 将字符串作为语句执行
enumerate(seq) 生成可迭代的索引值对
ord(c) 接受一个只包含一个字符的字符串，并返回这个字符的顺序值（一个整数）
range([start,] stop[, step]) 创建一个由整数组成的列表
reversed(seq) 按相反的顺序返回seq中的值，以便用于迭代
sorted(seq[,cmp][,key][,reverse]) 返回一个列表，其中包含seq中的所有值且这些值是经过排序的
xrange([start,] stop[, step]) 创建一个用于迭代的xrange对象
zip(seq1, seq2,...) 创建一个适合用于并行迭代的新序列
```
### 第6章 抽象
斐波那契数（一种数列，其中每个数都是前两个数的和。）  
要判断某个对象是否可调用，可使用内置函数callable。  
``` 
def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result
>>> fibs(5)
[0, 1, 1, 2, 3]
```
放在函数开头的字符串称为文档字符串（docstring），将作为函数的一部分存储起来。  
所有的函数都返回值。如果没有告诉它们该返回什么，将返回None。  
在def语句中，位于函数名后面的变量通常称为形参，而调用函数时提供的值称为实参。  
字符串（以及数和元组）是不可变的（immutable）。  
如果你创建覆盖整个列表的切片，得到的将是列表的副本。  
```  
>>> names = ['Mres. Entity', 'Mrs. Thing']
>>> n = names[:]
>>> n is names
False
>>> n == names
True
```
抽象的关键在于隐藏所有的更新细节。  
使用名称指定的参数称为关键字参数，最大的优点在于可以指定默认值。  
星号意味着收集余下的位置参数。如果没有可供收集的参数，params将是一个空元组。  
```  
>>> def print_params_2(title, *params):
...     print(title)
...     print(params)
...
>>> print_params_2('Nothing:')
Nothing:
()
>>>
```
要收集关键字参数，可使用两个星号。  
``` 
>>> def print_params_3(**params):
...     print(params)
...
>>> print_params_3(x=1, y=2, z=3)
{'x': 1, 'y': 2, 'z': 3}
>>>
```
模块bisect提供了标准的二分查找实现。  
``` 
map(func, seq[, seq, ...]) 对序列中的所有元素执行函数
filter(func, seq) 返回一个列表，其中包含对其执行函数时结果为真的所有元素
reduce(func, seq[, initial]) 等价于 func(func(func(seq[0], seq[1]), seq[2]), ...)
sum(seq) 返回 seq 中所有元素的和
apply(func[, args[, kwargs]]) 调用函数（还提供要传递给函数的参数）
```
### 第7章 再谈抽象
在面向对象编程中，术语对象大致意味着一系列数据（属性）以及一套访问和操作这些数据的方法。  
- 多态（polymorphism）：可对不同类型的对象执行相同的操作。
- 封装（encapsulation）：对外部隐藏有关对象工作原理的细节。
- 继承：可基于通用类创建出专用类。  

标准模块random包含一个名为choice的函数，它从序列中随机选择一个元素。  
``` 
>>> def length_message(x):
...     print("The length of ", repr(x), "is", len(x))
...
>>> length_message('Fnord')
The length of  'Fnord' is 5
>>> length_message([1,2,3])
The length of  [1, 2, 3] is 3
```
类的定义——一种对象。每个对象都属于特定的类，并被称为该类的实例。  
要让方法或属性成为私有的（不能从外部访问），只需让其名称以两个下划线打头即可。  
如果你不希望名称被修改，又想发出不要从外部修改属性或方法的信号，可用一个下划线打头。这虽然只是一种约定，但也有些作用。例如，from module import * 不会导入以一个下划线打头的名称。  
要指定超类，可在class语句中的类名后加上超类名，并将其用圆括号括起。  
要确定一个类是否是另一个类的子类，使用内置方法issubclass。  
如果你有一个类，并像知道它的基类，可访问其特殊属性 __bases__ 。  
要确定对象是否是特定类的实例，可使用 isinstance 。  
如果要获悉对象属于哪个类，可使用属性 __class__ 。  
除非万不得已，否则应避免使用多重继承。  
使用多重继承时，有一点务必注意：如果多个超类以不同的方式实现了同一个方法，必须在class语句中小心排列这些超类，因为位于前面的类的方法将覆盖位于后面的类的方法。  
要查看对象中存储的所有值，可检查其__dict__属性。  
鸭子类型，即假设所有对象都能完成其工作，同时偶尔使用hasattr来检查所需的方法是否存在。  
``` 
from abc import ABC, abstractmethod

class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass
```
@this的东西被称为装饰器。使用@abstractmethod来将方法标记为抽象的——在子类中必须实现的方法。  
标准库（如模块collections.abc）提供了多个很有用的抽象类。  
关于面向对象设计的一些思考：  
- 将相关的东西放在一起。  
- 不要让对象之间过于亲密。  
- 慎用继承，尤其是多重继承。  
- 保持简单。让方法短小紧凑。  

确定需要哪些类以及这些类应包含哪些方法时，尝试像下面这样做。  
(1) 将有关问题的描述（程序需要做什么）记录下来，并给所有的名词、动词和形容词加
上标记。  
(2) 在名词中找出可能的类。  
(3) 在动词中找出可能的方法。  
(4) 在形容词中找出可能的属性。  
(5) 将找出的方法和属性分配给各个类。  
(6) 记录（或设想）一系列用例，即使用程序的场景，并尽力确保这些用例涵盖了所有的功能。  
(7) 透彻而仔细地考虑每个场景，确保模型包含了所需的一切。如果有遗漏，就加上；如果
有不太对的地方，就修改。不断地重复这个过程，直到对模型满意为止。  
``` 
callable(object) 判断对象是否是可调用的（如是否是函数或方法）
getattr(object,name[,default]) 获取属性的值，还可提供默认值
hasattr(object, name) 确定对象是否有指定的属性
isinstance(object, class) 确定对象是否是指定类的实例
issubclass(A, B) 确定A是否是B的子类
random.choice(sequence) 从一个非空序列中随机地选择一个元素
setattr(object, name, value) 将对象的指定属性设置为指定的值
type(object) 返回对象的类型
```
### 第8章 异常
要引发异常，可使用raise语句，并将一个类（必须是Exception的子类）或实例作为参数。  
捕获异常后，如果要重新引发它（即继续向上传播），可调用raise且不提供任何参数。  
如果要使用一个except子句捕获多种异常，可在一个元组中指定这些异常。  
``` 
try:
    1 / 0
except NameError:
    print("Unknown variable")
else:
    print("That went well")
finally:
    print("Cleaning up.")
```
### 第9章 魔法方法、特性和迭代器
在Python中，创建构造函数很容易，只需将方法init的名称从普通的init改为魔法版__init__即可。  
[descriptor](https://docs.python.org/3/howto/descriptor.html)  
实现了方法__iter__的对象是可迭代的，而实现了方法__next__的对象是迭代器。  
包含yield语句的函数都被称为生成器。  
生成器由两个单独的部分组成：生成器的函数和生成器的迭代器。生成器的函数是由def语句定义的，其中包含yield。生成器的迭代器是这个函数返回的结果。  
``` 
>>> def simple_generator():
...     yield 1
...
>>> simple_generator
<function simple_generator at 0x0000012C19803E18>
>>> simple_generator()
<generator object simple_generator at 0x0000012C1B4D9678>
```
``` 
iter(obj) 从可迭代对象创建一个迭代器
next(it) 让迭代器前进一步并返回下一个元素
property(fget, fset, fdel, doc) 返回一个特性；所有参数都是可选的
super(class, obj) 返回一个超类的关联实例
```
### 第10章 开箱即用
模块并不是用来执行操作的，而是用于定义变量、函数、类等。鉴于定义只需做一次，因此导入模块多次和导入一次的效果相同。  
如果一定要重新加载模块，可使用模块importlib中的函数reload，它接受一个参数（要重新加载的模块），并返回重新加载的模块。  
``` 
import importlib
hello = importlib.reload(hello)
```
python -m progname args将使用命令行参数args来执行程序progname.  
检查模块是作为程序运行还是被导入另一个程序，使用变量__name__  
sys.path包含一个目录（表示为字符串）列表，解释器将在这些目录中查找模块。  
文件__init__.py的内容就将是包的内容。  
函数dir列出对象的所有属性。  
from copy import * 将只能得到变量__all__中列出的那些函数。  
help提供需要的所有信息。help(copy.copy)  
文档字符串就是在函数开头编写的字符串，用于对函数进行说明。copy.copy.\_\_doc__  
**事实上，要学习Python，阅读源代码是除动手编写代码外的最佳方式。**  
模块sys中一些重要的函数和变量：  
``` 
argv 命令行参数，包括脚本名
exit([arg]) 退出当前程序，可通过可选参数指定返回值或错误消息
modules 一个字典，将模块名映射到加载的模块
path 一个列表，包含要在其中查找模块的目录的名称
platform 一个平台标识符，如sunos5或win32
stdin 标准输入流——一个类似于文件的对象
stdout 标准输出流——一个类似于文件的对象
stderr 标准错误流——一个类似于文件的对象
```
模块os中一些重要的函数和变量：  
``` 
environ 包含环境变量的映射
system(command) 在子shell中执行操作系统命令
sep 路径中使用的分隔符
pathsep 分隔不同路径的分隔符
linesep 行分隔符（'\n'、 '\r'或'\r\n'）
urandom(n) 返回n个字节的强加密随机数据
```
模块fileinput中一些重要的函数：  
``` 
input([files[, inplace[, backup]]]) 帮助迭代多个输入流中的行
filename() 返回当前文件的名称
lineno() 返回（累计的）当前行号
filelineno() 返回在当前文件中的行号
isfirstline() 检查当前行是否是文件中的第一行
isstdin() 检查最后一行是否来自sys.stdin
nextfile() 关闭当前文件并移到下一个文件
close() 关闭序列
```
模块heapq中一些重要的函数：  
``` 
heappush(heap, x) 将x压入堆中
heappop(heap) 从堆中弹出最小的元素
heapify(heap) 让列表具备堆特征
heapreplace(heap, x) 弹出最小的元素，并将x压入堆中
nlargest(n, iter) 返回iter中n个最大的元素
nsmallest(n, iter) 返回iter中n个最小的元素
```
位置i处的元素总是大于位置i // 2处的元素，称为堆特征。  
函数heappop弹出最小的元素（总是位于索引0处），并确保剩余元素中最小的那个位于索引0处（保持堆特征）。  
``` 
>>> from heapq import *
>>> from random import shuffle
>>> data = list(range(10))
>>> shuffle(data)
>>> heap = []
>>> for n in data:
...     heappush(heap, n)
...
>>> heap
[0, 2, 1, 3, 5, 8, 4, 9, 6, 7]
>>> heappush(heap, 0.5)
>>> heap
[0, 0.5, 1, 3, 2, 8, 4, 9, 6, 7, 5]
>>> heappop(heap)
0
>>> heap
[0.5, 2, 1, 3, 5, 8, 4, 9, 6, 7]
```
模块time追踪一些重要的函数：  
```  
asctime([tuple]) 将时间元组转换为字符串
localtime([secs]) 将秒数转换为表示当地时间的日期元组
mktime(tuple) 将时间元组转换为当地时间
sleep(secs) 休眠（什么都不做） secs秒
strptime(string[, format]) 将字符串转换为时间元组
time() 当前时间（从新纪元开始后的秒数，以UTC为准）
```
真正的随机（如用于加密或实现与安全相关的功能），应考虑使用模块os中的函数urandom。  
模块random中一些重要的函数：  
``` 
random() 返回一个0~1（含）的随机实数
getrandbits(n) 以长整数方式返回n个随机的二进制位
uniform(a, b) 返回一个a~b（含）的随机实数
randrange([start], stop, [step]) 从range(start, stop, step)中随机地选择一个数
choice(seq) 从序列seq中随机地选择一个元素
shuffle(seq[, random]) 就地打乱序列seq
sample(seq, n) 从序列seq中随机地选择n个值不同的元素
```
shelve是一个对象持久化保存方法，将对象保存到文件里面，一般来说对象的保存和恢复都是通过shelve来进行的。
你的问题是test.txt已经存在，并且格式与shelve不符，所以提示 “db type could not be determined”
解决方法: 删除test.txt文件，首次运行后会自动生成该文件。  
模式'python\\.org'只与'python.org'匹配。为表示模块re要求的单个反斜杠，需要在字符串中书写两个反斜杠。  
模块re中的一些重要的函数：  
```  
compile(pattern[, flags]) 根据包含正则表达式的字符串创建模式对象
search(pattern, string[, flags]) 在字符串中查找模式
match(pattern, string[, flags]) 在字符串开头匹配模式
split(pattern, string[, maxsplit=0]) 根据模式来分割字符串
findall(pattern, string) 返回一个列表，其中包含字符串中所有与模式匹配的子串
sub(pat, repl, string[, count=0]) 将字符串中与模式pat匹配的子串都替换为repl
escape(string) 对字符串中所有的正则表达式特殊字符都进行转义
```
编组就是放在圆括号内的子模式，它们是根据左边的括号数编号的，其中编组0指的是整个模式。  
``` 
'There (was a (wee) (cooper)) who (lived in Fyfe)'
包含如下编组：
0 There was a wee cooper who lived in Fyfe
1 was a wee cooper
2 wee
3 cooper
4 lived in Fyfe
```
re匹配对象的重要方法：  
``` 
group([group1, ...]) 获取与给定子模式（编组）匹配的子串
start([group]) 返回与给定编组匹配的子串的起始位置
end([group]) 返回与给定编组匹配的子串的终止位置（与切片一样，不包含终止位置）
span([group]) 返回与给定编组匹配的子串的起始和终止位置
```
对于所有的重复运算符，都可在后面加上问号来将其指定为非贪婪的。  
**如果任务看起来吓人，将其分解为较小的部分几乎总是大有裨益。另外，要对手头的工具进行评估，确定如何解决面临的问题。**  
**无论要精通哪种编程语言，最佳的方式都是尝试使用它——找出其局限性和长处。**  
``` 
dir(obj) 返回一个按字母顺序排列的属性名列表
help([obj]) 提供交互式帮助或有关特定对象的帮助信息
imp.reload(module) 返回已导入的模块的重载版本
```
### 第11章 文件
要读取一行（从当前位置到下一个分行符的文本），可使用方法readline  
要读取文件中的所有行，并以列表的方式返回它们，可使用方法readlines  
``` 
with open("somefile.txt") as somefile:
    do_something(somefile)
```
with语句能够打开文件并将其赋给一个变量。在语句体中，你将数据写入文件。到达该语句末尾时，将自动关闭文件，即便出现异常亦如此。  
```  
open(name, ...) 打开文件并返回一个文件对象
```
### 第12章 图形用户界面

### 第13章 数据库支持
函数connect的常用参数：  
```  
dsn 数据源名称，具体含义随数据库而异 否
user 用户名 是
password 用户密码 是
host 主机名 是
database 数据库名称 是
```
连接对象的方法：  
```  
close() 关闭连接对象。之后，连接对象及其游标将不可用
commit() 提交未提交的事务——如果支持的话；否则什么都不做
rollback() 回滚未提交的事务（可能不可用）
cursor() 返回连接的游标对象
```
游标对象的方法：
```  
callproc(name[, params]) 使用指定的参数调用指定的数据库过程（可选）
close() 关闭游标。关闭后游标不可用
execute(oper[, params]) 执行一个SQL操作——可能指定参数
executemany(oper, pseq) 执行指定的SQL操作多次，每次都序列中的一组参数
fetchone() 以序列的方式取回查询结果中的下一行；如果没有更多的行，就返回None
fetchmany([size]) 取回查询结果中的多行，其中参数size的值默认为arraysize
fetchall() 以序列的序列的方式取回余下的所有行
nextset() 跳到下一个结果集，这个方法是可选的
setinputsizes(sizes) 用于为参数预定义内存区域
setoutputsize(size[, col]) 为取回大量数据而设置缓冲区长度
```
DB API构造函数和特殊值：  
```  
Date(year, month, day) 创建包含日期值的对象
Time(hour, minute, second) 创建包含时间值的对象
Timestamp(y, mon, d, h, min, s) 创建包含时间戳的对象
DateFromTicks(ticks) 根据从新纪元开始过去的秒数创建包含日期值的对象
TimeFromTicks(ticks) 根据从新纪元开始过去的秒数创建包含时间值的对象
imestampFromTicks(ticks) 根据从新纪元开始过去的秒数创建包含时间戳的对象
Binary(string) 创建包含二进制字符串值的对象
STRING 描述基于字符串的列（如CHAR）
BINARY 描述二进制列（如LONG或RAW）
NUMBER 描述数字列
DATETIME 描述日期/时间列
ROWID 描述行ID列
```
### 第 14 章 网络编程
标准库中一些与网络相关的模块：  
```  
asynchat 包含补充asyncore的功能（参见第24章）
asyncore 异步套接字处理程序（参见第24章）
cgi 基本的CGI支持（参见第15章）
Cookie Cookie对象操作，主要用于服务器
cookielib 客户端Cookie支持
email 电子邮件（包括MIME）支持
ftplib FTP客户端模块
gopherlib Gopher客户端模块
httplib HTTP 客户端模块
imaplib IMAP4客户端模块
mailbox 读取多种邮箱格式
mailcap 通过mailcap文件访问MIME配置
mhlib 访问MH邮箱
nntplib NNTP客户端模块（参见第23章）
poplib POP客户端模块
robotparser 解析Web服务器robot文件
SimpleXMLRPCServer 一个简单的XML-RPC服务器（参见第27章）
smtpd SMTP服务器模块
smtplib SMTP客户端模块
telnetlib Telnet客户端模块
urlparse 用于解读URL
xmlrpclib XML-RPC客户端支持（参见第27章）
```
**处理多个连接的主要方式有三种：分叉（forking）、线程化和异步IO**  
```  
urllib.urlopen(url[, data[, proxies]]) 根据指定的URL打开一个类似于文件的对象
urllib.urlretrieve(url[,fname[,hook[,data]]]) 下载URL指定的文件
urllib.quote(string[, safe]) 替换特殊的URL字符
urllib.quote_plus(string[, safe]) 与quote一样，但也将空格替换为+
urllib.unquote(string) 与quote相反
urllib.unquote_plus(string) 与quote_plus相反
urllib.urlencode(query[, doseq]) 对映射进行编码，以便用于CGI查询中
select.select(iseq, oseq, eseq[, timeout]) 找出为读/写做好了准备的套接字
select.poll() 创建一个轮询对象，用于轮询套接字
reactor.listenTCP(port, factory) 监听连接的Twisted函数
reactor.run() 启动主服务器循环的Twisted函数
```
### 第15章 Python 和 Web
屏幕抓取是通过程序下载网页并从中提取信息的过程。  
CGI(Common Gateway Interface):通用网关接口。  
WSDL: Web服务描述语言。  
### 第16章 测试基础
测试在先，编码在后，称为测试驱动的编程。  
先编写测试再编写代码并不是为了发现bug，而是为了检查代码是否管用。  
在测试驱动的编程中，最重要的一点是在编码期间反复地运行方法（函数或脚本），以不断获得有关你做法优劣的反馈。  
测试驱动开发过程的各个阶段：  
(1)确定需要实现的新功能。可将其记录下来，再为之编写一个测试。
(2)编写实现功能的框架代码，让程序能够运行（不存在语法错误之类的问题），但测试依然
无法通过。测试失败是很重要的，因为这样你才能确定它可能失败。如果测试有错误，导致在任
何情况下都能成功（这样的情况我遇到过很多次），那么它实际上什么都没有测试。不断重复这
个过程：确定测试失败后，再试图让它成功。  
(3)编写让测试刚好能够通过的代码。在这个阶段，无需完全实现所需的功能，而只要让测
试能够通过即可。这样，在整个开发阶段，都能够让所有的测试通过（首次运行测试时除外），
即便是刚着手实现功能时亦如此。
(4)改进（重构）代码以全面而准确地实现所需的功能，同时确保测试依然能够成功。
unittest:一个通用的测试框架。  
doctest:一个更简单的模块，是为检查文档而设计的，但也非常适合用来编写单元测试。  
doctest.testmod  
python my_math.py -v (verbose，意为详尽)  
源代码检查（PyChecker, PyLint）是一种发现代码中常见错误或问题的方式。  
性能分析（Profile, cProfile）指的是搞清楚程序的运行速度到底有多快。  
单元程序可让程序管用，源代码检查可让程序更好，而性能分析可让程序更快。  
```
doctest.testmod(module) 检查文档字符串中的示例（还接受很多其他的参数）
unittest.main() 运行当前模块中的单元测试
profile.run(stmt[,filename]) 执行语句并对其进行性能分析；可将分析结果保存到参数filename指定的文件中
```
### 第17章 扩展Python
回文（palindrome;如 I prefer pi）是忽略空格、标点等后正着读和反着读一样的句子。  
### 第18章 程序打包
1. 创建hello.py  
2. 简单的setuptools安装脚本（setup.py）
``` 
from setuptools import setup
setup(name='Hello',
      version='1.0',
      description='A simple example',
      author='Liu',
      py_modules=['Hello'])
```
3. 编译：python setup.py build
4. 安装：python setup.py install
5. 打包：python setup.py sdist  

使用py2exe创建可执行程序。py2exe目前只支持到python3.5，可以使用pyinstaller打包成exe:  
```
pip install pyinstaller
pyinstaller -F water_to3.py # 打包成exe文件
```

要让别人能够使用pip安装你开发的包，必须向Python Package Index(PyPI)注册它。  
python setup.py register  
注册包后，使用upload将其上传到PyPI.  
python setup sdist upload  
### 第19章 趣味编程
在编程过程中遇到麻烦（肯定会遇到）时，不要固守最初的设计和想法，而要灵活变通，以柔克刚。要做好应对并适
应变化的准备，不将意外的事故视为令人气馁的打击，而是将其看作让你重新探索新选项和可
能性的契机。  
原型（prototype）指的是尝试性实现，即一个模型。它实现了最终程序的主要功能。  
灵活性：设计和编程时，应以灵活性为目标。  
原型设计：要深入了解问题和可能的实现方案，一个重要的技巧是编写程序的简化版本，以了解它是如何工作的。  
配置：通过提取程序中的常量，可让以后修改程序变得更容易。  
日志：日志对找出程序存在的问题或监视其行为大有裨益。最安全的做法是使用标准库中的模块logging。  
### 第20章 项目1：自动添加标签







