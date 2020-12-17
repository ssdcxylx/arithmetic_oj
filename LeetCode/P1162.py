# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-29 09:14:20
# LastEditTime: 2020-03-29 09:48:48
# LastEditors: ssdcxy
# Description: 地图分析
# FilePath: /arithmetic_oj/LeetCode/P1162.py

import json
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        _set = set()
        dp = [[float('inf')]*n for _ in range(n)]
        cnt = 0
        ans = 0
        tmp = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    tmp.append((i, j))
                    _set.add((i, j))
                    dp[i][j] = 0
                    cnt += 1
        if cnt == n * n or cnt == 0:
            return -1
        while tmp:
            (x, y) = tmp.pop(0)
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= i < n and 0 <= j < n and (i, j) not in _set:
                    dp[i][j] = min(dp[i][j], dp[x][y] + 1)
                    ans = max(ans, dp[i][j])
                    _set.add((i, j))
                    tmp.append((i, j))
        return ans

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
            
            ret = Solution().maxDistance(grid)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()