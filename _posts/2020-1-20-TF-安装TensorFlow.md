
> `TensorFlow`是一个端到端开源机器学习平台。它拥有一个包含各种工具、库和社区资源的全面灵活生态系统，可以让研究人员推动机器学习领域的先进技术的。

# 准备

## 安装 Anaconda


`TensorFlow` 安装的前提是系统安装了 Python 2.5 或更高版本，教程中的例子是以 Python 3.6（Anaconda 3 版）为基础设计的。为了安装 `TensorFlow`，首先确保你已经安装了 Anaconda。可以从网址（https://www.anaconda.com/distribution/#download-section）中下载并安装适用于 Windows/macOS 或 Linux 的 Anaconda。

> 这个是`macos`的连接，一个是命令行的，一个是GUI的
>
> https://repo.anaconda.com/archive/Anaconda3-2019.10-MacOSX-x86_64.sh
>
> https://repo.anaconda.com/archive/Anaconda3-2019.10-MacOSX-x86_64.pkg


关于安装 `anaconda`， 可以参考官方的文档。
>https://docs.anaconda.com/anaconda/install/
---

## 配置 Anaconda
执行这个命令`source ~/.bash_profile`， 其实查看这个文件`.bash_profile`，关键的信息`export PATH="/opt/anaconda3/bin:$PATH"`，就是配置anaconda的环境变量。
然后执行`conda -V`
>(base) ➜  OpenSource conda -V  
>conda 4.7.12





# 安装

## 配置 pip 源

这一步可以省略，但是配置为国内的源之后，速度快的飞起来。
`sudo vi /Users/`username`/Library/Application\ Support/pip/pip.conf`，然后修改里面的内容为下面的源。
``` 
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple/
[install]
trusted-host=pypi.tuna.tsinghua.edu.cn
```
保存退出即可。

## 安装

当前版本只支持 CPU
> pip install https://storage.googleapis.com/tensorflow/mac/tensorflow-0.5.0-py2-none-any.whl\
或者干脆直接用`pip install tensorflow`一样的。


# Hello TensorFlow

这是第一个程序
```python
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

# Hello, TensorFlow!
```