# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 09:14:02
# LastEditTime: 2020-03-20 08:27:40
# LastEditors: ssdcxy
# Description: 买卖股票的最佳时机 IV
# FilePath: /arithmetic_oj/LeetCode/P0188.py

import json
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        if k > n:
            profit = 0
            for i in range(1, n):
                diff = prices[i] - prices[i - 1]
                profit += (diff if diff > 0 else 0)
            return profit
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(k, 0, -1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -float('inf')
                    continue
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i-1])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i-1])
        return dp[n][k][0]

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            k = int(line);
            line = next(lines)
            prices = stringToIntegerList(line);
            
            ret = Solution().maxProfit(k, prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()