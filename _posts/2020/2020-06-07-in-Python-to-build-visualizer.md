---
layout: post
title: "Python 构建可视化排序"
subtitle: '熟悉可视化pygame接口'
author: "叉叉敌"
header-style: text
tags:
  - python
  - pygame
  - 接口
  - 可视化
---
用 Python 构建排序可视化工具

Python 最近在计算机科学领域占据主导地位，其应用领域包括机器学习、数据科学、人工智能、网络开发和软件编程，这些都是21世纪的最新趋势。 根据 PYPL 编程语言普及指数，与其他编程语言相比，python 大约占总份额的31.6% 。

![python](https://gitee.com/chasays/mdPic/raw/master/uPic/ueNWFQ.jpg)

所以，我想我们可以用最好的方式来学习 python，通过构建一个精彩的项目来掌握任何编程语言中的一个基本原理—— sorting。在本文结束时，你可以用五种不同的算法构建一个令人惊叹的排序可视化工具:

- 选择排序
-  冒泡排序
 - 插入排序
 - 归并排序
 - 快速排序
## 算法
让我们创建一个名为 `algorithms.py` 的文件，在这个文件中，我们将用 python 编写所有的排序算法。 导入 `time` 模块来告诉用户可视化工具所花费的时间(注意: 显示的时间是系统渲染可视化工具所花费的时间，与排序算法无关)。 创建一个称为 `Algorithm` 的类，并将这段代码粘贴到这里:
```python
class Algorithm:
    def __init__(self, name):
        self.array = random.sample(range(512), 512) # Random array of size 512
        self.name = name # Get name of the variable

    def update_display(self, swap1=None, swap2=None):
        import visualizer
        visualizer.update(self, swap1, swap2) # pass the indexes to be swapped into the visualizer

    def run(self): # Start the timer and run the algorithm
        self.start_time = time.time() 
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed
```

我们最初将创建一个大小为512的随机数组。 在 `update_display` 方法中，我们将调用 `visualizer.py` 中的 `update` 函数，稍后将编写这个函数来处理图形。 最后，`run` 方法将启动计时器并调用算法函数，这是每个排序算法的一部分。 它返回已排序的数组和运行时间。

## 选择排序
```python
class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.update_display(self.array[i], self.array[min_idx])
```   


`Selectionsort` 类将继承 `Algorithm` 类，在其算法方法中我们实现了 `Selection sort`。 每次数组更新时，我们不断调用 `update_display` 方法并实时呈现数组的排序。 类似地，我们也实现了所有其他算法。



## 冒泡排序
```python
class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            self.update_display(self.array[j], self.array[j+1])
```

##  插入排序
```python
class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            cursor = self.array[i]
            idx = i
            while idx > 0 and self.array[idx-1] > cursor:
                self.array[idx] = self.array[idx-1]
                idx -= 1
            self.array[idx] = cursor
            self.update_display(self.array[idx], self.array[i])


```
## 归并排序

```python
class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self, array=[]):
        if array == []:
            array = self.array
        if len(array) < 2:
            return array
        mid = len(array) // 2
        left = self.algorithm(array[:mid])
        right = self.algorithm(array[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            self.update_display()
        result += left[i:]
        result += right[j:]
        self.array = result
        self.update_display()
        return result

```

## 快速排序
```python
class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self, array=[], start=0, end=0):
        if array == []:
            array = self.array
            end = len(array) - 1
        if start < end:
            pivot = self.partition(array,start,end)
            self.algorithm(array,start,pivot-1)
            self.algorithm(array,pivot+1,end)

    def partition(self, array, start, end):
        x = array[end]
        i = start-1
        for j in range(start, end+1, 1):
            if array[j] <= x:
                i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    self.update_display(array[i], array[j])
        return i
```
## 可视化工具

祝贺你！ 你只是写了所有流行的排序算法。 最后一步是直观地显示每种排序算法的工作方式。

下面是 `visualizer.py` 文件的代码。
```python
import algorithms
import time
import os
import sys
import pygame

 # Set the window length and breadth  (Make sure that the breadth is equal to size of array. [512])
dimensions = [1024, 512]
# List all the algorithms available in the project in dictionary and call the necessary functions from algorithms.py
algorithms = {"SelectionSort": algorithms.SelectionSort(), "BubbleSort": algorithms.BubbleSort(), "InsertionSort": algorithms.InsertionSort(), "MergeSort": algorithms.MergeSort(), "QuickSort": algorithms.QuickSort()}

# Check list of all the available sorting techniques using 'list'
if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        for key in algorithms.keys(): print(key, end=" ") # Display the available algorithms
        print("")
        sys.exit(0)

# Initalise the pygame library
pygame.init()
# Set the dimensions of the window and display it
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
# Fill the window with purple hue
display.fill(pygame.Color("#a48be0"))

def check_events(): # Check if the pygame window was quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

def update(algorithm, swap1=None, swap2=None, display=display): # The function responsible for drawing the sorted array on each iteration
    display.fill(pygame.Color("#a48be0"))
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Sorting...".format(algorithm.name, time.time() - algorithm.start_time)) # Display on title bar
    k = int(dimensions[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        colour = (80, 0, 255)
        if swap1 == algorithm.array[i]:
            colour = (0,255,0)
        elif swap2 == algorithm.array[i]:
            colour = (255,0,0)
        # The most important step that renders the rectangles to the screen that gets sorted.
        # pygame.draw.rect(dsiplay_window, color_of_rectangle, size_of_rectangle)
        pygame.draw.rect(display, colour, (i*k,dimensions[1],k,-algorithm.array[i]))
    check_events()
    pygame.display.update()

def keep_open(algorithm, display, time): # Keep the window open until sort completion
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Done!".format(algorithm.name, time))
    while True:
        check_events()
        pygame.display.update()

def main():
    if len(sys.argv) < 2:
        print("Please select a sorting algorithm.") 
    else:
        try:
            algorithm = algorithms[sys.argv[1]] # Pass the algorithm selected
            try:
                time_elapsed = algorithm.run()[1]
                keep_open(algorithm, display, time_elapsed)
                pass
            except:
                pass
        except:
            print("Error.")

if __name__ == "__main__":
    main()


```


太好了！ 我知道，有很多代码需要消化，但我向您保证，当您按下这个项目的运行按钮时，它将会取得丰硕的成果。 同时，让我向您解释一下可视化工具代码。


首先，我们导入我们编写算法的算法 python 文件。 然后，在 python 中导入 pygame 模块来处理我们项目中的图形。


另外，通过在终端中执行 `pip install pygame` 来安装 pygame。


设置维数组中的窗口大小，并确保保留第二个参数512，因为这是我们正在使用的随机样本数。

接下来的几行命令将向用户显示可用算法列表，并提示他们选择一个并在运行代码时输入。


然后，初始化 pygame 模块，设置窗口的尺寸，并用颜色填充显示器。


检查事件函数用于在关闭窗口时退出程序。


其次是整个程序更新方法中最重要的功能。 这个方法在每次迭代之后接受数组，并且手头有两个交换变量，swap1和 swap2变量。 这些变量被赋予不同的颜色。


然后我们使用 `pygame.draw.rect()`函数将这些数组元素渲染到窗口并更新它。


只要 pygame 窗口仍在运行，而且窗口没有被终止，那么保持 open 函数就会保持 pygame 窗口处于打开状态。


最后，主函数将用户选择算法作为输入，并调用具体算法及其定时器。

## 结果

最终，是时候运行我们的项目了。 在 project 目录中打开终端，执行 `python visualizer.py` 列表以获得所有可用算法的列表。

![selector](https://gitee.com/chasays/mdPic/raw/master/uPic/selector.gif)

若干启发
中国六字
个体理性与集体理性相冲突,还是相一致,取决于
制度安排(游戏规则)。
解决个体理性与集体理性之间的冲突不是靠否定个
体理性,而是靠修改制度(游戏规则),从而在满
足个体理性的基础上实现集体理性。
从智猪博弈中还可以发现,在A<10时,任一方去按
都是集体理性的选择,而收入分配的不均将有助于
减少个休性与焦休御性的油室
