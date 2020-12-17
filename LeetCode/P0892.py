# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-25 07:56:58
# LastEditTime: 2020-03-25 08:05:44
# LastEditors: ssdcxy
# Description: 三维形体的表面积
# FilePath: /arithmetic_oj/LeetCode/P0892.py

import json
from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        def area(l):
            return 6 * l - 2 * (l-1)
        def repeat(i, j, k):
            nonlocal n
            if not (0 <= i < n and 0 <= j < n and grid[i][j] > 0):
                return 0
            if grid[i][j] > k:
                return k
            return grid[i][j]
        if not grid: return 0
        n = len(grid)
        if n == 1: return area(grid[0][0])
        ans = 0
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                if val <= 0:
                    continue
                cur = area(val)
                cur -= (repeat(i+1, j, val) + repeat(i-1, j, val) + repeat(i, j+1, val) + repeat(i, j-1, val))
                ans += cur
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
            
            ret = Solution().surfaceArea(grid)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()