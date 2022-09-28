# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-04 07:44:36
# LastEditTime: 2020-03-04 08:35:06
# LastEditors: ssdcxy
# Description: 腐烂的橘子
# FilePath: /arithmetic_oj/LeetCode/P0994.py

from typing import List
import json

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def dfs(i, j, val):
            nonlocal m, n
            grid[i][j] = val
            deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for delta in deltas:
                a, b = i+delta[0], j+delta[1]
                if 0 <= a < m and 0 <= b < n and (grid[a][b] == 1 or grid[a][b] - grid[i][j] > 1):
                    dfs(a, b, val+1)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dfs(i, j, 2)
        _max = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                _max = max(_max, grid[i][j])
        return _max - 2 if _max >= 2 else 0

                            
        

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
            
            ret = Solution().orangesRotting(grid)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()