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


## read more
https://dev.mysql.com/doc/refman/8.0/en/set-password.html

