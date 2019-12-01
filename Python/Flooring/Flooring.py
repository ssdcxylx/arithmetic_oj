# -*- coding: utf-8 -*-
# @Time    : 2019-08-05 23:07
# @Author  : ssdcxy
# @Email   : 18379190862@163.com
# @File    : Flooring.py


def floor(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return floor(n-1) + floor(n-2)


if __name__ == '__main__':
    print(floor(10))