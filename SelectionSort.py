#!/usr/bin/python3
# coding=utf-8
# 选择排序：先从未排序序列中选择出最小的元素，放到排序序列的起始位置；再从未排序序列中找出最小的元素，然后放到已排序序列的末尾。
def SelectSort(arr):
    n = len(arr)
    #进行n-1次选择
    for i in range(n-1):
        MinIndex = i
        #从i+1位置开始选择出最小的元素
        for j in range(i+1, n):
            if arr[j] < arr[MinIndex] :
                MinIndex = j
        if MinIndex != i :
            arr[i], arr[MinIndex] = arr[MinIndex], arr[i]

if __name__ == '__main__':
    arr = [3,1,4,2,6,5]
    SelectSort(arr)
    print(arr)