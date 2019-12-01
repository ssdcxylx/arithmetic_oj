# -*- coding: utf-8 -*-
# @Time    : 2019-08-05 21:53
# @Author  : ssdcxy
# @Email   : 18379190862@163.com
# @File    : Sort1.py


def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        flag = False
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                flag = True
        if not flag:
            return lst
    return lst


def top_k(lst, left, right, k):
    if left > right:
        return None
    low = left
    high = right
    pivot = lst[left]
    while left < right:
        while left < right and lst[right] >= pivot:
            right -= 1
        lst[left] = lst[right]
        while left < right and lst[left] <= pivot:
            left += 1
        lst[right] = lst[left]
    lst[left] = pivot
    if left == k-1:
        print(pivot)
        return
    elif left > k-1:
        top_k(lst, low, left-1, k)
    else:
        top_k(lst, left+1, high, k)


def quick_sort(lst, left, right):
    if left > right:
        return lst
    low = left
    high = right
    pivot = lst[left]
    while left < right:
        while left < right and lst[right] >= pivot:
            right -= 1
        lst[left] = lst[right]
        while left < right and lst[left] <= pivot:
            left += 1
        lst[right] = lst[left]
    lst[right] = pivot
    quick_sort(lst, low, left-1)
    return quick_sort(lst, left+1, high)


def merge(left, right):
    lst3 = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst3.append(left[i])
            i += 1
        else:
            lst3.append(right[j])
            j += 1
    if j == len(right):
        for k in left[i:]:
            lst3.append(k)
    else:
        for k in right[j:]:
            lst3.append(k)
    return lst3


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def low_filter(lst, i, n):
    while i < n:
        lindex = 2*i + 1
        rindex = 2*i + 2
        if rindex < n:
            if lst[rindex] > lst[i] and lst[lindex] <= lst[rindex]:
                lst[rindex], lst[i] = lst[i], lst[rindex]
                i = rindex
            elif lst[lindex] > lst[i] and lst[rindex] <= lst[lindex]:
                lst[lindex], lst[i] = lst[i], lst[lindex]
                i = lindex
            else:
                i = n
        elif lindex < n:
            if lst[lindex] > lst[i]:
                lst[lindex], lst[i] = lst[i], lst[lindex]
                i = lindex
        else:
            i = n
    return lst


def create_heap(lst):
    n = len(lst)
    for i in range((n >> 1)-1, -1, -1):
        lst = low_filter(lst, i, n)
    return lst


def heap_sort(lst):
    n = len(lst)
    lst = create_heap(lst)
    for i in range(n):
        lst[0], lst[n-i-1] = lst[n-i-1], lst[0]
        low_filter(lst, 0, n-i-1)
    return lst


if __name__ == '__main__':
    lst = [2, 2, 7, 6, 1, 3, 5]
    k = 4
    # top_k(lst, 0, len(lst)-1, k)
    # print(quick_sort(lst, 0, len(lst)-1))
    # print(merge_sort(lst))
    print(heap_sort(lst))

