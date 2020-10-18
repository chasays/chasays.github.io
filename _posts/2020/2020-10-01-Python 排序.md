---
layout: post
title: "Python 算法 排序 "
subtitle: '快排和堆'
author: "叉叉敌"
header-style: text
tags:
  - 算法
  - 排序
---
我们常见的冒泡排序，冒泡排序而已有2种优化思路，就是排过序中，`比下一个的还小，就退出本次循环`，进入下一次循环， 还有一种优化，因为是冒泡，每次冒泡后，最后（几个）数的都是排过序的。`因此每次比较只与前面没有排序的比较`。
```python
def bubble(li):
    if not isinstance(li, list):
        raise ValueError("please enter the list value")
        
    counter = 0
    length = len(li)
    last = 0
    border = length - 1
    
    for i in range(length-1):
        swap = False 
        for j in range(0,border):
            counter += 1
            if li[j] < li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                swap = True
                last = j
                print(i,j,li,counter)
        
        if not swap: break ## 
        border = last 
        
    return li
```

今天需要是的排序中2个重要的排序。一个是快排，一个是堆排。
## 快排

>概念：快速排序是一种非常高效的排序算法，采用 “分而治之” 的思想，把大的拆分为小的，小的拆分为更小的。其原理是，对于给定的记录，选择一个基准数，通过一趟排序后，将原序列分为两部分，使得前面的比后面的小，然后再依次对前后进行拆分进行快速排序，递归该过程，直到序列中所有记录均有序。


![oF8Z3v](https://gitee.com/chasays/mdPic/raw/master/uPic/oF8Z3v.gif)


意思就是，选一个基准数povit， `然后前面的都小于这个中间数， 后面的大于这个中间数`。等于的就放后面。

基准数的位置：
- 取第一个元素
- 取最后一个元素
- 取第中间位置元素
- 取第一个、最后一个、中间位置3者的中位数元素

```python
def quickSorted(lists, i, j):
    if i>=j:return lists
    povit = lists[i]
    low = i
    high = j
    while i < j:
        # 从后往前
        while i<j and lists[j] >= povit:
            j -= 1
        lists[i] = lists[j] # 交换povit的值
        print(i, j, lists)
        # 从前到后
        while i<j and lists[i] <= povit:
            i += 1
        lists[j] = lists[i] # 交换
        print(i, j, lists)
    lists[j] = povit  # 找到中间的为povit值
    quickSorted(lists, low, i-1) # 前面再来递归
    quickSorted(lists, i+1, high) # 后面的来递归
    return lists
```

## 堆排
Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆是一个近似完全二叉树的结构，并同时满足堆的性质：即子节点的键值或索引总是小于（或者大于）它的父节点。
![u0yaw8](https://gitee.com/chasays/mdPic/raw/master/uPic/u0yaw8.jpg)

重复从最大堆取出数值最大的结点(把根结点和最后一个结点交换，把交换后的最后一个结点移出堆)，并让残余的堆维持最大堆性质。

`堆节点的访问`， 通常堆是通过一维数组来实现的。在数组起始位置为0的情形中：
- 父节点i的左子节点在位置 2i+1;
- 父节点i的右子节点在位置2i+2;
- 子节点i的父节点在位置floor((i-1)/2);

在堆的数据结构中，堆中的`最大值总是位于根节点`（在优先队列中使用堆的话堆中的最小值位于根节点）。堆中定义以下几种操作：

- 最大堆调整（Max Heapify）：将堆的末端子节点作调整，使得`子节点永远小于父节点`
- 创建最大堆（Build Max Heap）：将堆中的所有数据重新排序
- 堆排序（HeapSort）：移除位于第一个数据的根节点，并做最大堆调整的递归运算
```python
def headSorted(lst):
    def siftDown(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1 # 左子节点
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]: # 有子节点和最后一个比， 已经左右节点比
                child += 1 # 右子节点
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root] # 子节点永远小于父节点
                root = child 
                print(child, root, lst)
            else:
                break
    # 创建最大堆
    for start in range((len(lst)-2)//2, -1, -1):
        siftDown(start, len(lst) - 1)
    # 堆排序
    for end in range(len(lst)-1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        siftDown(0, end-1) # 每次出去最后一个并排序
    print(lst)
    return lst

if __name__=="__main__":
    s = [1,4,2,7,8,5,3,9,0,6]
    headSorted(s)
```

下面这个是知乎的：https://zhuanlan.zhihu.com/p/105624690

堆排序有以下几个核心的步骤：

- 将待排序的数组初始化为大顶堆，该过程即建堆。
- 将堆`顶元素与最后一个元素进行交换`，除去最后一个元素外可以组建为一个新的大顶堆。
- 由于第二部堆顶元素跟最后一个元素交换后，新建立的堆不是大顶堆，需要重新建立大顶堆。重复上面的处理流程，直到堆中仅剩下一个元素。

```python
class Solution(object):
    def heap_sort(self, nums):
        i, l = 0, len(nums)
        self.nums = nums
        # 构造大顶堆，从非叶子节点开始倒序遍历，因此是l//2 -1 就是最后一个非叶子节点
        for i in range(l//2-1, -1, -1): 
            self.build_heap(i, l-1)
        # 上面的循环完成了大顶堆的构造，那么就开始把根节点跟末尾节点交换，然后重新调整大顶堆  
        for j in range(l-1, -1, -1):
            nums[0], nums[j] = nums[j], nums[0]
            self.build_heap(0, j-1)

        return nums

    def build_heap(self, i, l): 
        """构建大顶堆"""
        nums = self.nums
        left, right = 2*i+1, 2*i+2 ## 左右子节点的下标
        large_index = i 
        if left <= l and nums[i] < nums[left]:
            large_index = left

        if right <= l and nums[left] < nums[right]:
            large_index = right
 
        # 通过上面跟左右节点比较后，得出三个元素之间较大的下标，如果较大下表不是父节点的下标，说明交换后需要重新调整大顶堆
        if large_index != i:
            nums[i], nums[large_index] = nums[large_index], nums[i]
            self.build_heap(large_index, l)

if __name__=="__main__":
    s = [1,4,2,7,8,5,3,9,0,6]
    print(Solution().heap_sort(s))
```

## read more
[python 快排](https://zhuanlan.zhihu.com/p/63227573)
[堆排序](https://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F)
