# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 07:54:49
# LastEditTime: 2020-03-12 08:06:16
# LastEditors: ssdcxy
# Description: 礼物的最大价值
# FilePath: /arithmetic_oj/JianzhiOffer/47.py

import json
from typing import List

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m][n]
                    
                    
        
                
        

def stringToInt2dArray(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            grid = stringToInt2dArray(line)
            
            ret = Solution().maxValue(grid)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()