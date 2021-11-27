---
layout: post
title: "构建 Python CLI参数，还在用 argparse ?"
subtitle: ''
author: "叉叉敌"
header-style: text
tags:
  - python
  - typer
---

![](https://gitee.com/chasays/mdPic/raw/master/uPic/wMu9OW.jpg)


# 构建 CLI 参数 --name
Python `argparse` 库可以方便我们添加命令行界面，但是有点复杂，代码有点多，且长。

https://docs.python.org/3/library/argparse.html#module-argparse

```python
import argparse

def greeting(name: str):
    print(f'Hello {name}!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Greet users')
    parser.add_argument('--name', type=str)
    args = parser.parse_args()

    if args.name:   
        greeting(args.name)
```

先要定义一个`greeting`方法，然后再通过argparse 的一系列方法就是实现一个 `add_argument` 参数，

```sh
$ python 20211108argparse.py -h
usage: Greet users [-h] [--name NAME]

optional arguments:
  -h, --help   show this help message and exit
  --name NAME


$ python argparse.py -name RikXiao
Hello risss!
```

# 一行搞定 - typer

`Typer` 是一个用于构建CLI应用程序的库。基于Python 3.6+类型提示。

![](https://gitee.com/chasays/mdPic/raw/master/uPic/sjdDdE.png)

- 书写直观：调试耗时少
- 易于使用：shell等自动完成
- 简短： 最小化代码搞定
- 强大：可以随心所欲的增加复杂性

先安装 typer 库，`pip install typer`，记得用python3.6+。

下面就用 typer 一行来搞定上面的实现。
```py
import typer 

def greeting(name: str):
    print(f'Hello {name}!')

if __name__ == '__main__':
    typer.run(greeting)
```

然后在命令行执行，`--help` 输出的参数，非常的完整。

```sh
$ python 20211108argparse.py --help      
Usage: 20211108argparse.py [OPTIONS] NAME

Arguments:
  NAME  [required]

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.
```

执行这个函数。

```sh
$ python 20211108argparse.py rik
Hello rik!
```

## 为参数添加说明


修改下这个函数的帮助说明，添加一行`this function to say hello xxx`

```py

def greeting(name: str):
    """this function to say hello xxx"""
    print(f'Hello {name}!')

```

执行help命令。
```sh
./20211108argparse.py --help
Usage: 20211108argparse.py [OPTIONS] NAME

  this function to say hello xxx
```

## 高级用法

username 是一个变量参数，然后再添加一个time是一个可选参数，

```py

import typer

def greeting(name: str = typer.Argument(..., help='Username'),
             time: int = typer.Option(8, help='Whether user has signed up')):
    """Say hello to users"""
    if time < 12:
        print(f'Good morning {name}!')
    elif time >= 12 and time < 18:
        print(f'Good afternoon {name}!')
    else:
        print(f"Good evening {name}")


if __name__ == '__main__':
    typer.run(greeting)
```


执行 --help 之后，可以看到的结果。
```sh
Arguments:
  NAME  Username  [required]

Options:
  --time INTEGER                  Whether user has signed up  [default: 8]
```

还有其他用法，可以参见 typer 的官网，用一行代码就搞定参数的设置。