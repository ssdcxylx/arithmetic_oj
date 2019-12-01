# -*- coding: utf-8 -*-
# @Time    : 2019-08-02 10:42
# @Author  : ssdcxy
# @Email   : 18379190862@163.com
# @File    : LongestPalindrome.py


def lp(s):
    n = len(s)
    dp = [[1 for j in range(n)]
          for i in range(n)]
    left = 0
    max_l = 1
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            dp[i][j] = (s[i] == s[j]) & dp[i+1][j-1]
            if dp[i][j] and max_l < j - i + 1:
                max_l = j-i+1
                left = i
    return s[left:max_l+left]


if __name__ == '__main__':
    str = 'abbaba'
    print(lp(str))
