
前段时间和同事远程弄一个东西的时候，要提交git信息的时候，发现我这边输入不了ESC这个键，有可能这个远程程序和终端的esc 键冲突了。输入提交信息的时候，只能使用-m，但是这个问题，我在输入多行的时候，发现我是输入不了的，后来我在查阅相关文档之后，这个m是可以实现输入多行这个需求的。

在 `git`  里面，可以直接跟上` -m` 的参数可以实现提交信息。

```
git commit -m "this is the commit msg"
```

![8nIffs](https://gitee.com/chasays/mdPic/raw/master/uPic/8nIffs.png)

## 多个 -m 参数
如果是多行来提交，提交信息的话可以使用多个 `-m`。像下面这个代码就是提交多行，提交之后它的效果就是在显示作为多行的。

```
git commit -m "1. the first line" -m "2. the second line"

 ```

![Cnjygs](https://gitee.com/chasays/mdPic/raw/master/uPic/Cnjygs.png)


## 使用回车
还有一种情况就是使用。一个 -m，然后在里面使用 `回车`。然后通过回车，把需要的消息体加入到这个里面，打个双引号再返回，在这个里面体现的内容就是真正我们看的一个内容。

这里需要注意的是先打一个双引号，如果不是先打银行的话，可能会造成你输入不了回车，如果是直接回车了，可能他就提交了。然后把内容放到里面去，这个内容是我们所看到的那种，也是我们希望看到那个，然后在最后再把这个引号打回来。

```
git commit -m "
1. first line
2. second line
"
```



![tnGUwW](https://gitee.com/chasays/mdPic/raw/master/uPic/tnGUwW.png)


## 使用文件
通过上面有两种方式可以去实现多行提交，那还有一种方式就是。通过文件的方式，先把消息放到文件中，然后通过从标准输入读取文件，然后再放到我们的消息体里面去。
```
# cat msg
Summary: from local file
1. first line
2. second line
```
提交命令
```
git commit --file=msg
```
效果图
![NQY3Ap](https://gitee.com/chasays/mdPic/raw/master/uPic/NQY3Ap.png)

今天的学习就到这里。希望对你有所帮忙。