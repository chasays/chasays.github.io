

## PowerToys
第一个是windows上的一个开源工具，它集成了非常多的实用工具。有桌面布局、文件预览、图片缩放等。

>Microsoft PowerToys 是一组免费的系统工具软件，由微软为Windows操作系统上的高级用户设计。这些程序为了使生产力达到最高，加入或变更了一些功能，或加入更多自定义选项。PowerToys可用于Windows 95、Windows XP和Windows 10。适用于Windows 10的PowerToys为自由及开放源代码软件，并使用MIT授权条款托管于GitHub。

在 `windows10` 下面是要用超级用户去运行，如果是普通用户的运行是有些功能是不可用的。

![1](https://gitee.com/chasays/mdPic/raw/master/uPic/zxrkgD.png)

用户自定义桌面，布局，主要是你在看多个文件的时候可以，如果现在屏幕都比较大，不用调整大小，只需要拖放到对应的一个表那个大小里面去了，不用你去手动调尺寸。

![2](https://gitee.com/chasays/mdPic/raw/master/uPic/gKiy01.png)

仅限于文件浏览器的预览窗格添加。预览窗格是文件资源管理器中的现有功能。要启用它，只需单击功能区中的“查看”选项卡，然后单击“预览窗格”。
PowerToys现在将允许预览两种类型的文件：Markdown（.md）和SVG（.svg）

![3](https://gitee.com/chasays/mdPic/raw/master/uPic/9jMSH8.png)

用于快速调整图像大小。从文件资源管理器中单击鼠标右键，即可立即调整一个或多个图像的大小。

![4](https://gitee.com/chasays/mdPic/raw/master/uPic/qwuzXM.png)

用于使用搜索和替换或正则表达式进行高级批量重命名。PowerRename允许简单搜索和替换或更高级的正则表达式匹配。在搜索和替换输入字段中键入内容时，预览区域将显示项目将重命名为的内容。然后，PowerRename调用Windows资源管理器文件操作引擎以执行重命名。这样的好处是允许在PowerRename退出后撤消重命名操作。

![5](https://gitee.com/chasays/mdPic/raw/master/uPic/tBUxEo.png)

可以帮助您使用简单的Alt空格立即搜索和启动您的应用程序并开始输入！它是开源的，用于其他插件的模块化。这个有点类似 Mac 下面的 `alfred`，非常方便。windows 下面也有同款是 wox。
不过对于那个自动计算的，我还是没搞懂，应该是调用的是python的一个库去计算的，但是在计算那个对数时候，总是出错。比如`log(10,10)`,结果应该是1，但是结果不是。

![6](https://gitee.com/chasays/mdPic/raw/master/uPic/p1hmDP.png)

## winget
是 `windows` 的软件包管理器服务，可以理解为 Ubuntu 下面的apt-get， centos下面的yum，以及mac下面的brew。估计后面结合 .appx 文件来安装非常的方便。

![7](https://gitee.com/chasays/mdPic/raw/master/uPic/v76VOU.png)

最近一个 Linux 项目，需要copy文件，之前只用的 xftp 协议。因为是嵌入式这个 xftp 已经被阉割了，所以只能用 scp 协议。我只需要在命令行输入`winget install winscp`, 过一会就开始自动安装了，不过还是需要点击下一步确认。希望以后是 appx 包的时候应该就不需要了。

![8](https://gitee.com/chasays/mdPic/raw/master/uPic/HXiH47.png)


## pipwin


<a href="https://pypi.org/project/pipwin/" style="color: rgb(0, 112, 201); display: block; margin-bottom: -1px;" _href="https://pypi.org/project/pipwin/"> <svg opacity="1" style="display: block; background-image: url(&quot;https://gitee.com/chasays/mdPic/raw/master/uPic/opYyHy.jpg&quot;); ;" xmlns="http://www.w3.org/2000/svg"> </svg> </a>


如果你是要在 windows 上经常使用 Python，那么在windows安装一些库，那可能会遇到一些问题，比如说安装 pythonnet（用Python去调用windows的DLL动态库。）、numpy、opencv-python等 ，就可能就会遇到错误，那这事怎么办？那你可以去安装一个pipiwn，你去安装第三方的库的时候, 就会减少很多不必要的错误。
`pipwin install pythonnet`

https://pypi.org/project/pipwin/

