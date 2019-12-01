# -*- coding: utf-8 -*-
# @Time    : 2019-08-02 10:12
# @Author  : ssdcxy
# @Email   : 18379190862@163.com
# @File    : ShortestPath.py

inf = float('inf')


def floyd(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if lst[i][j] > lst[i][k] + lst[k][j]:
                    lst[i][j] = lst[i][k] + lst[k][j]
    return lst


if __name__ == '__main__':
    lst = [[0, 2, 6, 4], [inf, 0, 3, inf], [7, inf, 0, 1], [5, inf, 12, 0]]
    print(floyd(lst))
