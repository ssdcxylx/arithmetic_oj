# -*- coding: utf-8 -*-
# @Time    : 2019-08-01 20:17
# @Author  : ssdcxy
# @Email   : 18379190862@163.com
# @File    : ChangeCoins.py


def change_coins(coins, n):
    if n < 0:
        return None
    dp = [0 for i in range(n+1)]
    path = [0 for j in range(n+1)]
    for i in range(1, n+1):
        best = i
        for c in coins:
            if i >= c and best > dp[i-c] + 1:
                best, path[i] = dp[i-c] + 1, i - c
        dp[i] = best
    print(dp[-1])
    while path[n] != 0:
        print(n-path[n], end=" ")
        n = path[n]
    print(n, end=' ')


if __name__ == '__main__':
    # n = input()
    # coins = [int(x) for x in input().split()]
    coins, n = [1, 3, 5], 11
    change_coins(coins, n)
