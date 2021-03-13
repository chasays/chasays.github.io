---
layout: post
title: "TensorFlow 基础学习 - 2"
subtitle: '物品图片如何训练'
author: "叉叉敌"
header-style: text
tags:
  - TensorFlow
---

让我们来看这样一个场景，让计算机识别不同的服装用品（有提包、鞋子、裤子等10类物品）。我们将用包含10种不同类型的`物品图片的数据集来训练一个神经元网络，实现分类`。

## 数据导入

首先通过`tf.keras`的API可以直接获得Fashion MNIST数据集。

在mnist对象上调用l`oad_data`方法会得到两个元组，各自包含两个列表。这些列表存储了服装用品的训练与测试图像数据及标签值。

为什么会有2组数据？
我们可能在想为什么有2组数据-训练集和测试集。记得在介绍中说过的吗？基本想法是`将1组数据用于训练`，然后用`另一组数据评估模型在分类值方面的表现会有多好`。测试数据必须是模型还没有看到过的。毕竟，当完成模型的训练后，必定想用它之前没有见过的数据来试一试!

```python
from tensorflow import keras
fashion_mnist = keras.datasets.fashion_mnist
(train_iamges, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
```

获取到了4个变量，一个训练集一个测试集。
来看看具体的内容。

```python
import matplotlib.pyplot as plt
plt.imshow(training_images[42])

```

![](https://gitee.com/chasays/mdPic/raw/master/uPic/qorHkT.png)

## 归一化处理

我们会注意到，数字中的所有值都在0和255之间。如果我们要训练一个神经网络，出于多种原因，如果把所有的值都`处理成0和1之间`，那就更容易得到较好的训练效果。这个过程叫做 "**归一化**"......幸运的是，在Python中，很容易对这样的列表进行归一化，而不需要循环。可以这样做：
其实就是把矩阵里面的每一个数都除以255即可。

```python
training_images  = training_images / 255.0
test_images = test_images / 255.0
```

## 模型设计

我们可能在想为什么有2组数据-训练集和测试集。记得在介绍中说过的吗？基本想法是将1组数据用于训练，然后用另一组数据评估模型在分类值方面的表现会有多好。测试数据必须是模型还没有看到过的。毕竟，当完成模型的训练后，必定想用它之前没有见过的数据来试一试!

现在我们来设计Fashion MNIST分类模型。这里有不少新的概念，不过别担心，我们会掌握它们的窍门。

```py
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), 
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])
```

或者用下面的方法设计模型，效果一样

```py
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(10, activation=tf.nn.softmax))
```

- Sequential ：这定义了神经网络中的层数序列。一开始学习神经元网络总是使用序列模型。
- Flatten : 还记得上面将图像打印出来的时候是一个正方形吗？扁平化只是把这个正方形变成了一个一维的集合。`把二维数组变成一维数组`。
- Dense : 增加一层神经元。每一层神经元都需要一个激活函数 `activation` 来告诉它们输出什么。有很多选项，但目前只用这些（relu和softmax）

Relu的意思是 "如果X>0返回X，否则返回0"--所以它的作用是它只把大于0的值传递给网络中的下一层，小于0的也当作0。

![](https://gitee.com/chasays/mdPic/raw/master/uPic/a6vrqo.png)

Softmax激活函数接收到一组值后，选择其中最大的一个输出。例如，上一层的输出为[0.1, 0.1, 0.05, 0.1, 9.5, 0.1, 0.05, 0.05, 0.05]，Softmax就省去了我们在其中寻找最大的值，并把它变成[0,0,0,0,0,1,0,0,0,0,0] Softmax的意思是 "如果X>0，则返回X，否则返回0" -- 所以它的作用是只把0或更大的值传给下一层的网络。--其目的是节省大量的编码！
![](https://gitee.com/chasays/mdPic/raw/master/uPic/zLEMQI.png)

现在模型已经定义好了，下一步要做的事情就是实际建立它。可以像之前一样用优化器和损失函数编译它--然后通过调用`model.fit`来训练它，要求它将训练数据与标签拟合--即让模型找出训练数据和标签之间的关系。训练好之后，它将能对格式与训练数据相同，但从未“见过”的新数据做出预测。

## 训练
```py
model.compile(optimizer = tf.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)
```
![](https://gitee.com/chasays/mdPic/raw/master/uPic/xqxele.png)

一旦模型完成了训练 -- 能在最后一个epoch结束时看到一个准确率值。这告诉我们，神经网络对训练数据的分类准确率约为81%。即，它找出了图像和标签之间的模式匹配，81%的分类结果都正确。考虑到只训练了5个epochs，而且做得相当快，所以结果还不错。

>这里要注意的是：`损失值下减小的，精确度是提高的，才是正常的。`

但对于未见过的数据，它的分类准确度有多高？这就是为什么我们需要测试图像的原因。我们可以调用model.evaluation，并将用于测试的图像和标签数据传入，它会报告测试数据的损失。让我们试一试。

## AMA

1. 数据没有做归一化处理？
归一化的目的就是消除奇异样本数据，导致的不良影响。数据归一化后，最优解的寻优过程明显会变得平缓，更容易正确的收敛到最优解。
归一化可以参考这篇文章：https://www.cnblogs.com/silence-tommy/p/7113498.html

2. 模型设计的时候，数据没有做Flatten扁平化处理会这样？
没有做扁平化处理，就是28层神经元。

3. 模型设计的时候，中间层的神经元用更大的数字来替代，结果是什么？

`训练时间更长，但更准确`。通过增加更多的神经元，计算机必须做更多的计算，减慢了训练过程。但对于本案例，增加神经元数量有积极的影响--确实得到了更好的准确度。但这并不意味着总是 "越多越好"，因为很快就会遇到收益递减的定律。

4. 考虑最后（产出）层。为什么有10个神经元？如果数量少于10会发生什么？例如，尝试改作5个来训练网络
一旦模型发现一个意外的值，就会产生一个错误。规则是--最后一层的神经元数量应该与你要分类的类数相匹配。在这种情况下，是数字0-9，所以有10个，因此你的最后一层应该有10个神经元。

5. 考虑网络中增加层数的影响。如果在512层和10层之间再加一层会发生什么？

答案：`没有显著影响`--因为这是相对简单的数据。对于复杂得多的数据，通常要增加额外的层。

6. 请考虑改变训练epochs次数，为有什么影响？

试试15个epochs--可能会得到一个比5个epochs更好的模型,损失更小。 试试30个epochs--可能会看到损失值停止下降，有时还会增加。这是被称为 "过拟合 "的副作用，在训练神经网络时，需要一直注意这个问题。如果损失没有改善，那么浪费时间继续训练是没有意义的

7. 之前在训练模型的时候，你可能会想'如果可以在达到一个期望值的时候停止训练不是很好吗？

--即95%的准确率对你来说可能已经足够了，如果你在3个epochs后达到了这个值，为什么还要坐等它完成更多的训练次数呢....，那么如何解决这个问题？就像其他很多类似程序一样......运用回调函数！让我们来看看它的实际作用。


```py
import tensorflow as tf
print(tf.__version__)

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('loss')<0.4):
      print("\nReached 60% accuracy so cancelling training!")
      self.model.stop_training = True

callbacks = myCallback()
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images=training_images/255.0
test_images=test_images/255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])
```