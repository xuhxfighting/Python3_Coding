#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 冒泡排序：输出结果升序
# 算法分析：https://my.oschina.net/u/4131409/blog/3079828

def BubbleSort(arr):
    # 1. 计算数组长度
    n = len(arr)
    # 2. 迭代n-1次
    for i in range(n):
    # 3. 每次迭代比较的次数逐次减1
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
BubbleSort(arr)
print(arr)
'''
for i in range(len(arr)):
    print("%d" %arr[i],end=' ')
'''

'''
def bubble_sort(alist):
    for j in range(len(alist)-1,0,-1):
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)
'''