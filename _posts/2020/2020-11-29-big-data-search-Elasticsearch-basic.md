---
layout: post
title: "全文搜索引擎 Elasticsearch 入门教程"
subtitle: '大数据必备'
author: "叉叉敌"
header-style: text
tags:
  - Elasticsearch
  - 大数据
---


## 全文搜索是什么

>全文搜索引擎就是通过从互联网上提取的各个网站的信息（以网页文字为主）而建立的数据库中，检索与用户查询条件匹配的相关记录，然后按一定的排列顺序将结果返回给用户。

ES是一个基于 Lucene 库的搜索引擎。它提供了一个分布式的、支持多租户的全文搜索引擎，该引擎具有 HTTP web 界面和无模式的 JSON 文档。是用 Java 开发的。遵循开放核心业务模式，部分软件根据各种开放源码许可证(主要是 Apache 许可证)进行许可，而其他部分则根据专有(源码可用)弹性许可证进行许可。官方客户端可以在 Java，。NET (c #)、 PHP、 Python、 Apache Groovy、 Ruby 和许多其他语言。据 DB-Engines 排名，Elasticsearch 是最受欢迎的企业搜索引擎，其次是 Apache Solr，也是基于 Lucene 的.

![](https://gitee.com/chasays/mdPic/raw/master/uPic/aiIUBK.png)

---

## 安装

服务端，以macOS为例`brew install elasticsearch`

![](https://gitee.com/chasays/mdPic/raw/master/uPic/lRknOT.png)

安装好了直接运行 `curl localhost:9200`

![](https://gitee.com/chasays/mdPic/raw/master/uPic/6l2BVS.png)

上面代码中，请求9200端口，Elastic 返回一个 JSON `对象，包含当前节点、集群、版本等信息。`

>默认情况下，Elastic 只允许本机访问，如果需要远程访问，可以修改 Elastic 安装目录的`config/elasticsearch.yml`文件，去掉`network.host`的注释，将它的值改成0.0.0.0，然后重新启动 Elastic。

客户端，以python为例

`python -m pip install elasticsearch`
![](https://gitee.com/chasays/mdPic/raw/master/uPic/2ccCLd.png)
---

## 基本概念

Elastic 本质上是一个分布式数据库，允许多台服务器协同工作，每台服务器可以运行多个 Elastic 实例。

单个 Elastic 实例称为一个`节点`（`node`）。一组节点构成一个`集群`（c`luster`）。

Elastic 会索引所有字段，经过处理后写入一个反向索引（Inverted Index）。查找数据的时候，直接查找该索引。

所以，Elastic 数据管理的顶层单位就叫做 `Index（``索引`）。它是单个数据库的同义词。每个 Index （即数据库）的名字必须是小写。

Index 里面单条的记录称为 `Document`（文档）。许多条 Document 构成了一个 Index。

Document 可以分组，比如weather这个 Index 里面，可以按城市分组（北京和上海），也可以按气候分组（晴天和雨天）。这种分组就叫做 `Type`，它是虚拟的逻辑分组，用来过滤 Document。

`http://localhost:9200/_mapping?pretty=true` 这个命令可以列出每个 Index 所包含的 Type。

![](https://gitee.com/chasays/mdPic/raw/master/uPic/McqMu9.png)

## 基本操作 新建和删除

`新建` Index，可以直接向 Elastic 服务器发出 PUT 请求。下面的例子是新建一个名叫weather的 Index。

服务器返回一个 JSON 对象，里面的acknowledged字段表示操作成功。


```
$ url -X PUT 'localhost:9200/weather'
{"acknowledged":true,"shards_acknowledged":true,"index":"weather"}%

```

然后，我们发出 DELETE 请求，删除这个 Index。

```
curl -X DELETE 'localhost:9200/weather'
{"acknowledged":true}%
```
-------
## 中文分词 （选）
要安装和elasticsearch版本匹配的。安装命令`elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/xxxx.zip`
>https://github.com/medcl/elasticsearch-analysis-ik/releases

![](https://gitee.com/chasays/mdPic/raw/master/uPic/RPTr1g.png)
新建一个 account 的index `curl -X PUT 'localhost:9200/accounts' -H 'Content-Type: application/json'  -d '`， person是Type。

```
curl -X PUT 'localhost:9200/accounts' -H 'Content-Type: application/json'  -d '
{
  "mappings": {
    "person": {
      "properties": {
        "user": {
          "type": "text",
          "analyzer": "ik_max_word",
          "search_analyzer": "ik_max_word"
        },
        "title": {
          "type": "text",
          "analyzer": "ik_max_word",
          "search_analyzer": "ik_max_word"
        },
        "desc": {
          "type": "text",
          "analyzer": "ik_max_word",
          "search_analyzer": "ik_max_word"
        }
      }
    }
  }
}'

{"error":{"root_cause":[{"type":"resource_already_exists_exception","reason":"index [accounts/_tFhzXBbTvakegDC4k64TQ] already exists","index_uuid":"_tFhzXBbTvakegDC4k64TQ","index":"accounts"}],"type":"resource_already_exists_exception","reason":"index [accounts/_tFhzXBbTvakegDC4k64TQ] already exists","index_uuid":"_tFhzXBbTvakegDC4k64TQ","index":"accounts"},"status":400}%
```

-----
## 数据操作

在account里面，`新增`一条记录
```
curl -X PUT -H 'Content-Type: application/json' 'localhost:9200/accounts/person/1' -d '
{
  "user": "张三",
  "title": "工程师",
  "desc": "数据库管理"
}'
{"_index":"accounts","_type":"person","_id":"1","_version":2,"result":"updated","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":1,"_primary_term":2}
```
>如果你仔细看，会发现请求路径是`/accounts/person/1`，最后的1是该条记录的 Id。`它不一定是数字`，任意字符串（比如abc）都可以。

`新增`记录的时候，也可以不指定 Id，这时要改成 `POST` 请求。
```
curl -X POST -H 'Content-Type: application/json' 'localhost:9200/accounts/person/' -d '
{
  "user": "张三",
  "title": "工程师",
  "desc": "数据库管理"
}'
{"_index":"accounts","_type":"person","_id":"5vzIE3YBFWECnAW261hs","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":2,"_primary_term":2}

```

>注意，如果没有先创建 Index（这个例子是accounts），直接执行上面的命令，Elastic 也不会报错，而是直接生成指定的 Index。所以，打字的时候要小心，`不要写错 Index 的名称`。

新增了后，`查询`记录`curl 'localhost:9200/accounts/person/1?pretty=true'`


```
curl 'localhost:9200/accounts/person/1?pretty=true'
{
  "_index" : "accounts",
  "_type" : "person",
  "_id" : "1",
  "_version" : 2,
  "_seq_no" : 1,
  "_primary_term" : 2,
  "found" : true,
  "_source" : {
    "user" : "张三",
    "title" : "工程师",
    "desc" : "数据库管理"
  }
}
```
返回的数据中，found字段表示查询成功，_source字段返回原始记录。


如果 Id 不正确，就查不到数据，found字段就是false。


```
curl 'localhost:9200/accounts/person/32?pretty=true'
{
  "_index" : "accounts",
  "_type" : "person",
  "_id" : "32",
  "found" : false
}
```
`更新`记录就是使用 PUT 请求，重新发送一次数据。

```
curl -X PUT 'localhost:9200/accounts/person/1' -H 'Content-Type: application/json' -d '
{
    "user" : "张三",
    "title" : "工程师",
    "desc" : "数据库管理，软件开发"
}'
{"_index":"accounts","_type":"person","_id":"1","_version":3,"result":"updated","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":3,"_primary_term":2}
```
可以看到，上面更新记录的 Id 没变，但是版本（`version`）从2变成3，操作类型（`result`）从created变成updated，`created`字段变成false，因为这次不是新建记录。

查询更新成功没， 更新成功。 
![](https://gitee.com/chasays/mdPic/raw/master/uPic/eoKLJ7.png)


查询所有的记录。

```
curl 'localhost:9200/accounts/person/_search'
{"took":57,"timed_out":false,"_shards":{"total":1,"successful":1,"skipped":0,"failed":0},"hits":{"total":{"value":2,"relation":"eq"},"max_score":1.0,"hits":[{"_index":"accounts","_type":"person","_id":"1","_score":1.0,"_source":
{
    "user" : "张三",
    "title" : "工程师",
    "desc" : "数据库管理，软件开发"
}},{"_index":"accounts","_type":"person","_id":"5vzIE3YBFWECnAW261hs","_score":1.0,"_source":
{
  "user": "张三",
  "title": "工程师",
  "desc": "数据库管理"
}}]}}
```

`上面字段的含义`
- total：返回记录数，本例是2条。
- max_score：最高的匹配程度，本例是1.0。
- hits：返回的记录组成的数组。

返回的记录中，每条记录都有一个_score字段，表示匹配的程序，默认是按照这个字段降序排列。

`带有参数查询` query， 默认是10条记录，可以设置size和from。

>官方说明文档： https://www.elastic.co/guide/en/elasticsearch/reference/5.5/query-dsl-match-query.html

```
curl 'localhost:9200/accounts/person/_search' -H 'Content-Type: application/json'  -d '
{
  "query" : { "match" : { "desc" : "软件" }}
}'
{"took":28,"timed_out":false,"_shards":{"total":1,"successful":1,"skipped":0,"failed":0},"hits":{"total":{"value":1,"relation":"eq"},"max_score":1.241217,"hits":[{"_index":"accounts","_type":"person","_id":"1","_score":1.241217,"_source":
{
    "user" : "张三",
    "title" : "工程师",
    "desc" : "数据库管理，软件开发"
}}]}}
```

有支持逻辑运算，如果有多个搜索关键字， Elastic 认为它们是`or`关系。

下面代码搜索的是软件 or 系统。

```
curl 'localhost:9200/accounts/person/_search'  -d '
{
  "query" : { "match" : { "desc" : "软件 系统" }}
}'
```

还有 `and` 的查询， 下面就是and的操作
```
curl 'localhost:9200/accounts/person/_search'  -d '
{
  "query": {
    "bool": {
      "must": [
        { "match": { "desc": "软件" } },
        { "match": { "desc": "系统" } }
      ]
    }
  }
}'
```



`删除`记录
```
curl -X DELETE 'localhost:9200/accounts/person/1'
{"_index":"accounts","_type":"person","_id":"1","_version":4,"result":"deleted","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":4,"_primary_term":2}
```


----
## readmore
https://www.elastic.co/blog/a-practical-introduction-to-elasticsearch

https://www.ruanyifeng.com/blog/2017/08/elasticsearch.html

https://en.wikipedia.org/wiki/Elasticsearch

https://elasticsearch-py.readthedocs.io/en/7.10.0/


>[github博客](https://chasays.github.io/)
>微信公众号：chasays， 欢迎关注一起吹牛逼，也可以加微信号「xxd_0225」互吹。
