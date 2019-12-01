# -*- coding: utf-8 -*-
# @Time    : 2019-08-06 13:16
# @Author  : ssdcxy
# @Email   : 18379190862@163.com
# @File    : MeanAndVariance.py


def mean_and_variance(lst):
    n = len(lst)
    _sum = 0
    _sum_square = 0
    _mean = 0
    _variance = 0
    for i in range(n):
        _sum += lst[i]
        _sum_square += lst[i]**2
        _mean = _sum / (i+1)
        _variance = 1/(i+1)*_sum_square + _mean**2 - 2 / (i+1) * _mean * _sum
    return _mean, _variance


if __name__ == '__main__':
    lst = [1, 2]
    print(mean_and_variance(lst))