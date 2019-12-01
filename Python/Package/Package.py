# -*- coding: utf-8 -*-
# @Time    : 2019-08-01 21:40
# @Author  : ssdcxy
# @Email   : 18379190862@163.com
# @File    : Package.py


def package(V, v, w):
    dp = [0 for i in range(V+1)]
    for i in range(1, V+1):
        best = 0
        for j in range(0, len(v)):
            if i >= v[j] and best < dp[i-v[j]] + w[j]:
                best = dp[i-v[j]] + w[j]
        dp[i] = best
    print(dp[-1])


def zero_one_package(V, v, w):
    n = len(v)
    dp = [[0 for i in range(V+1)]
          for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, V+1):
            if j < v[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[i-1]]+w[i-1])
    print(dp[n][V])


if __name__ == '__main__':
    V, v, w = 9, [2, 3, 4, 5], [3, 4, 5, 7]
    zero_one_package(V, v, w)

