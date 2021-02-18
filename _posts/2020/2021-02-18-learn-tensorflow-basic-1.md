---
layout: post
title: "TensorFlow 基础学习 - 1"
subtitle: 'y=2x-1，如何训练'
author: "叉叉敌"
header-style: text
tags:
  - TensorFlow
---

## 学习目的

了解机器学习的一些基础功能，一些基础用法，然后在我们的实际工作中创造出更多的火花。

![](https://gitee.com/chasays/mdPic/raw/master/uPic/FJmVc4.png)


## 环境准备

环境话有很多，我在学习的这个慕课的实验室、谷歌实验室。还有腾讯实验室都可以用来做，也非常方便，本地环境搭建也是非常的方便，但是在训练数据多的时候，那就非常的慢。

`这些实验室提供强大的算力，最主要的还是免费。`


- https://ot.icourse163.org/#/lab
- https://colab.research.google.com/notebooks/intro.ipynb



![](https://gitee.com/chasays/mdPic/raw/master/uPic/u19dtY.png)

## 实例

![](https://gitee.com/chasays/mdPic/raw/master/uPic/0q6RdJ.png)

`定义神经网络的框架叫做keras`，它将神经元网络模型定义为一组Sequential层。Keras库也需要导入。

然后我们导入一个名为`numpy的库`，它可以帮助我们方便快捷地将数据`表示为列表`。

在编译神经网络时，我们`必须指定2个函数`：一个损失函数和一个优化器。

如果我们读过很多有关机器学习的数学理论，这里通常是用到它们的地方。但Tensorflow将这些数学很好地封装在函数中供我们使用。那么这个程序里到底发生了什么？我们来看一下：

我们知道，在上面的函数中，两组数字之间的关系其实是y=2x-1。当计算机试图 "学习 "这个映射关系时，它猜测......也许y=10x+10。`LOSS（损失）函数将猜测的答案与已知的正确答案进行比较`，并衡量偏差程度。然后，计算机使用`OPTIMIZER函数再做一次猜测，努力使损失最小化`。这时，也许计算机会得出一些像y=5x+5这样的结果，虽然还是很糟糕，但更接近正确的结果（即损失更低）。训练的时候，将依据指定的EPOCHS次数，重复这样的猜测与优化过程。

下面的程序中可以看到如何设置用 "平均平方误差 "来计算损失，并使用 "同步梯度下降 "来优化神经元网络。我们并不需要理解背后的这些数学，但我们可以看到它们的成效! 

随着经验的积累，我们将了解如何选择相应的损失和优化函数，以适应不同的情况。

在调用**model.fit**函数时，神经网络“学习”X和Y之间的关系。在这个过程中，它将一次又一次地完成上面所说的循环，即做一个猜测，衡量它有多好或多坏（又名损失），使用Opimizer进行再一次猜测，如此往复。训练将根据指定的遍数（epochs）执行此操作。当运行此代码时，将在输出结果中看到损失（loss）。



```python
from tensorflow import keras
import numpy as np

## 构建模型
## layer就是一层神经元， shape就是一个输入值, 接下来我们将创建一个最简单的神经网络。它只有1层，且这层只有1个神经元，它的输入只是1个数值
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

## 优化和损失函数
model.compile(optimizer='sgd', loss='mean_squared_error')

## 准备训练数据
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float) # tf擅长处理float数据
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)


## 训练模型
model.fit(xs, ys, epochs=500) # y是标签，eposhs是训练次数，这里是100次
```

到这里为止模型已经训练好了，它学习了X和Y之间的关系。现在，我们可以使用**model.predict**方法来让它计算未知X对应的Y。例如，如果X=10，我们认为Y会是什么？在运行下面代码之前，请猜一猜：

```python
model.predict([10.0])
## 18.980xxx 接近于19
```
我们可能会想到19，对吧？但最后输出比19低了一丁点儿。这是为什么呢？因为神经网络处理的是概率，所以根据我们向神经元网络提供的数据，它计算出X和y之间的关系是y=2x-1的概率非常高。但由于只有6个数据点，无法完全确定x和y的函数关系。因此，10对应的y值非常接近19，但不一定正好是19。当使用神经网络时，会看到这种模式反复出现。我们几乎总是在处理概率，而非确定的数值。并经常需要通过进一步编写程序，来找出概率所对应的结果，特别当处理分类问题时。


如果是训练 `1500` 次的话，结果更准确。
![](https://gitee.com/chasays/mdPic/raw/master/uPic/hzzJ1F.png)