# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 09:14:02
# LastEditTime: 2020-02-22 09:24:16
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
        dp = [[0]*(n) for _ in range(k+1)]
        for i in range(1, k+1):
            pre_max = -prices[0]
            for j in range(1, n):
                pre_max = max(pre_max, dp[i-1][j-1]-prices[j])
                dp[i][j] = max(dp[i][j-1], pre_max+prices[j])
        return dp[-1][-1]

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