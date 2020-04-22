
>网址里面有个特殊字符%E2%80%8B

所见不一定是所得. 
今天终于活久见, 看上去是一样的, 但是实际就是不一样还差一个字符。
那看见下面一个图片，下面一个图片，嗯是返回的一串字符串，我要判断它们相等，肉眼看上去是完全相等的，但是实际上，它们是不相等的，所以在判断相等的时候始终返回嗯 `False` 。

 看上去是`2001603`，url编码是`2%E2%80%8B001603/` 。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200421170940929.png)

到底是什么原因造成的？我把获取到的字符串，通过 `ascii` 码编码之后。明显的看到有一个错误发生。在 `2 `这个数字后面。

```
str(path).split('/')[-1].encode('ascii')=='MAIN_HCP3_AU_ER_G55D_UNIT_DB_2001603'
```
发现在2这个数字后面，他有一个编码，Unicode编码是 `u200b` 。通过查询Unicode？可以知道这是一个0宽度的字符串。如果他表现出来就是没有宽度的，肉眼是看不见的。
>{UnicodeEncodeError}'ascii' codec can't encode character u'\u200b' in position 30: ordinal not in range(128)



## 解决
遇到这种问题怎么去解决？通过python，用python的方法encode去编码，用 assci 编码，然后忽略掉错误就可以了。
```
str(path).split('/')[-1].encode('ascii', 'ignore')=='MAIN_HCP3_AU_ER_G55D_UNIT_DB_2001603'
```
## 其他
那是其他的类似0宽度字符串还有如下几种方式。如果遇到同样的问题，还是用这个方法就可以解决

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200421171116262.png)
类似的还有
| Unicode code point | character UTF-8  |(hex.) name |
|  ----  | ----  | ----  |
|U+2000  |  e2 80 80|  EN QUAD| 
|U+2001   |e2 80 81 |EM QUAD|
|U+2002   |e2 80 82 |EN SPACE|
|U+2003   |e2 80 83 |EM SPACE|
|U+2004   |e2 80 84 |THREE-PER-EM SPACE|
|U+2005   |e2 80 85 |FOUR-PER-EM SPACE|
|U+2006   |e2 80 86 |SIX-PER-EM SPACE|
|U+2007   |e2 80 87 |FIGURE SPACE|
|U+2008   |e2 80 88 |PUNCTUATION SPACE|
|U+2009   |e2 80 89 |THIN SPACE|
|U+200A   |e2 80 8a |HAIR SPACE|
|U+200B  |e2 80 8b |ZERO WIDTH SPACE|
|U+200C  |e2 80 8c |ZERO WIDTH NON-JOINER|
|U+200D  |e2 80 8d |ZERO WIDTH JOINER|
|U+200E ‎ |e2 80 8e |LEFT-TO-RIGHT MARK|
|U+200F ‏ |e2 80 8f |RIGHT-TO-LEFT MARK|

>https://www.utf8-chartable.de/unicode-utf8-table.pl?start=8192&number=128
