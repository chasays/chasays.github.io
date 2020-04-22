>远程连接 Ubuntu16.4 桌面

对于这个场景不是很多, 毕竟`Linux`天生的优势就是CLI, 但是有些软件是需要用户界面的软件才去操作，比如说Android studio, 就需要这样的东西。因此就需要远程桌面, 对于 `GUI` 的软件使用就变得非常重要了。

在网上搜了很多教程，都没有一个完整的教程，要么使用的就是不能联通，要么有些教程就是凌凌散散的。所以强心提笔总结一下是如何通过命令行去配置。

## 步骤
1. 安装xrdp
```
sudo apt-get install xrdp
```
2. 安装vnc4server
对于发行版的Ubuntu, vnc4server是已经安装好的，所以说我们就不需要手动去安装了，如果是其他版本，就需要手动安装。

3. 安装xfce4
这个软件比较大，网速快就几分钟。

```
sudo apt-get install xubuntu-desktop
```

4. 配置xfce4
创建.xsession文件并写入内容。
`echo "xfce4-session" >~/.xsession`


5. 继续配置xfce4
```
sudo vi /etc/xrdp/startwm.sh
在/etc/X11/Xsession 前一行插入
xfce4-session
```
6. 重启xrdp
`sudo service xrdp restart`

7. 配置好成功之后可以通过windows的远程桌面访问程序mstsc.exe，这个程序在开始里面搜索，其实是可以弹出来，是一个显示器的图标。输入 Linux 的用户名和密码就可以访问了。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200421112939602.png)


![在这里插入图片描述](https://img-blog.csdnimg.cn/20200421113001404.png?)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200421113018613.png?)

```
$ cat /etc/xrdp/startwm.sh
#!/bin/sh

if [ -r /etc/default/locale ]; then
  . /etc/default/locale
  export LANG LANGUAGE
fi

xfce4-session # 新加的
./etc/X11/Xsession
```

8. 配置自动补全
```
~$ diff ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml_bak 
118c118
<       <property name="&lt;Super&gt;Tab" type="empty"/> 
---
>       <property name="&lt;Super&gt;Tab" type="string" value="switch_window_key"/>
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200421165658822.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200421165200396.png?)

