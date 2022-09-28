# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-21 21:41:13
# LastEditTime: 2020-12-14 14:21:49
# LastEditors: ssdcxy
# Description: 最佳买卖股票时机含冷冻期
# FilePath: /arithmetic_oj/LeetCode/P0309.py

import json
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]
        for i in range(n+1):
            if i == 0:                         
                dp[i][0] = 0
                dp[i][1] = -float('inf')
            if i == 1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i-1])
        return dp[n][0]
            

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
            prices = stringToIntegerList(line);
            
            ret = Solution().maxProfit(prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()