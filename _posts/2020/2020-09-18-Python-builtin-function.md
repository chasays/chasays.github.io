---
layout: post
title: "Python内建函数"
subtitle: '学下下内建函数，事半功倍'
author: "叉叉敌"
header-style: text
tags:
  - python
  - 内建函数
  - 效率
  - 基础
---

是计算一个数的商和余数的时候，发现基础的内建函数还没有掌握，今天空了来补一下。以下的列子均是在Python3里面支持的。

那就从第一个开始求余数和商开始吧。


# 数字有关
 

### 数字计算


- divmod
python `divmod() `函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。

![1](https://gitee.com/chasays/mdPic/raw/master/uPic/eHOw9Q.png)

- abs
提到数字计算还有用的最多的， `abs`，比如求任意一个数的x进制，如果是复数就可以用上这个 `abs，` 对应的加上一个 `signal -`。

```py
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if base > len(digits):
    raise ValueError("Bases greater than 36 not handled in base_repr.")
elif base < 2:
    raise ValueError("Bases less than 2 not handled in base_repr.")

num = abs(number)
res = []
while num:
    num, r = divmod(num, base)
    #res.append(digits[num % base])
    #num //= base
    res.append(digits[r])

if padding:
    res.append('0' * padding)
if number < 0:
    res.append('-')
return ''.join(reversed(res or '0'))
```
但是还可以用切片的方式来处理这个算法，
```py
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
```

- round 

- pow
和math.pow 有点差别就是，后者是返回的float，前者类似于 `**`的计算结果， 比如pow(2,2) = 2**2

- sum
有其他高级用法的可以参考numpy.sum这个求和
- min
- max
```py
>>> round(2.456, 2)
2.26
>>> pow(3, 3)
27
>>> sum([0,1,2,3,4], 2)      # 列表计算总和后再加 2
12
>>> s = [2,3,4,1]
>>> max(s)
4
>>> min(s)
1
```

### 输入输出

- input
- print
在python3的时候是一个函数， 不只是一个关键字了， 
>print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

下面就是每个0.5s间隔打一个点，就是类似`loading.......`的动态效果
```py
print("Loading",end = "")
for i in range(20):
    print(".",end = '',flush = True)
    time.sleep(0.5)
```


### 数据类型

- bool
```py
>>>issubclass(bool, int)  # bool 是 int 子类
True
```
- int
```py
>>> int('0xa',16)  
10  
```
- float
- complex
```py
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
>>> complex("1+2j")
(1 + 2j)
```
### 进制转换
- bin

- otc
- hex
```py
>>> bin(10)
'0b1010'
>>> oct(20)
'0o24'
>>> hex(12)
'0xc'
```

# 数据结构

### 序列

- list
- tuple
```py

>>> tuple({1:2,3:4})    #针对字典 会返回字典的key组成的tuple
 
(1, 3)
```

### 操作序列
- reverse
- slice
其实和[::]类似，可以巧妙的用步长为-1就可以反转，看看下面的列子
```py

>>> s.reverse()
>>> s
[1, 4, 3, 2]

>>>myslice = slice(5)    # 设置截取5个元素的切片
>>> myslice
slice(None, 5, None)
>>> arr = range(10)
>>> arr
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> arr[myslice]         # 截取 5 个元素
[0, 1, 2, 3, 4]
>>> s
[1, 4, 3, 2]
>>> s[::-1]
[2, 3, 4, 1] #可以有reverse的效果
```

### 字符串

- str
- bytes (only for python3)
可以用于有些socket只接受byte类型的input
- ord
ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数
- chr

- repr
repr() 函数将对象转化为供解释器读取的形式。
和str()效果类似

```py
>>> str(s)
'[1, 4, 3, 2]'
>>> bytes('xxd', 'utf-8')
b'xxd'
>>> bytes('叉叉敌', 'utf-8')
b'\xe5\x8f\x89\xe5\x8f\x89\xe6\x95\x8c'

>>> ord('a')
97
>>> ord('A')
65
>>> chr(97)
'a'
>>> repr(s)
'[1, 4, 3, 2]'
```

### 数据集合

- dict
- set
set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
- frozenset
返回一个冻结的集合，冻结后集合`不能再添加或删除任何元素`。对象可以list， dict，tuple等
- getattr
用于判断对象是否包含对应的属性

```py
>>> dict(a='a', b='b', t='t')     # 传入关键字
{'a': 'a', 'b': 'b', 't': 't'}

>>> set(s)
{1, 2, 3, 4}
>>> ss = [2,3,4,5]
>>> set(ss)
{2, 3, 4, 5}

>>> set1 = set(ss)
>>> set2 = set(s)
>>> set1 |set2
{1, 2, 3, 4, 5}
>>> set1 - set2
{5}
>>> set2 - set1
{1}

>>> adict = {}
>>> fs = frozenset(s)
>>> adict[fs] = 123
>>> adict
{frozenset({1, 2, 3, 4}): 123}

# 获取对象属性后返回值可直接使用
>>> class A(object):        
...     def set(self, a, b):
...         x = a        
...         a = b        
...         b = x        
...         print a, b   
... 
>>> a = A()                 
>>> c = getattr(a, 'set')
>>> c(a='1', b='2')
2 1
```
### 处理集合的函数
- len
Python len() 方法返回对象（字符、列表、元组等）长度或项目个数。


- sorted
sorted() 函数对所有可迭代的对象进行排序操作。

- enumerate
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
这样就不用再加一个参数来获取对于的位置，直接就可以获取到对于的index值。

```py
>>> for i,v in enumerate(s):
...     print(i,v)
...
0 1
1 4
2 3
3 2
```
- all
可迭代对象中全部是True, 结果才是True
比如用于 需要执行所有的操作， 但是要最后检查实际的结果其中有没有Fail。 先把结果保存到一个list，然后用all(list)。
>元素除了是 0、空、None、False 外都算 True。 any下同。


- any
any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。

- zip
用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
>在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。

```py

>>> zipped = list(zip(s,ss)) # 打包
>>> zipped
[(1, 2), (4, 3), (3, 4), (2, 5)]
>>> zip(*zipped)
<zip object at 0x105c89190>
>>> list(zip(*zipped)) # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 4, 3, 2), (2, 3, 4, 5)]
```

- filter
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

```py

import math
def is_sqr(x):
    return math.sqrt(x) % 1 == 0
 
newlist = filter(is_sqr, range(1, 101))
print(newlist)
:: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 
```
- map
map() 会根据提供的函数对指定序列做映射。用法和filter有点类似，` 不过map要多个迭代参数`

```py
>>>def square(x) :            # 计算平方数
...     return x ** 2
... 
>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]
 
# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]
```

- locals
locals() 函数会以字典类型返回当前位置的`全部局部变量`。

```py
>>> def testlocals(arg):
...     x = 1
...     print(locals())
...
>>> testlocals(4)
{'arg': 4, 'x': 1}
```

- globals
globals() 函数会以字典类型返回当前位置的`全部全局变量`。

```py
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 's': [1, 4, 3, 2], 'slice': slice(None, 2, None), 'ss': [2, 3, 4, 5], 'set1': {2, 3, 4, 5}, 'set2': {1, 2, 3, 4}, 'i': 3, 'v': 2, 'list1': <zip object at 0x105cd8410>, 'zipped': [(1, 2), (4, 3), (3, 4), (2, 5)], 'testlocals': <function testlocals at 0x105c497a0>}
```

### 迭代器和生成器

- range
用方法和切片参数类似
- next
- iter
iter和next搭配使用， 这样就节约内存的加载，就用的时候才会价值。

```py
>>> while True:
...     x = next(it, 's')
...     print(x)
...     if x == 's':
...             break
...
1
2
3
4
5
s
```
### 执行字符串代码
- compile
compile() 函数将一个字符串编译为字节代码。
- eval
- exec
可以动态的拼接字符串后，然后执行字符串语句。

```py
>>>str = "for i in range(0,10): print(i)" 
>>> c = compile(str,'','exec')   # 编译为字节代码对象 
>>> c
<code object <module> at 0x10141e0b0, file "", line 1>
>>> exec(c)
0
1
2
3
4
5
6
7
8
9
>>> str = "3 * 4 + 5"
>>> a = compile(str,'','eval')
>>> eval(a)
17
```

### 内存相关
- hash
hash() 用于获取取一个对象（字符串或者数值等）的哈希值。
返回的 hash 值都是固定长度的，也用于校验程序在传输过程中是否被第三方（木马）修改，如果程序（字符）在传输过程中被修改hash值即发生变化，如果没有被修改，则 hash 值和原始的 hash 值吻合。 有点类似文件的md5，不过md5也有可能重复，实际应该是shanum。

### 其他
- open
```py
with open('file') as f:
    f.write('ccd\n')

```
- __import__
用于动态加载类和函数 。
经常用于一个模块经常变化就可以使用 __import__() 来动态载入。

- callable
用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。
```py
>>> def add(a, b):
...     return a + b
... 
>>> callable(add)             # 函数返回 True
True
```
- classmethod
修饰符对应的函数`不需要实例化`，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
```py
class A(object):
    bar = 1
    def func1(self):  
        print ('foo') 
    @classmethod
    def func2(cls):
        print ('func2')
        print (cls.bar)
        cls().func1()   # 调用 foo 方法
 
A.func2()               # 不需要实例化
```



还有一个比较常见的例子
```py
#创建一个类
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def print_date(self):
        print(self.year, self.month, self.day)

#实例化类
data_object = Date('2018','10','31')
#执行输出函数
data_object.print_date()
2018 10 31

#在上面的例子中可以看到类的实例化需要传递‘年月日’三个参数。并且是要求分别传递。那么假设用户不按照要求填写，他填写的2018-10-31这样的一个参数呢？
#我们需要先对参数进行分割处理，然后再实例化类。例如下面的代码：

#分割函数
def from_string(date_as_string):
    return map(int, date_as_string.split('-'))

#创建类
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def print_date(self):
        print(self.year, self.month, self.day)

#先执行分割函数对数据进行处理
year, month, day = from_string('2018-10-31')

#实例化类
data_object = Date(year, month, day)
#执行输出函数
data_object.print_date()
2018 10 31

#这样做视乎可以解决这个问题，但是from_string方法应该是属于类的一部分，现在需要写在外部，就导致了类功能外散，后期不便于管理，以后增加功能的时候会出现问题，所以我们就必须将from_string迁移到类里面去，并且还要在类的实例化之前调用它，我们都知道，一般情况下，如果想调用类中的方法，必须先实例化类，而我们现在的需求是要在实例化之前。这时就需要使用@classmethod咯。代码如下：

#创建一个类
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def print_date(self):
        print(self.year, self.month, self.day)
    
    #声明类方法
    @classmethod
    def from_string(cls, date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        return cls(year, month, day) #实例化类并返回实例化对象

data_object = Date.from_string('2018-10-31')
#执行输出函数
data_object.print_date()
2018 10 31

#这是一个比较经典的案例，来自于stackoverflow。我暂时没有想到更好的，就先对原案例进行了一些修改并且加上了一些注释。
#使用@classmethod可以有效的防止类功能外散，可以将对属于当前类的功能集中起来，便于管理，并且对类的继承、重载、多态都是有一定的帮助，这个小例子只能算是一个用法说明，在实际的操作中会有更加复杂的用法，还需要以项目的实际业务逻辑来制定。
```

- staticmethod
与上面的classmethod对应还有这个方法。
`最大的差别就是，在这个方法里面不涉及其他类成员的功能函数方法。`因为这个方法声明后始终调用的是基类的方法。而classmethod始终是当前类的。

- super
提到类，那不得不说下这个。` super()有一个非常好的优势，就是可以隐式的调用父类的当前类重载掉的方法。`

https://www.zky.name/article/67.html
```py
#声明A类
class A:
    def __init__(self):
        self.n = 2

    def plus(self, m):
        print('当前对象是 {} 来自 A类的plus方法'.format(self))
        self.n += m

#声明B类，继承A类
class B(A):
    def __init__(self):
        self.n = 3

    def plus(self, m):
        print('当前对象是 {} 来自 B类的plus方法'.format(self))
        #调用C类的plus方法
        super().plus(m)
        self.n += 3

#声明C类，继承A类。
class C(A):
    def __init__(self):
        self.n = 4

    def plus(self, m):
        print('当前对象是 {} 来自 C类的plus方法'.format(self))
        #调用A类的plus方法
        super().plus(m)
        self.n += 4

#声明D类，继承B和C类，这样D类就有2个父类咯。B和C就成为了兄弟类。
#D类的MRO是[D,B,C,A,Object]
class D(B, C):
    def __init__(self):
        self.n = 5

    def plus(self, m):
        print('当前对象是 {} 来自 D类的plus方法'.format(self))
        #调用B类的plus方法
        #一定要记住一点，在这个例子里，所有类中的super()函数都没有指定参数，所以从D类一直super()到A类，所有的self都是D类的self。
        super().plus(m)
        self.n += 5

#实例化D类
d = D()

#调用D类的plus()方法
d.plus(2)

#输出D类的n属性
print(d.n)

```

out：

```
当前对象是 <__main__.D object at 0x000000000222DCF8> 来自 D类的plus方法
当前对象是 <__main__.D object at 0x000000000222DCF8> 来自 B类的plus方法
当前对象是 <__main__.D object at 0x000000000222DCF8> 来自 C类的plus方法
当前对象是 <__main__.D object at 0x000000000222DCF8> 来自 A类的plus方法
19
```
如果是多重继承，就需要 `设置MRO并指定起始类`
```py
class D(B, C):
    def __init__(self):
        self.n = 5

    def plus(self, m):
        print('当前对象是 {} 来自 D类的plus方法'.format(self))
        super(C,self).plus(m)
        #super(C,D).plus(self,m) 和上一句效果相同。
        self.n += 5

#实例化D类
d = D()

#调用D类的plus()方法
d.plus(2)

#输出D类的n属性
print(d.n)
```
输出结果：
```
当前对象是 <__main__.D object at 0x000000000280DCF8> 来自 D类的plus方法
当前对象是 <__main__.D object at 0x000000000280DCF8> 来自 A类的plus方法
12
```


- dir
不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
```py
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'i', 'it', 'list1', 's', 'set1', 'set2', 'slice', 'ss', 'testlocals', 'time', 'v', 'x', 'zipped']
>>>
```

- help
查看函数或模块用途的详细说明。
```py
>>>help('sys')             # 查看 sys 模块的帮助
……显示帮助信息……
```
- id
或者内存地址
比如查看list的是一个连续的地址。其实python的list不是一个连续的地址。
- isinstance
判断一个对象是否是一个已知的类型，类似 type()。
如果要判断两个类型是否相同推荐使用 isinstance()。
type有9中。
>int，float，bool，complex，str(字符串)，list，dict(字典)，set，tuple

- issubclass
2个参数，是否是后一个参数的子类
- memoryview
主要作用是获取对象的内存视图对象，即对象的引用。无论将对象的全部或者部分赋值给他们对象，都不会创建新的对象，修改被赋值对象也直接会影响原对象的值。
>参数必须支持缓冲协议，一般常用的就是`bytes以及bytearray`，由bytes和bytearray生成的元素都是单字节的，而由其他类型（例如array.array）生成的可能包含更大的元素

可以看到d和z都是一个地址
```py
>>> z
b'a'
>>> memoryview(z)
<memory at 0x105ee4a10>
>>>

>>> d = z
>>> memoryview(z)
<memory at 0x105ee4d50>
>>> d
b'a'
>>> z
b'a'
>>> memoryview(d)
<memory at 0x105ee4d50>
```


- property
主要作用是设置类属性的方法，用于指定属性的获取、修改和删除的对应方法，可以增加对属性的限制，例如验证、过滤、二次处理等。也可以将这个函数理解为属性的“资源路由”，任何与这个属性有关的操作，都会被自动分配给对应的方法去处理。这个函数还可以用类的装饰器@property、@x.setter以及@x.deleter来替代（x为属性名）。
```py
>>> class User:
...     def __init__(self):
...         self._age = 0
...     @property
...     def age(self):
...         '这是设置年龄的property属性'
...         print('正在获取年龄属性')
...         return self._age
...     @age.setter
...     def age(self, value):
...         print('正在设置年龄属性')
...         self._age = value
...     @age.deleter
...     def age(self):
...         print('正在删除年龄属性')
...         del self._age
...
>>> u = User()
>>> u.age = 18
正在设置年龄属性
>>> u.age
正在获取年龄属性
18
>>> del u.age
正在删除年龄属性
```

## read more 
https://docs.python.org/zh-cn/3/library/functions.html
https://www.runoob.com/python/python-built-in-functions.html
https://www.zky.name/article/19.html