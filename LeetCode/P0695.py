# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-19 20:41:33
# LastEditTime: 2020-02-20 14:49:45
# LastEditors: ssdcxy
# Description: 岛屿的最大面积
# FilePath: /arithmetic_oj/LeetCode/P0695.py

import json

class Solution(object):
    def maxAreaOfIsland(self, grid):
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) + area(r, c+1) + area(r, c-1))
        seen = set()
        return max(area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))


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
            
            ret = Solution().maxAreaOfIsland(grid)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()