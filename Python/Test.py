# -*- coding: utf-8 -*-
# @time       : 2019-10-09 14:37
# @author     : ssdcxy
# @email      : 18379190862@163.com
# @file       : Test.py
# @description:


if __name__ == '__main__':
    l = [5, 3, 1, 2, 4]
    quicksort = lambda l: quicksort([i for i in l[1:] if i < l[0]]) + [l[0]] + quicksort([j for j in l[1:] if j >= l[0]]) if l else []
    print(quicksort(l))