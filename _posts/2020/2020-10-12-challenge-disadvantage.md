---
layout: post
title: "正视自己的不足"
subtitle: '更大的挑战'
author: "叉叉敌"
header-style: text
tags:
  - 不足
  - 挑战
  - 音频
---

# Audio
PESQ
NR 无参考
FR 全参考

# Video
POLQA PS 像素
- PSNR（峰值信噪比）：用得最多，但是其值不能很好地反映人眼主观感受。一般取值范围：20-40.值越大，视频质量越好。

- SSIM（结构相似性）：计算稍复杂，其值可以较好地反映人眼主观感受。一般取值范围：0-1.值越大，视频质量越好。

# ECNR
布局 混响
延时大小
单双讲

# 网络损伤
udp肯定会出现丢包


# 音视频原理
编码解码
h264 h265 opus vp8

# 基础
- the difference between thread and process


|Thread|Process|
----|----
进程中的一部分| 任何正在执行的程序
用较少的时间来终止| 用比线程更多的时间来终止
一个线程就是最小单位| 多个线程组成一个进程
线程间交互是高效| 进程间交互是相对低效
共享内存| 孤立的

- 定义方面：进程是程序在某个数据集合上的一次`运行活动`；`线程是进程中的一个执行路径`。 
- 角色方面：在支持线程机制的系统中，进程是`系统资源分配`的单位，线程是`系统调度`的单位。 
- 资源共享方面：进程之间`不能共享`资源，而`线程共享所在进程`的地址空间和其它资源。同时线程还有自己的栈和栈指针，程序计数器等寄存器。 
- 独立性方面：进程有自己独立的地址空间，而`线程没有`，线程必须依赖于进程而存在。
- 应用方面： 对于Python来说有GIL，因此`多线程用于I/O密集型场景`。

![1](https://gitee.com/chasays/mdPic/raw/master/uPic/hGOYGB.jpg)

- the difference between tcp and udp

|tcp|udp|
----|----
可靠、双工传输| 不可靠
面向连接传输| 面向数据传输，对于网络数据的广播非常有效（没有打开、维护、终止开销）
提供了流的控制和数据确认| 只有使用校验和基本的错误检查
按顺序送达|没有排序
tcp复杂，所以慢|udp快、简单、高效
重传| 不会重传
20~80字节可变长度|8字节的`固定`长度标头
重量级| 轻量级
不支持广播| 支持
http ftp | dns dhcp VoIP





- the difference between list and link

Type|list|link|
----|----|----
分配空间| 连续， 一次开辟，永久使用| 不连续， 链表存储数据时一次只开辟存储一个节点的物理空间，如果后期需要还可以再申请。
空间利用率| 利用高| 由于链表中每个数据元素都必须携带至少一个指针(前节点和后节点)
查找| 有下标O(1)|查找O(n)
插入和删除| O(n)| O(1)




- how to test real-time communication (focus on audio and media)





  

# read more
[IQA](https://sse.tongji.edu.cn/linzhang/IQA/IQA.htm)
[腾讯无参考质量评估在视频增强的进展与应用](https://blog.csdn.net/vn9PLgZvnPs1522s82g/article/details/97992210)

https://www2.tutormeetplus.com/v2/render/playback?mode=playback&token=0febd6ef28094bb0b9d7859a2e6c4f68
