---
layout: post
title: " git format-patch 应用"
subtitle: '把A分支上的一个commit，merge到B分支'
author: "叉叉敌"
header-style: text
tags:
  - git
  - format-patch
  - 工具
---

场景就是要解决的问题，就是把B分支的一个commit，单独merge到A分支上面去。

思路是生成一个patch，然后把这个patch应用到要merge的分支。

有2种方式，一种是`git format-patch`，然后用 `git am `应用。还有一种就是`git diff`, 切换分支后，`git apply`.推荐前一种，前一种是包含了邮件格式。

# git format-patch

用法， `git format-patch -n` ,这个n就是最上面的n个commit。

```git
$ git format-patch -1 # 
0001-update-missing-error.patch
git checkout master
git am < 0001-update-missing-error.patch
```

# git diff

就是在2个commit中间生成一个patch， `git diff commit2 commit1 > patch`，然后用git apply

```git
git diff 123a 3242 >> 1.patch
git checkout dev
git apply 1.patch
```

第一种比较好，简单，直接就生成对应的patch名字。在实际生成环境中去解决问题。