# 基本单位
张量 `tensor` 是TensorFlow的基本单位，这两天就是数学里面的一个速度啊，没有，一位侍者二位数得，还有就是标量。
```python
random_float = tf.random.uniform(shape=())
zero_vector = tf.zeros(shape=(2))

A = tf.constant([[1., 2.], [3., 4.]])
B = tf.constant([[5., 6.], [7., 8.]])

```

tensor 张量的属性有`形状、类型、和值三`个属性，那可以通过三个方法去获取，shape,dtype， numpy().
```py
print(A.shape)     
print(A.dtype)    
print(A.numpy()) 
```
果上面常量里面不是小数（1.），如果是int。那么返回的对应的也是int32。

# 操作
TensorFlow 里面有`操作`，操作实际就是对数组的运算。有求和、乘积。
```py
C = tf.add(A, B)    # 计算矩阵A和B的和
D = tf.matmul(A, B) # 计算矩阵A和B的乘积
```

关于矩阵的乘法， 可以查看恶补下相关的知识
>https://baike.baidu.com/item/%E7%9F%A9%E9%98%B5%E4%B9%98%E6%B3%95



一个m×n的矩阵就是m×`n`个数排成m行`n`列的一个数阵。由于它把许多数据紧凑地集中到了一起，所以有时候可以简便地表示一些复杂的模型，如电力系统网络模型。

![1](https://gitee.com/chasays/mdPic/raw/master/uPic/9mvUNu.png)


![2](https://gitee.com/chasays/mdPic/raw/master/uPic/5CYrKc.png)

# 求导

机器学习中的大部分问题都是优化问题，而绝大部分优化问题都可以使用梯度下降法处理，那么搞懂什么是梯度，什么是梯度下降法就非常重要！这是基础中的基础，也是必须掌握的概念！
提到梯度，就必须从`导数`、偏导数和方向导数讲起，弄清楚这些概念，才能够正确理解为什么在优化问题中使用梯度下降法来优化目标函数，并熟练掌握梯度下降法。

关于梯度下降
>https://baike.baidu.com/item/%E6%A2%AF%E5%BA%A6/13014729

我直接搬吧。梯度的本意是一个向量（矢量），表示某一函数在该点处的方向导数沿着该方向取得最大值，即函数在该点处沿着该方向（此梯度的方向）变化最快，变化率最大（为该梯度的模）。


掌握了上面，`导数、偏导数，导梯度下降`这些概念之后，再来了解，这是TensorFlow里面的一个自动求导机制`tf.GradientTape()` 这个 “求导记录器” 来实现自动求导，那只要掌握两三个常见的API, 那我们就可以对函数进行求导求偏导数，还有梯度下降都可以计算。

```py
import tensorflow as tf

x = tf.Variable(initial_value=3.)
with tf.GradientTape() as tape:     
    y = tf.square(x)
y_grad = tape.gradient(y, x)        
print(y, y_grad)

# 输出

tf.Tensor(9.0, shape=(), dtype=float32)
tf.Tensor(6.0, shape=(), dtype=float32)

```
上面 `x` 是用 `tf.Variable()` 声明的一个变量。与普通张量一样，变量同样具有形状、类型和值三种属性。
```py

X = tf.constant([[1., 2.], [3., 4.]])
y = tf.constant([[1.], [2.]])
w = tf.Variable(initial_value=[[1.], [2.]])
b = tf.Variable(initial_value=1.)
with tf.GradientTape() as tape:
    L = tf.reduce_sum(tf.square(tf.matmul(X, w) + b - y))
w_grad, b_grad = tape.gradient(L, [w, b])        # 计算L(w, b)关于w, b的偏导数
print(L, w_grad, b_grad)
```

输出
```
tf.Tensor(125.0, shape=(), dtype=float32)
tf.Tensor(
[[ 70.]
[100.]], shape=(2, 1), dtype=float32)
tf.Tensor(30.0, shape=(), dtype=float32)
```

`tf.square() `操作代表对输入张量的每一个元素求平方，不改变张量形状。 `tf.reduce_sum()` 操作代表对输入张量的所有元素求和，输出一个形状为空的纯量张量（可以通过 `axis` 参数来指定求和的维度，不指定则默认对所有元素求和）

## 主要API

https://www.tensorflow.org/versions/r1.9/api_guides/python/array_ops

https://www.tensorflow.org/versions/r1.9/api_guides/python/math_ops


## 模型建立与训练 
