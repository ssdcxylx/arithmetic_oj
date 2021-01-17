# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-16 10:01:30
# LastEditTime: 2020-12-22 15:27:59
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/Test.py

def simple_quick_sort(lst):
    quick_sort = lambda l: quick_sort(i for i in l[1:] if i <= l[0]) + [l[0]] + quick_sort(j for j in l[1:] if j > l[0]) if l else []
    return quick_sort(l)

def quick_sort(lst, low, high):
    if low >= high:
        return lst
    left, right = low, high
    pivot = lst[low]
    while left < right:
        while left < right and lst[right] >= pivot:
            right -= 1
        lst[left] = lst[right]
        while left < right and lst[left] < pivot:
            left += 1
        lst[right] = lst[left]
    lst[right] = pivot
    quick_sort(lst, low, right-1)
    quick_sort(lst, right+1, high)
    return lst


if __name__ == "__main__":
    lst = [0, 5, 4, 4, 4, 3, 3, 3, 2, 1]
    print(quick_sort(lst, 0, len(lst)-1))