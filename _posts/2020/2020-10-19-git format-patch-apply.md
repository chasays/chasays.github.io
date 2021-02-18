---
layout: post
title: " A分支上的一个commit，merge到B分支"
subtitle: '有三种方法，diff,format-patch, cherry-pick'
author: "叉叉敌"
header-style: text
tags:
  - git
  - format-patch
  - 工具
  - cherry-pick
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

# git cherry-pick


`28c4904` 在 dev 上，如何把这个提交直接应用到其他分支上去， 
1. 首先切换到要应用的分支上，这里用master举例 `git checkout master`
2. 然后应用这个 commit， `git cherry-pick 28c4904`
3. 这个时候还没有完， 还需要 `git push origin master`
4. 然后看下这个，这个时候就完成了应用了。

![1](https://gitee.com/chasays/mdPic/raw/master/uPic/tktmXp.png)


![2](https://gitee.com/chasays/mdPic/raw/master/uPic/VAgzAf.png)

![3](https://gitee.com/chasays/mdPic/raw/master/uPic/TYagLM.png)

# 总结
把一个commit应用到其他分支上，有好几种方法，最简单的就是最后一种，其他2种，就用对应的`git am `或者  `git apply` 方法即可。