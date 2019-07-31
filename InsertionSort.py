#!/usr/bin/python3
#coding = utf-8
#插入排序：插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
def InsertionSort(arr):
    n = len(arr)
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1,n):
            #以a[j-1]为基准，a[j]要与a[j-1]以及之前的元素进行比较，确定插入位置
            for j in range(i,0,-1):
                if arr[j-1] > arr[j]:
                    arr[j-1], arr[j] = arr[j], arr[j-1]

if __name__ == '__main__':
    arr = [3,1,4,2,6,5]
    InsertionSort(arr)
    print(arr)