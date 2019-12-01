# -*- coding: utf-8 -*-
# @Time    : 2019-08-06 13:40
# @Author  : ssdcxy
# @Email   : 18379190862@163.com
# @File    : Other.py


def no_repeat_square(lst):
    return len(set([x**2 for x in lst]))


if __name__ == '__main__':
    lst = [-10, -10, -5, 0, 1, 5, 8, 10]
    print(no_repeat_square(lst))

