## 提示
`macOS`系统是出了名的安全性是很高的，最近我在升级到最新版本的系统之后10.15, 现在运行uPic软件程序的时候提示。
```
”upic将对您的电脑造成伤害。 您应该将它移到废纸篓。
```
下面就是讲一些解决方法。

## 解决方法

1. 用下面命令行手动签名方式
```
codesign --force --deep --sign - /Applications/uPic.app

```
![1](https://gitee.com/chasays/mdPic/raw/master/uPic/7Izrtv.png)

2. 设置软件覆盖恶意软件保护
访达-应用程序principle右键-显示简介-覆盖恶意软件保护 打勾就好了
![2](https://gitee.com/chasays/mdPic/raw/master/uPic/Ll6YOA.png)

3. 再次打开的时候就提示ok了
![3](https://gitee.com/chasays/mdPic/raw/master/uPic/irQ6RI.png)