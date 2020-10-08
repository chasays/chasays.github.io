---
layout: post
title: "Python list 实现"
subtitle: '看看底层是怎么实现的'
author: "叉叉敌"
header-style: text
tags:
  - python
  - list
---
## List 对象的C结构
CPython 中的列表对象由以下 C 结构表示。ob_item是指向列表元素的指针列表。分配的是内存中分配的插槽数。
```c
typedef struct {
    PyObject_VAR_HEAD
    PyObject **ob_item;
    Py_ssize_t allocated;
} PyListObject;
```

## 初始化list
比如初始化一个空的数组 l = []
```py
arguments: size of the list = 0
returns: list object = []
PyListNew:
    nbytes = size * size of global Python object = 0
    allocate new list object
    allocate list of pointers (ob_item) of size nbytes = 0
    clear ob_item
    set list's allocated var to 0 = 0 slots
    return list object
```
注意分配的slot和size是不同的，这个size就是len(), 分配的slot其实就是内存大小。所以经常看到分配的是大于这个size的，因为避免每次追加的时候都重新分配内存。

## append 功能

append一个整数到list里面, l.append(1)
```py
arguments: list object, new element
returns: 0 if OK, -1 if not
app1:
    n = size of list
    call list_resize() to resize the list to size n+1 = 0 + 1 = 1
    list[n] = list[0] = new element
    return 0

```
上面有4个slot被分配来扩容，只有第一个l[0]指向了刚刚追加的元素。虚线下面的表示分配了没有使用。
可以看出时间复杂度是o(1)
![1](https://gitee.com/chasays/mdPic/raw/master/uPic/HZmZxC.jpg)

既然有分配多的空间，那就继续append更多的值。
![1](https://gitee.com/chasays/mdPic/raw/master/uPic/QxHbBK.jpg)


## insert 功能

在1的位置插入一个数字l.insert(1,5)
```c
arguments: list object, where, new element
returns: 0 if OK, -1 if not
ins1:
    resize list to size n+1 = 5 -> 4 more slots will be allocated
    starting at the last element up to the offset where, right shift each element
    set new element at offset where
    return 0

```
同样的 虚线下面是分配了没用使用的。总共有8个slots，但是只有5个长度，看到时间复杂度是O(n)
![3](https://gitee.com/chasays/mdPic/raw/master/uPic/Tm9heQ.jpg)

## pop 功能
默认移除最后一个元素，并返回该值。
如果list的pop移除后的大小 小于 分配的一半的话，这个list就减少。
下面刚好是一半，不小于，所以分配大小不变
时间复杂度是O(1)
```c
arguments: list object
returns: element popped
listpop:
    if list empty:
        return null
    resize list with size 5 - 1 = 4. 4 is not less than 8/2 so no shrinkage
    set list object size to 4
    return last element
```
![4](https://gitee.com/chasays/mdPic/raw/master/uPic/KJAgqh.jpg)

如果再移除一个元素就小于一半了，则分配大小就是减少后的大小的一半。所以分配大小就是6 slots
可以看到 位置3和4仍然是指向空的。
![5](https://gitee.com/chasays/mdPic/raw/master/uPic/q89iB2.jpg)


## remove 功能
指定元素移除。l.remove(1), listremove() 被调用。
```c
arguments: list object, element to remove
returns none if OK, null if not
listremove:
    loop through each list element:
        if correct element:
            slice list between element's slot and element's slot + 1
            return none
    return null
```
为了切片和移除元素，list_ass_slice()这个被调用
```c
arguments: list object, low offset, high offset
returns: 0 if OK
list_ass_slice:
    copy integer 5 to recycle list to dereference it
    shift elements from slot 2 to slot 1
    resize list to 5 slots
    return 0
```
![6](https://gitee.com/chasays/mdPic/raw/master/uPic/Wth5IA.jpg)
remove的时间负责度是O(n)。


## readmore
https://docs.python.org/3/c-api/list.html
http://www.laurentluce.com/posts/python-list-implementation/