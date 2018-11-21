#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Sort
# 选择排序
# 1.运行时间和输入无关 2.数据移动是最少的
# 交换总次数N 需要N^2/2次比较
def selectSort(array):
    length = len(array)
    for i in range(length):
        min = i
        for j in range(min + 1 , length):
            if (array[j] < array[min]):
                min = j
        array[i] , array[min] = array[min] , array[i]
    return array


# 插入排序
# 1.平均情况下插入排序需要~N^2/4次比较以及~N^2/4次交换 最坏情况下需要~N^2/2次比较和~N^2/2次交换，最好情况下需要N-1次比较和0次交换
def insertionSort(array):
    length = len(array)
    for i in range(length):
        for j in range(i , 0 , -1):
            if(j > 0 and (array[j] < array[j - 1])):
                array[j] , array[j-1] = array[j-1],array[j]
    return array

#插入排序需要的交换操作和数组中倒置的数量相同，需要的比较次数大于等于倒置的数量，小于等于倒置的数量加上数组的大小再减一。
#对于随机排序的无重复主键的数组，插入排序和选择排序的运行时间是平方级别的。两者之比应该是一个较小的常数。


#希尔排序
#运行时间达不到平方级别 ， 代码量很小，且不需要使用额外的内存空间。
def shellSort(array):
    N = len(array)
    h = 1
    while (h < N/3):
        h = 3*h + 1
    while(h >= 1):
        for i in range( h , N):
            for j in range(i ,0 , -h):
                if(array[j] < array[j-h]):
                    array[j] , array[j-h] = array[j - h] , array[j]
        h = h/3
    return array



print (shellSort([0,5,6,3,1,2,9]))