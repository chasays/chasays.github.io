---
layout: post
title: "Bash和sh的区别"
subtitle: 'sh比较常用'
author: "叉叉敌"
header-style: text
tags:
  - python
  - 线程
  - 通信
---
## sh

`Shell命令语言` 是 `POSIX` 标准描述的一种编程语言。它有许多的实现（ksh88，dash，...）。bash也可以视为的实现sh

![1](https://gitee.com/chasays/mdPic/raw/master/uPic/0CNeBA.png)
因为 `sh` 是规范，所以它/bin/sh是到大多数POSIX系统上实际实现的符号链接（或硬链接）。
## bash
`bash` 开始时是sh兼容的实现（尽管它比POSIX标准早了几年），但是随着时间的流逝，它获得了许多扩展。这些扩展中的许多扩展名可能会更改有效POSIX Shell脚本的行为，因此，它本身 `bash` 不是有效的 POSIX `Shell` 。相反，它是POSIX Shell语言的方言。


![2](https://gitee.com/chasays/mdPic/raw/master/uPic/zpR6Z0.png)
bash支持一个`--posix`开关，这使其更符合POSIX。如果以调用，它还会尝试模仿POSIX `sh`.



长期以来，`/bin/sh` 它一直指向` /bin/bash` 大多数GNU/Linux系统。结果，几乎可以忽略两者之间的区别了。但是这种情况最近开始改变。

/bin/sh不指向/bin/bash（某些/bin/bash甚至可能不存在）的系统的一些流行示例是：

- 现代Debian和Ubuntu系统，默认情况下符号链接sh到dash；
- Busybox，通常在Linux系统启动期间作为的一部分运行initramfs。它使用ashshell实现。
- BSD，通常是任何非Linux系统。OpenBSD使用pdkshKorn shell的后代。FreeBSD sh是原始UNIX Bourne shell的后代。Solaris拥有自己的产品sh，长期以来一直不符合POSIX。Heirloom项目提供了免费的实现。
您如何找出/bin/sh系统上的指向？

复杂之处在于它/bin/sh可能是符号链接或硬链接。如果它是一个符号链接，一种可解决的便携式方法是：
```
% file -h /bin/sh
/bin/sh: Mach-O 64-bit executable x86_64
```



如果是硬链接，请尝试
```
% find -L /bin -samefile /bin/sh
/bin/sh
```

![1](https://gitee.com/chasays/mdPic/raw/master/uPic/NsJucj.png)

实际上，该 `-L` 标志同时覆盖了符号链接和硬链接，但是此方法的缺点是它不可移植-POSIX 不需要 find支持该 -samefile选项，尽管GNU find和FreeBSD find都支持该选项。


最终，由您决定使用哪个脚本，方法是将“ shebang”行写为脚本的第一行。

例如
```
#!/bin/sh
```

将使用sh（以及碰巧指向的任何内容），
```
#!/bin/bash
```
将/bin/bash在可用的情况下使用（如果不可用，则会失败并显示错误消息）。当然，您也可以指定其他实现，例如
```
#!/bin/dash
```
## 使用哪一个？
对于我自己的脚本，`- ` 出于以下原因，我更喜欢：

- 它是标准化的
- 它更容易学习
- 它可以在POSIX系统之间移植-即使它们恰好没有bash，也必须具有sh
使用也有好处bash。它的功能使编程更加方便，并且类似于其他现代编程语言中的编程。这些包括范围局部变量和数组之类的东西。Plain sh是一种非常简约的编程语言。

>sh: http://man.cx/sh
>bash: http://man.cx/bash

