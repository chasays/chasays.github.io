---
layout: post
title: "TensorFlow 基础学习 - 3"
subtitle: '图片不是规则的怎么办'
author: "叉叉敌"
header-style: text
tags:
  - TensorFlow
  - CNN
---



## 卷积神经网络

抓住它的核心思路，即通过卷积操作缩小了图像的内容，将模型注意力集中在图像特定的、明显的特征上。

max pooling - `增强特征，减少数据`
![](https://gitee.com/chasays/mdPic/raw/master/uPic/J83C5a.png)

## 实现



在下面的代码中模型在训练数据上的精度可能上升到93%左右，在验证数据上可能上升到91%。

这是朝着正确方向取得的显著进步!

试着运行更多的epochs--比如20个epochs，然后观察结果! 虽然结果可能看起来非常好，但实际上验证结果可能会下降，这是因为"过拟合"造成的，后面将会讨论。

(简而言之，'过拟合'发生在网络模型从训练集中学习到的结果非常好，但它太狭隘了，只能识别训练数据，而在看到其他数据时效果不佳。举个例子，如果我们一辈子只看到红色的鞋子，那么当我们看到一双蓝色的麂皮鞋可能会感到迷惑......再举一例，应试教育往往使得学生只对做过的题目有很好的正确率，但对真实的问题却错误率很高）

![](https://gitee.com/chasays/mdPic/raw/master/uPic/pXdBXT.png)
```py
import tensorflow as tf
print(tf.__version__)
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images=training_images.reshape(60000, 28, 28, 1)
training_images=training_images / 255.0
test_images = test_images.reshape(10000, 28, 28, 1)
test_images=test_images/255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28, 28, 1)),
  tf.keras.layers.MaxPooling2D(2, 2),
  tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
model.fit(training_images, training_labels, epochs=5)
test_loss = model.evaluate(test_images, test_labels)
```
## 卷积模型是如何建立的

`第一步是收集数据`。我们会注意到，这里和之前有一点变化，训练数据需要改变维度（shape）。这是因为第一次卷积期望一个包含所有数据的单一张量，所以要把训练数据设置为60000x28x28x1的一个4D列表，测试图像也是如此处理。如果不这样做，会在训练时得到一个错误，因为卷积操作将不能识别数据形状。



接下来是定义模型。首先要添加一个卷积层。参数是

- 我们想要生成的卷积数（`过滤器数量`）。这个数值是任意的，`但最好是从32开始的倍数`。
- 卷积的大小（`过滤器的大小`），在本例中为3x3网格。这是最常用的尺寸。
- `要使用的激活函数` -- 在本例中，我们将使用relu，我们可能还记得它相当于当x>0时返回x，否则返回0。
- `在第一层，设定输入数据的形状`。


在卷积层之后加上一个MaxPooling层，用来压缩图像，同时保持卷积所强调的特征内容。通过为MaxPooling指定(2,2)，效果是将图像的大小缩小四分之一。它的想法是创建一个2x2的像素数组，然后选取最大的一个，从而`将4个像素变成1个`，在整个图像中重复这样做，这样做的结果是将水平像素的数量减半，垂直像素的数量减半，`有效地将图像缩小25%`。

再增加一个卷积层和MaxPooling2D。


现在对输出进行扁平化处理。在这之后，你将拥有与非卷积版本相同的DNN结构，即全连接神经元网络。

含有128个神经元的全连接层，以及10个神经元的输出层。

现在编译模型，调用model.fit方法做训练，接着用测试集评估损失和准确率。

## 网络结构

看看可否只使用单个卷积层和单个MaxPooling 2D将MNIST（手写数字）识别率提高到99.8%或更高的准确率。一旦准确率超过这个数值，应该停止训练。Epochs不应超过20个。如果epochs达到20但精度未达到要求，那么就需要重新设计层结构。当达到99.8%的准确率时，你应该打印出 "达到99.8%准确率，所以取消训练！"的字符串。

```py
import tensorflow as tf
from tensorflow import keras

## overwrite callback

class Callbacks(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('accuracy')>=0.998):
      print("达到99.8%准确率，所以取消训练！")
      self.model.stop_training = True

callbacks = Callbacks()

## 准备数据
mnist = tf.keras.datasets.mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

## 归一化
training_images = training_images.reshape(60000, 28, 28, 1)
training_images = training_images / 255.0

test_images = test_images.reshape(10000, 28, 28, 1)
test_images  = test_images / 255.0

## 建立模型
model = tf.keras.models.Sequential([
   tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28, 28, 1)),
   tf.keras.layers.MaxPooling2D(2, 2),
  #  tf.keras.layers.Conv2D(62, (3, 3), activation='relu'),
  #  tf.keras.layers.MaxPooling2D(2,2),

   tf.keras.layers.Flatten(), ##扁平化
   tf.keras.layers.Dense(128, activation='relu'),
   tf.keras.layers.Dense(10, activation='softmax')
])


## 训练
model.compile(optimizer=tf.keras.optimizers.Adam(), 
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])
model.summary()
model.fit(training_images, training_labels, epochs=4, callbacks=[callbacks])

## 预测和评估

test_loss = model.evaluate(test_images, test_labels)

```

结果

![](https://gitee.com/chasays/mdPic/raw/master/uPic/v2yTSv.png)

