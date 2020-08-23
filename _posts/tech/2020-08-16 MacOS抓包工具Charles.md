抓包工具有wireshark， tcpdump， 还有就是Charles。

今天分享的是最后一个Charles。抓包分2个， 一个是移动端的，一个是macOS自带的应用。

# 安装Charles
https://www.charlesproxy.com/latest-release/download.do
这里有官方最新的包， 不过启动后有提示。也有符合社会主义特殊的软件

```
# 替换 包里面的charles.jar包

# 还有就是直接输入分享的license
Registered Name: https://zhile.io
License Key: 48891cf209c6d32bf4

# 还有在线生成key license的
https://www.charles.ren/
```

# 开始配置

## 本地配置代理
在本地网络设置里面配置代理为`127.0.0.1 8888`。
![1](https://gitee.com/chasays/mdPic/raw/master/uPic/1DS5NM.png)
![2](https://gitee.com/chasays/mdPic/raw/master/uPic/C3zUCm.png)

## Charles配置
勾选macOS proxy
![3](https://gitee.com/chasays/mdPic/raw/master/uPic/8HntiW.png)

## 对于SSL的proxy需要安装证书
安装ssl
![4](https://gitee.com/chasays/mdPic/raw/master/uPic/xHRhBc.png)
配置代理
![5](https://gitee.com/chasays/mdPic/raw/master/uPic/ir1FPA.png)

这里是支持通配符的。
![6](https://gitee.com/chasays/mdPic/raw/master/uPic/6ogCWo.png)

#  macOS开启recording

在这里就可以看到所有的抓包了， 如果电脑其他软件配置的不是这个port的话，是抓不到的。
![7](https://gitee.com/chasays/mdPic/raw/master/uPic/MKCYXC.png)


# 手机Recording

手机抓包只是多了一个步骤，就是需要在安装证书的，证书这是第1个。
第2个就是在你连接的WiFi，这个WiFi和你的笔记本电脑是同一个局域网，还有就是手机连接的WiFi要手动设置一个代理，这个代理的话是你电脑的IP端口的话也是8888。这样就可以了。

## 先配置手机的ip代理

## 然后在macOS上点击如下安装证书到手机上，安装的时候电脑上的Charles不要关闭。

![8](https://gitee.com/chasays/mdPic/raw/master/uPic/Rz1a9X.png)

这个时候手机会提示一句下载好了，需要到通用-》设备管理里面去点击安装即可。
![9](https://gitee.com/chasays/mdPic/raw/master/uPic/PyY2Kx.png)

![uA7HWv](https://gitee.com/chasays/mdPic/raw/master/uPic/uA7HWv.png)
![MFfXYy](https://gitee.com/chasays/mdPic/raw/master/uPic/MFfXYy.png)


# 总结
安装好证书就可以用了，用的话就在手机或者macos上访问对应的软件或是网址，然后就通过Charles，就可以获取到他们的信息，他都要header，返回值，response都可以看到。