在 `git`  里面，可以直接跟上` -m` 的参数可以实现提交信息。

```
git commit -m "this is the commit msg"
```

![8nIffs](https://gitee.com/chasays/mdPic/raw/master/uPic/8nIffs.png)


如果是多行来提交，提交信息的话可以使用多个 `-m`。像下面这个代码就是提交多行，提交之后它的效果就是在显示作为多行的。

```
git commit -m "1. the first line" -m "2. the second line"

 ```

![Cnjygs](https://gitee.com/chasays/mdPic/raw/master/uPic/Cnjygs.png)

还有一种情况就是使用。一个 -m，然后在里面使用 `回车`。然后通过回车，把需要的消息体加入到这个里面，打个双引号再返回，在这个里面体现的内容就是真正我们看的一个内容。

这里需要注意的是先打一个双引号，如果不是先打银行的话，可能会造成你输入不了回车，如果是直接回车了，可能他就提交了。然后把内容放到里面去，这个内容是我们所看到的那种，也是我们希望看到那个，然后在最后再把这个引号打回来。



