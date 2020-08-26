我听师傅在安装这个教程，我拖了很久了，应该我看应该是半年了。今天重新真正的把这个拖延症给搞定，然后执行起来，今天我就要彻底的要把这篇文章给写出来，写这篇文章主要的目的就是。避免踩一些坑，然后看里面有什么问题的话，然后自己遇到有什么问题，也会提出来，最后怎么去解决。
对于这类教程网上也有很多这样的一个教程，包括各方面的都有，他们的其实也非常的详细。所以说在安装这个方面的话，遇到问题大家不妨可以通过百度或者谷歌，有条件的可以通过谷歌去搜索安装教程，那也可以通过搜索有的关键字，然后就通过去搜索，希望这个问题是真的是能够解决的。

# 安装
这里推荐两个比较官方的安装文档，第1个是谷歌官方，第2个是。tf.wifi安装文档。
- https://tf.wiki/zh_hans/basic/installation.html
- https://tensorflow.google.cn/install

2个网址都不需要特殊的工具，只需要联网了就可以访问这个网址。
第1个安装就到这里就完了。你是一个想真心去学习，我相信安装是难不倒你的，所以说我这里就不再对安装做更多的一个分享。


# 填坑

- 使用 `pip install tensorflow` 来安装 TensorFlow，不过 python 源的版本往往更新较慢，难以第一时间获得最新的 TensorFlow 版本；

可以通过添加pip国内的一些镜像

```
阿里云 http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣(douban) http://pypi.douban.com/simple/
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
```
我就不冷炒饭了。替换方法可以参考, 
> https://developer.aliyun.com/article/652884

- TensorFlow 目前不支持32位了， 如果非的需要32bit的话， 可以参考 Anaconda 的安装方法


# 方法总比问题多！