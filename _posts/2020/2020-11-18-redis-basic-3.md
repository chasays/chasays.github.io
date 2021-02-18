---
layout: post
title: "学习 Redis - 3. 进阶"
subtitle: '只要你肯坚持，才会体会到放弃的快乐'
author: "叉叉敌"
header-style: text
tags:
  - redis
  - 大数据
---

![](https://gitee.com/chasays/mdPic/raw/master/uPic/LFKvwa.jpg)


----

## Redis 数据备份与恢复

备份
```
127.0.0.1:6379> SAVE
OK
```

备份还有一个在后台执行`bgsave`

```
127.0.0.1:6379> BGSAVE
Background saving started
```

该命令将在 redis 安装目录中创建`dump.rdb`文件。

安装目录可以用 `config get dir`获取到

```
127.0.0.1:6379> CONFIG GET dir
dir
/Users/admin/Dxxxx
```



-----

## Redis 安全
可以通过 redis 的配置文件设置`密码参数`，这样客户端连接到 redis 服务就需要密码验证，这样可以让你的 redis 服务更安全。
默认的密码是空，通过`config set requirepass`来设置密码。

```
127.0.0.1:6379> CONFIG GET requirepass
requirepass

127.0.0.1:6379> CONFIG SET requirepass "123"
OK
127.0.0.1:6379> CONFIG GET requirepass
requirepass
123
127.0.0.1:6379>
```

`如果没有授权成功是不可以执行命令的`。
比如下面先输入错误密码`1234`，然后执行命令失败， 然后输入正确密码`123`，执行成功。

```
(base) ➜  PYTHON redis-cli --raw
127.0.0.1:6379> AUTH 1234
WRONGPASS invalid username-password pair

127.0.0.1:6379> set test1 123
NOAUTH Authentication required.

127.0.0.1:6379> AUTH 123
OK
127.0.0.1:6379> set test1 123
OK
```

----
## Redis 性能测试

`redis-benchmark` 该命令是在 redis 的目录下执行的，而不是 redis 客户端的内部指令。

![](https://gitee.com/chasays/mdPic/raw/master/uPic/4FpRdc.png)

以下实例同时执行 100 个请求来检测性能：


```
(base) ➜  PYTHON redis-benchmark -n 100 -q
PING_INLINE: 50000.00 requests per second
PING_BULK: 25000.00 requests per second
SET: 33333.33 requests per second
GET: 33333.33 requests per second
INCR: 33333.33 requests per second
LPUSH: 50000.00 requests per second
RPUSH: 20000.00 requests per second
LPOP: 50000.00 requests per second
RPOP: 14285.71 requests per second
```

---

## Redis 管道技术

Redis是一种基于客户端-服务端模型以及请求/响应协议的TCP服务。这意味着通常情况下一个请求会遵循以下步骤：

- 客户端向服务端发送一个查询请求，并监听Socket返回，通常是以阻塞模式，等待服务端响应。
- 服务端处理命令，并将结果返回给客户端。


可以用` python redis`库来执行这个。设置了密码需要输入密码才可以访问可以操作。

```
>>> r = redis.StrictRedis(host="localhost", port=6379, password='123', db=0)
>>> r.set("111", '123')
True
```

---- 
## 总结

Redis常见的功能，有备份，设置密码，性能测试，以及管道技术，和其他语言的搭建脚本。

>[github博客](https://chasays.github.io/)
>微信公众号：chasays， 欢迎关注一起吹牛逼，也可以加微信号「xxd_0225」互吹。
