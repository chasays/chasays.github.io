---
layout: post
title: "可能提到Cydia的东西"
subtitle: '如何安装altstore'
author: "叉叉敌"
header-style: text
tags:
  - altStore
---

![Tfxtpb](https://gitee.com/chasays/mdPic/raw/master/uPic/Tfxtpb.png)


1. 开始邮件的管理插件功能

![9xWHps](https://gitee.com/chasays/mdPic/raw/master/uPic/9xWHps.png)

默认情况下是关闭的。
试了很多方法都不是很有用。主要的是需要在里面创建一个`Bundles`的目录。然后把插件解压后copy进去重启mail。
```
Quit the Mail application.
Go to the Finder
Hold the Option key and click on the Go menu
Choose Library
Navigate to the Mail directory in the Library directory
Drag MsgFilerPlugIn.mailbundle to Bundles folder in the Mail directory. `Create the Bundles folder `if it does not already exist.
If you have never used another Mail bundle, you will need to run the following commands in the Terminal application:
If you are using macOS 10.14 or higher, type:

sudo defaults write "/Library/Preferences/com.apple.mail" EnableBundles 1
defaults write com.apple.mail EnableBundles -bool true
defaults write com.apple.mail BundleCompatibilityVersion 4
```

![eTXN5H](https://gitee.com/chasays/mdPic/raw/master/uPic/eTXN5H.png)

参考这个连接：https://msgfiler.com/support/plugin/

2. 激活插件

插件有可能提示不兼容。参考如下。

sudo codesign -f -s - /Library/Mail/Bundles/AltPlugin.mailbundle

sudo spctl --master-disable



3. 使用


# 文档

https://altstore.io/faq/
