#!/usr/bin/python3
#coding=utf-8
# 快速排序：
# 1. 快速排序和冒泡排序都属于交换排序，快速排序是冒泡排序的升级。		
# 2. 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
#	然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
# 3. 时间复杂度：
#   - 最优时间复杂度：O(nlogn)
#   - 最坏时间复杂度：O(n2)
#   - 稳定性：不稳定
#
# 算法步骤
# 1. 选择一个基准，此处以待排序数组的第一个数组作为基准来比较
# 2. 分区：比基准值小的放到基准值前面，反之放在右边，相等则不动
# 3. 递归分区
def Partition(arr, start, end):
    pivot_key = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot_key:
            end -= 1
        arr[end], arr[start] = arr[start], arr[end]

        while start < end and arr[start] <= pivot_key:
            start += 1
        arr[start], arr[end] = arr[end], arr[start]
    return start



def QuickSort(arr, start, end):
    #递归结束：待排序数组中start<end
    if start < end:
        pivote = Partition(arr, start, end)
        QuickSort(arr, start, pivote-1)
        QuickSort(arr, pivote+1, end)
if __name__=='__main__':
    #arr = [int(i) for i in input().split()]
    arr = [5,3,4,5]
    QuickSort(arr,0,len(arr)-1)
    print(arr)