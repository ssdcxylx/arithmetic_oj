# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 14:32:46
# LastEditTime: 2020-02-20 14:55:35
# LastEditors: ssdcxy
# Description: 岛屿数量
# FilePath: /arithmetic_oj/LeetCode/P0200.py

import json
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if (0 <= r < rows) and (0 <= c < cols) and (r, c) not in seen and grid[r][c] == '1':
                seen.add((r, c))
                for delta in deltas:
                    dfs(r+delta[0], c+delta[1])
        if grid is None or len(grid) == 0 :
            return 0
        count = 0
        seen = set()
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == '1':
                    dfs(row, col)
                    count += 1
        return count


def stringToChar2dArray(input):
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
            grid = stringToChar2dArray(line)
            
            ret = Solution().numIslands(grid)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()