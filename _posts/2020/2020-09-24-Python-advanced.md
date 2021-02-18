---
layout: post
title: "Python进阶"
subtitle: '向高手学习学习'
author: "叉叉敌"
header-style: text
tags:
  - Python
  - 进阶
---
课程连接：
>https://time.geekbang.org/column/intro/176

## 开篇
- 从工程角度掌握Python高阶用法；
- 独立开发Python项目的能力；
- 硅谷一线工程师的独家经验分享；
- 完整的Python学习路径。

## 基础

### IDE
Jupyter 的三大特点：整合所有的资源、交互性编程体验和零成本重现结果。


### 元组和列表
列表是动态的，长度可变，可以随意的增加、删减或改变元素。列表的存储空间略大于元组，性能略逊于元组。
元组是静态的，长度大小固定，不可以对元素进行增加、删减或者改变操作。元组相对于列表更加`轻量级，性能稍优`。

### 字典和集合

集合的pop()操作是删除集合中最后一个元素，可是集合本身是无序的，你无法知道会删除哪个元素，因此这个操作得谨慎使用。

字典和集合都是无序的数据结构，其内部的哈希表存储结构，保证了其查找、插入、删除操作的高效性。所以，字典和集合通常运用在对元素的`高效查找、去重`等场景。

### 字符串

- Python中字符串使用单引号、双引号或三引号表示，三者意义相同，并没有什么区别。其中，三引号的字符串通常用在多行字符串的场景。
- Python中字符串是不可变的（前面所讲的新版本Python中拼接操作’+='是个例外）。因此，随意改变字符串中字符的值，是不被允许的。
- 拼接用 `‘’.join() `或者用 `+` 
- Python中字符串的格式化（string.format）常常用在输出、日志的记录等场景。


### 输入和输出
- I/O	操作需谨慎，一定要`进行充分的错误处理`，并细心编码，防止出现编码漏洞；
- 编码时，对内存`占用和磁盘占用`要有充分的估计，这样在出错时可以更容易找到原因；
- JSON序列化是很方便的工具，要结合实战多多练习；
- 代码尽量简洁、清晰，哪怕是初学阶段

思考

```py
## in.txt	可能非常非常大（意味着你不能一次读取到内存中），而	output.txt	不会很大（意味着重复的单词数量很多）。

## 遍历 用一个迭代器
with open("in.txt") as infile:
    for line in infile:
        do_something_with(line)

## 读取的时候指定大小
with open('in.txt', 'rb') as f:
    while True:
        buf = f.read(1024)
        if buf: 
            ...
        else:
            break


## defaultdict

from	collections	import	defaultdict
import	re
f = open("ini.txt", mode="r", encoding="utf-8")
d = defaultdict(int)
for line in f:
  for word in filter(lambda x: x, re.split(r"\s", line)):
    d[word] += 1
print(d) ## 统计每个字符的多少个
```




## 进阶
### 比较和拷贝


## 规范
### 代码风格？

## 实战

### 量化

