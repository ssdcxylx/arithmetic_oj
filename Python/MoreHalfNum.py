# -*- coding: utf-8 -*-
# @Time    : 2019-08-05 23:19
# @Author  : ssdcxy
# @Email   : 18379190862@163.com
# @File    : MoreHalfNum.py


def search(lst):
    count = 1
    ans = lst[0]
    for i in range(1, len(lst)):
        if lst[i] == ans:
            count += 1
        else:
            count -= 1
        if count <= 0:
            ans = lst[i]
            count = 1
    return ans


if __name__ == '__main__':
    lst = [2, 1, 3, 2, 2, 1, 2, 3]
    print(search(lst))