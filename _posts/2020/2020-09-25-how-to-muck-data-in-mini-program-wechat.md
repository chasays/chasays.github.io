---
layout: post
title: "如何用浏览器或者微信小程序开发Mock数据"
subtitle: '微信小程序mock数据'
author: "叉叉敌"
header-style: text
tags:
  - 微信小程序
  - mock数据
---

## 获取原始数据
点开IDE的调试窗口，然后和chrome一样，点开network，可以看到request。如果是数据太少，就自己可以生成一个手动写一个JSON格式的结果。

![1](https://gitee.com/chasays/mdPic/raw/master/uPic/LIV6eU.png)


## 设置mock
获取到数据之后，就可以模拟了， 

首先点击mock， 然后点击Mock右边有一个+ plus符号。
对应填写API接口类型，有request等还有可以mock支付相关的信息。
接着就是参数，url，后面的地址填写可以用通配符和正在表达。



![2](https://gitee.com/chasays/mdPic/raw/master/uPic/uKEplc.png)
上面这个数据生成的模板，主要有data和statusCode， code对应的就是httpResponseCode。
只要符合这个类型的都是返回指定的数据。
```json
{
  "data": {"errno":0,"data":{xxxx}},
  "statusCode": 200,
  "header": 123
}
```

比如进入到具体的页面，实际没有request，但是还是有数据的，数据就是我们刚刚mock的。

![3](https://gitee.com/chasays/mdPic/raw/master/uPic/53rGby.png)