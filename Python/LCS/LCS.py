# -*- coding: utf-8 -*-
# @Time    : 2019-08-05 20:40
# @Author  : ssdcxy
# @Email   : 18379190862@163.com
# @File    : LCS1.py


def lcs2(a, b):
    n, m = len(a), len(b)
    dp = [[0 for j in range(m+1)]
          for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[n][m])


def lcs1(a, b):
    n, m = len(a), len(b)
    dp = [0 for i in range(m+1)]
    pre = [0 for i in range(m+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[j] = pre[j-1] + 1
            else:
                dp[j] = max(dp[j-1], pre[j])
            pre[j-1] = dp[j-1]
        pre[m] = dp[m]
    print(dp[m])


if __name__ == '__main__':
    a = "xyxxzxyzxy"
    b = "zxzyyzxxyxxz"
    lcs1(a, b)