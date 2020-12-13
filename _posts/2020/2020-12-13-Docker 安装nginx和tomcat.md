---
layout: post
title: "Docker 安装nginx和tomcat"
subtitle: '只要你肯坚持，才会体会到放弃的快乐'
author: "叉叉敌"
header-style: text
tags:
  - nginx
  - tomcat
  - docker
---

前一篇文章已经介绍过如何安装和使用 Docker。今天来实际操作下，安装tomcat和nginx。

## 拉取第一個docker鏡像

`docker pull hello-world` 拉取一个镜像
![](https://gitee.com/chasays/mdPic/raw/master/uPic/93Y7YG.png)

可以配置国内的一些镜像源，这样速度快多了。
https://hub-mirror.c.163.com
https://docker.mirrors.ustc.edu.cn




`docker images`查看镜像

`docker run hello-world`运行这个镜像

![](https://gitee.com/chasays/mdPic/raw/master/uPic/PxRpTy.png)

docker 架构图
![](https://gitee.com/chasays/mdPic/raw/master/uPic/ZWj9mz.jpg)


## 拉取一个nginx

`docker pull nginx` 用这个命令拉取一个最新的nginx镜像， 并运行`docker run nginx`

![](https://gitee.com/chasays/mdPic/raw/master/uPic/As37uE.png)

`docker exec -it xxx`进入到nginx镜像里面，然后执行命令`which nginx`

![](https://gitee.com/chasays/mdPic/raw/master/uPic/bN4ZFZ.png)

## 网络

`docker run -d -p 9090:80 nginx`后台-d运行一个nginx，并把本地的9090端口映射到nginx的80端口。
也可以用`docker run -d -P xx`用-P来随机映射一个端口

![](https://gitee.com/chasays/mdPic/raw/master/uPic/1Bsctx.png)

用`lsof -i:9090` 查看端口
![](https://gitee.com/chasays/mdPic/raw/master/uPic/577109.png)

![](https://gitee.com/chasays/mdPic/raw/master/uPic/pTssU2.png)

---

## Tomcat 的拉取和启动

tomcat的运行方式和nginx的类似
![](https://gitee.com/chasays/mdPic/raw/master/uPic/fBQcYS.png)


然后需要把war包传到 tomcat的运行目录下面

编写Dockerfile
```
FROM tomcat  # 启动镜像的名字
MAINTAINER xudong xxd0225@gmail.com # 维护信息
COPY jpress-v3.3.0.war /usr/local/tomcat/webapps  # 把当前目录的war包copy到tocat的目录下
```

开始制作一个images
`docker build .`这个之多的名字是none， 可以用tag来指定一个名字，注意名字要全部小写。
`docker build -t chasaystest:1.0 .`
![](https://gitee.com/chasays/mdPic/raw/master/uPic/AdDxUO.png)

然后运行
`docker run -d -P 1234:8080 chasaystest`。 这样就可以把tomcat 8080的映射到1234端口。本机用1234就可以访问tomcat端口。`http://localhost:1234`

![](https://gitee.com/chasays/mdPic/raw/master/uPic/nJeU0v.png)



