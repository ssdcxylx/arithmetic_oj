# coding = utf-8

"""
优化方法1：引入随机性
优化方法2：聚集
优化方法3：三位数取中
优化方法4：引入插入排序
优化方法5：优化递归操作，尾递归
优化方法6：并行操作，多线程处理子序列
"""

import random
import time


def quick_sort(lst, first=0, last=0):
    if last - first + 1 < 10:
        insert_sort(lst, first, last)
    else:
        # 快速排序
        if first >= last:
            return lst
        low = first
        high = last
        left_lst_len = 0  # 分割后第一个序列和第二个序列与主元相等元素的长度
        right_lst_len = 0
        select_pivot_median(lst, first, last)  # 选择主元并将置于首位
        pivot = lst[first]
        while first < last:
            while first < last and lst[last] >= pivot:
                if lst[last] == pivot:
                    right_lst_len += 1
                last -= 1
            lst[first] = lst[last]
            while first < last and lst[first] <= pivot:
                if lst[first] == pivot:
                    left_lst_len += 1
                first += 1
            lst[last] = lst[first]
        lst[last] = pivot
        lst1_last = first - 1  # 保存分割后第一个序列的最后位置和第二个序列的最开始的位置
        lst2_first = first + 1
        flag = low
        while lst1_last - low > 0 and flag < lst1_last and left_lst_len > 0:  # 将第一个序列中与主元相等的元素置于主元左侧
            if pivot == lst[flag]:
                while lst[lst1_last] == pivot and left_lst_len > 0 and lst1_last - low > 0:
                    left_lst_len -= 1
                    lst1_last -= 1
                if lst1_last > 0 and left_lst_len > 0:
                    lst[flag], lst[lst1_last] = lst[lst1_last], lst[flag]
                    left_lst_len -= 1
                    lst1_last -= 1
                else:
                    break
            flag += 1
        flag = high
        while high - lst2_first > 0 and flag > lst2_first and right_lst_len > 0:  # 将第二个序列中与主元相等的元素置于主元右侧
            if pivot == lst[flag]:
                while lst[lst2_first] == pivot and right_lst_len > 0 and high - lst2_first > 0:
                    right_lst_len -= 1
                    lst2_first += 1
                if lst2_first < high and right_lst_len > 0:
                    lst[flag], lst[lst2_first] = lst[lst2_first], lst[flag]
                    right_lst_len -= 1
                    lst2_first += 1
                else:
                    break
            flag -= 1
        quick_sort(lst, low, lst1_last)


def select_pivot_median(lst, first, last):
    # 将选取的主元即lst[first],lst[mid],lst[last]的中位数置于first坐标位置
    mid = first + ((last - first) >> 1)  # 计算序列中间元素的下标
    if lst[mid] > lst[last]:
        lst[mid], lst[last] = lst[last], lst[mid]
    if lst[first] > lst[last]:
        lst[first], lst[last] = lst[last], lst[first]
    if lst[mid] > lst[first]:
        lst[mid], lst[first] = lst[first], lst[mid]


def insert_sort(lst, first, last):
    # 插入排序
    for index in range(first + 1, last + 1):
        key = lst[index]
        j = index - 1
        while j >= first:
            if lst[j] > key:
                lst[j + 1] = lst[j]
                lst[j] = key
            j -= 1


def simple_quick_sort(lst):
    quick_sort = lambda l: quick_sort([i for i in l[1:] if i <= l[0]]) + [l[0]] + quick_sort([j for j in l[1:] if j > l[0]]) if l else []
    return quick_sort(lst)


# 测试
if __name__ == "__main__":
    print(simple_quick_sort([5, 3, 3, 2, 4]))
    # sortLst = []
    # sortLst2 = []
    # # 随机初始化序列
    # for i in range(0, 5000000):
    #     element = 1
    #     sortLst.append(element)
    #     sortLst2.append(element)
    # start = time.clock()
    # quick_sort(sortLst, 0, len(sortLst) - 1)
    # end = time.clock()
    # print(end - start)
    # start = time.clock()
    # sortLst2.sort()
    # end = time.clock()
    # print(end - start)
