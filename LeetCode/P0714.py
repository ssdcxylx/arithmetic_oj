# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 07:55:31
# LastEditTime: 2020-02-22 08:03:30
# LastEditors: ssdcxy
# Description: 买卖股票的最佳时机含手续费
# FilePath: /arithmetic_oj/LeetCode/P0714.py

import json
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n+1)]
        prices.insert(0, 0)
        dp[1][1] = -prices[1]
        for i in range(2, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
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
            line = next(lines)
            fee = int(line);
            
            ret = Solution().maxProfit(prices, fee)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()