---
layout: post
title: "macOS Mysql8 重置用户密码"
subtitle: '配置Maven，Java，Spring'
author: "叉叉敌"
header-style: text
tags:
  - vscode
  - Maven
  - Spring
---
Mysql 8+ 修改密码好多命令都不太对。看了官方文档终于奏效了。

版本：
```
mysql -V
mysql  Ver 8.0.17 for macos10.14 on x86_64 (MySQL Community Server - GPL)
```

登录提示：
```
mysql -uuser -p
Enter password:
ERROR 1045 (28000): Access denied for user 'user'@'localhost' (using password: YES)
```

- 访问拒绝
- 密码错误

## 解决方法

```
SET PASSWORD FOR 'user'@'localhost' = 'password';
```

Microsoft SQL 和 Mysql 是不一样的。
用下面这个微软的去登录mysql使用提示不对，要么端口，或者网络问题。后来才发现这个
![2](https://gitee.com/chasays/mdPic/raw/master/uPic/9Vdf2i.png)
>mssql与mysql的有什么区别？哪个更好用？MySQL可以说是MSSQL的简化版本。理念相同，但MySQL的实现比MSSQL的需求低。MySQL是一个免费的、开放源代码的SQL数据库，所以免费的MYSQL很受欢迎，php+mysql，MySQL数据库专用于PHP网站的，一般用在PHP的网页上的，他和PHP可以说是黄金搭档（都是开源免费的东西）。对于不是特别大流量的网站，特别胜任,效率最高，MYSQL适合小、中型网站。mysql 是个开源的数据库Server,可运行在windows平台、unix、linux平台，其标准版是免费的，ASP.NET跟MYSQL不适合一起用，国内建站用PHP+MySQL+Apache很流行。

>MS SQL是微软推出的商用数据库系统，全称是Microsoft SQL Sever。，是微软的东东，都需要收钱的，所以贵些，目前的大型网站一般使用Oracle或者MSSQL，JSP.PHP.ASP都可以。一般是企业级的商务网站使用的。MS SQL Server 和ASP都是微软的产品， 互相兼容性最好， 所以ASP 网站用MS SQL Server 最好， 搭配！


用这个来访问Mysql就方便多了。
![2](https://gitee.com/chasays/mdPic/raw/master/uPic/nmr1td.png)

## read more
https://dev.mysql.com/doc/refman/8.0/en/set-password.html

