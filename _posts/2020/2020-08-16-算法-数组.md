---
layout: post
title: "算法-数组"
subtitle: '数组、链表'
author: "叉叉敌"
header-style: text
tags:
  - 算法
  - 数组
  - 链表
---

# 什么是数组？

我估计你心中已经有了答案。不过，我还是想用专业的话来给你做下解释。数组（Array）是`一种线性表数据结构`。它用一组连续的内存空间，来存储一组具有相同类型的数据。


第一是线性表（Linear List）。顾名思义，线性表就是数据排成`像一条线一样的结构`。每个线性表上的数据最多只有前和后两个方向。其实除了数组，链表、队列、栈等也是线性表结构。


而与它相对立的概念是`非线性表`，比如二叉树、堆、图等。之所以叫非线性，是因为，在非线性表中，数据之间并不是简单的前后关系。

第二个是连续的内存空间和相同类型的数据。正是因为这两个限制，它才有了一个堪称“杀手锏”的特性：“`随机访问`”。

很多时候我们并不是要去死记硬背某个数据结构或者算法，而是要学习它背后的思想和处理技巧，这些东西才是最有价值的。如果你细心留意，不管是在软件开发还是架构设计中，总能找到某些算法和数据结构的影子。

## 访问越界问题

C 没有越界的限制,所有的内存空间都是可以自由访问的.
Java ArrayList 最大的优势就是可以将很多数组操作的细节封装起来。比如前面提到的数组插入、删除数据时需要搬移其他数据等。另外，它还有一个优势，就是支持动态扩容。

# 链表
它并不需要一块连续的内存空间，它通过“指针”将一组零散的`内存块串联起来`使用。与数组一样，链表也支持数据的查找、插入和删除操作。这个也是单向链表。链表本身没有大小的限制，天然地`支持动态扩容`。从普通的单链表衍生出来好几种链表结构，比如双向链表、循环链表、双向循环链表。


循环链表是一种特殊的单链表。实际上，循环链表也很简单。它跟单链表唯一的区别就在尾结点。


双向链表， 有next和pre节点。占用空间，速度快。

![1](https://gitee.com/chasays/mdPic/raw/master/uPic/e4XR4c.png)

LinkedHashMap 就是双向的数据设计。
用`空间换时间`的设计思想， 还是用时间换空间，取决于具体的项目。

双向循环链表。



对于内存要求严格的，使用数组。因为链表的每一个next和pre都需要内存来存储，都是需要空间的。

单项循环链表：
```py
# 定义链表中节点的属性
class Node:
    def __init__(self, initdata):
        self.__data = initdata
        self.__next = None

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setData(self, newdata):
        self.__data = newdata

    def setNext(self, newnext):
        self.__next = newnext

# 定义单向循环链表
class SinCycLinkedlist:
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(self.head)

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head.getNext()) # 设置临时node的data和next
        self.head.setNext(temp) # 把node对象设置为head的next

    def remove(self, item):
        prev = self.head
        while prev.getNext() != self.head:
            cur = prev.getNext()
            if cur.getData() == item:
                prev.setNext(cur.getNext()) # 把当前要移除的前一个next索引到其下一个，就跳过了 要移除的值，因此链表中就没有该值了
            prev = prev.getNext()

    def search(self, item):
        cur = self.head.getNext()
        while cur != self.head:
            if cur.getData() == item:
                return True
            cur = cur.getNext()

        return False

    def empty(self):
        return self.head.getNext() == self.head # 把尾和头连起来

    def size(self):
        count = 0
        cur = self.head.getNext()
        while cur != self.head:
            count += 1
            cur = cur.getNext() # 长度

        return count
```
## 对于写出来的代码检查是否正常

```
如果链表为空时，代码是否能正常工作？

如果链表只包含一个结点时，代码是否能正常工作？

如果链表只包含两个结点时，代码是否能正常工作？

代码逻辑在处理头结点和尾结点的时候，是否能正常工作？
```

你可以找一个具体的例子，`把它画在纸上`，释放一些脑容量，留更多的给逻辑思考，这样就会感觉到思路清晰很多。

这节我主要和你讲了写出正确链表代码的六个技巧。分别是理解指针或引用的含义、警惕指针丢失和内存泄漏、利用哨兵简化实现难度、重点留意边界条件处理，以及举例画图、辅助思考，还有多写多练。

我觉得，写链表代码是最考验逻辑思维能力的。因为，链表代码到处都是指针的操作、边界条件的处理，稍有不慎就容易产生 Bug。

## python的list和linkedlist区别

`python中list设计，其实和linkedlist的内存复杂度是一样的。 只有时间复杂度不一样。`

链表的删除和插入的时间复杂度都是 O(1)， 但是列表只有在结尾插入才是O(1),其他都是O(n)。

![2](https://gitee.com/chasays/mdPic/raw/master/uPic/VPgmC3.png)

其实python提供了一个 `deque` 库，就是链表的功能，插入和删除时间复杂度都是O(1)
```
>>> from collections import deque
>>> deque()
deque([])
>>> llist = deque("abcde")
>>> llist
deque(['a', 'b', 'c', 'd', 'e'])

>>> llist.append("f")
>>> llist
deque(['a', 'b', 'c', 'd', 'e', 'f'])

>>> llist.pop()
'f'

>>> llist
deque(['a', 'b', 'c', 'd', 'e'])
>>> llist.appendleft("z")
>>> llist
deque(['z', 'a', 'b', 'c', 'd', 'e'])

>>> llist.popleft()
'z'

>>> llist
deque(['a', 'b', 'c', 'd', 'e'])
```


# 作业
```
单链表反转

链表中环的检测

两个有序的链表合并

删除链表倒数第 n 个结点

求链表的中间结点
```

## 参考
python链表介绍：https://realpython.com/linked-lists-python/
关于python-list实现： http://www.laurentluce.com/posts/python-list-implementation/
python链表实现：https://www.cnblogs.com/russellluo/p/3285045.html