# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 08:04:30
# LastEditTime: 2020-02-22 09:02:33
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0123.py

import json
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0]*n for _ in range(3)]
        for i in range(1, 3):
            pre_max = -prices[0]
            for j in range(1, n):
                pre_max = max(pre_max, dp[i-1][j-1]-prices[j])
                dp[i][j] = max(dp[i][j-1], pre_max + prices[j])
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
            prices = stringToIntegerList(line);
            
            ret = Solution().maxProfit(prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()