---
layout: post
title: " 可视化压力测试工具- apache jmter"
subtitle: '特点是浏览器的控制脚本用 Python 来写'
author: "叉叉敌"
header-style: text
tags:
  - 压力测试
  - 工具
---

>Apache JMeter ™是开源软件，是一个 100% 纯 Java 应用程序，旨在`加载测试功能行为和测量性能`。它最初设计用于测试 Web 应用程序，但后来扩展到其他测试函数。


## 功能预览

能够加载和性能测试许多不同的应用程序/服务器/协议类型：
- Web - HTTP、HTTPS（Java、NodeJS、PHP、ASP.NET，...）
- REST Web 服务
- Ftp
- 通过 JDBC 的数据库
- Ldap
- 通过 JMS 面向消息的中间件 （MOM）
- 邮件 - SMTP（S）、POP3（S）和 IMAP（S）
- 本机命令或 shell 脚本
- Tcp
- Java 对象

`服务器和数据库`的性能测试的工具。此类测试使我们能够估计应用程序的`用户数量`，在舒适的条件下可以使用它，并使我们能够看到何时应该更改为更高效的服务器。此类测试还允许我们验证代码的哪些部分效率低下，需要重写。

[apache jmter](https://www.2n.pl/blog/apache-jmeter)

![aFxj2u](https://gitee.com/chasays/mdPic/raw/master/uPic/aFxj2u.jpg)

JMeter mock的`用户数量`。就我而言，是 20，000，因此我们还需要确定他们中有多少人应该以秒执行其任务。我认为 10 - 50 范围在这种情况下是合适的。因此，我们单击"线程组"并设置指定这些选项：

- 线程数 - 用于发送请求的线程数，
- 启动周期 - 发送请求的秒数，
- 循环计数 - 重复给定测试多少次，
- 延迟线程创建，直到需要 - 如果不选中此选项，JMeter 将立即为所有线程分配所有内存。这意味着，即使用户在 30 分钟后执行其示例，在运行脚本后也会立即为他保留内存，
- 调度程序 - 我们可以设置要运行测试的天和时间。

![DZIwhS](https://gitee.com/chasays/mdPic/raw/master/uPic/DZIwhS.jpg)


## read more 
https://jmeter.apache.org/
