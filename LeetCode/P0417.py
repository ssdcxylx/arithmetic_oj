# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 17:02:33
# LastEditTime: 2020-02-20 17:43:05
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0417.py

import json
from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def dfs(row, col, cur, res):
            res.add((row, col))
            for delta in deltas:
                if 0 <= row + delta[0] < rows and 0 <= col + delta[1] < cols:
                    if (row+delta[0], col+delta[1]) not in res and matrix[row+delta[0]][col+delta[1]] >= matrix[row][col]:
                        dfs(row+delta[0],col+delta[1], matrix[row][col], res)
        if not matrix or not matrix[0]: return
        rows, cols = len(matrix), len(matrix[0])
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res1 = set()
        res2 = set()
        for row in range(rows):
            # 太平洋
            dfs(row, 0, 0, res1)
            # 大西洋
            dfs(row, cols-1, 0, res2)
        for col in range(cols):
            # 太平洋
            dfs(0, col, 0, res1)
            # 大西洋
            dfs(rows-1, col, 0, res2)
        return list(res1 & res2)

def stringToInt2dArray(input):
    return json.loads(input)

def int2dArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            matrix = stringToInt2dArray(line)
            
            ret = Solution().pacificAtlantic(matrix)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()