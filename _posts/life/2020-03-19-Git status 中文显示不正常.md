## 问题
![5hcLZc](https://gitee.com/stormzhang/mdPic/raw/master/uPic/5hcLZc.png)

如上面，git status 看到自己修改的内容是编码后的内容。也不方便阅读和查看。
```shell
➜  Advanced-Test git:(master) ✗ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   "05_Others/02_\346\265\213\350\257\225\344\271\246\347\261\215.md"

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	"06_Attachments/01_Linux/Linux\345\270\270\347\224\250\345\221\275\344\273\24404 - ls.md"
	"06_Attachments/01_Linux/Linux\345\270\270\347\224\250\345\221\275\344\273\24405 - \346\226\207\346\234\254\350\277\275\345\212\240\345\210\260\346\226\207\344\273\266\344\270\255.md"

no changes added to commit (use "git add" and/or "git commit -a")
```

## 解决方法
```
git config --global core.quotepath false
```

然后在查看结果。
```
➜  Advanced-Test git:(master) ✗ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   05_Others/02_测试书籍.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	06_Attachments/01_Linux/Linux常用命令04 - ls.md
	06_Attachments/01_Linux/Linux常用命令05 - 文本追加到文件中.md

no changes added to commit (use "git add" and/or "git commit -a")
```

![fEL7NX](https://gitee.com/stormzhang/mdPic/raw/master/uPic/fEL7NX.png)