---
layout: post
title: "Vscode 安装Java Spring项目"
subtitle: '配置Maven，Java，Spring'
author: "叉叉敌"
header-style: text
tags:
  - vscode
  - Maven
  - Spring
---
记一次二次开发Spring项目的，用vscode配置环境过程。因为vscode是用json文件保存的配置。好多都过时了。强行提笔记录一下

## 安装组件
一个java， 一个spring boot
![1](https://gitee.com/chasays/mdPic/raw/master/uPic/p2aGRp.png)


![2](https://gitee.com/chasays/mdPic/raw/master/uPic/j4jcE2.png)

## 安装Maven和Java
java这个简单
>https://java.com/zh_CN/download/help/mac_install.xml


maven
配置环境变量，如果是zshrc就用如下配置
```sh
# maven home
export M2_HOME=/Users/xxx/Documents/Maven
export PATH=$PATH:$M2_HOME/bin
# end
```

> http://maven.apache.org/download.cgi
主要是修改源为阿里
```
<!-- 阿里云仓库 -->
        <mirror>
            <id>alimaven</id>
            <mirrorOf>central</mirrorOf>
            <name>aliyun maven</name>
            <url>http://maven.aliyun.com/nexus/content/repositories/central/</url>
        </mirror>
        <mirror>
            <id>nexus-aliyun</id>
            <mirrorOf>*</mirrorOf>
            <name>Nexus aliyun</name>
            <url>http://maven.aliyun.com/nexus/content/groups/public</url>
        </mirror>
        <!-- 中央仓库1 -->
        <mirror>
            <id>repo1</id>
            <mirrorOf>central</mirrorOf>
            <name>Human Readable Name for this Mirror.</name>
            <url>http://repo1.maven.org/maven2/</url>
        </mirror>
 
        <!-- 中央仓库2 -->
        <mirror>
            <id>repo2</id>
            <mirrorOf>central</mirrorOf>
            <name>Human Readable Name for this Mirror.</name>
            <url>http://repo2.maven.org/maven2/</url>
        </mirror>
```

## 然后配置vscode配置maven
复制下面文件settings.json里面,修改自己的 `java.home` 以及maven地址
```json
"maven.excludedFolders": [
        "**/.*",
        "**/node_modules",
        "**/target",
        "**/bin",
        {
            "workbench.iconTheme": "vscode-icons",
            "workbench.startupEditor": "newUntitledFile",
            "java.errors.incompleteClasspath.severity": "ignore",
            "workbench.colorTheme": "Atom One Dark",
            "java.home":"/Library/Java/JavaVirtualMachines/jdk1.8.0_221.jdk/Contents/Home",
            "java.configuration.maven.userSettings": "/Users/admin/Documents/Maven/conf/settings.xml",
            "maven.executable.path": "/Users/admin/Documents/Maven/bin/mvn",
            "maven.terminal.useJavaHome": true,
            "maven.terminal.customEnv": [
                {
                    "environmentVariable": "JAVA_HOME",
                    "value": "/Library/Java/JavaVirtualMachines/jdk1.8.0_221.jdk/Contents/Home"
                }
            ],
        }
    ],
```

## 编译

在maven窗口右键点击 `install`即可。

![2](https://gitee.com/chasays/mdPic/raw/master/uPic/e25DjO.png)


## 运行
进入到vscode命令行
然后输入spring
![RfFRZY](https://gitee.com/chasays/mdPic/raw/master/uPic/RfFRZY.png)

选择需要引入的包，引入如下几个包即可满足web开发：

DevTools（代码修改热更新，无需重启）、Web（集成tomcat、SpringMVC）、Lombok（智能生成setter、getter、toString等接口，无需手动生成，代码更简介）、Thymeleaf （模板引擎）。

选择好要引入的包后直接回车，在新弹出的窗口中选择项目路径，至此Spring Boot项目创建完成。

![4](https://gitee.com/chasays/mdPic/raw/master/uPic/2NabmK.png)

如果是导入已经存在的Spring boot项目，则导入后在SPRING-BOOT DASHBOARD可以看到很多的server，右键就可以start或者debug了。

![1](https://gitee.com/chasays/mdPic/raw/master/uPic/xShkzS.png)

## read more

https://www.shuzhiduo.com/A/ke5jPDRgzr/