# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-07 08:42:11
# LastEditTime: 2020-03-07 09:02:45
# LastEditors: ssdcxy
# Description: 搜索二维矩阵 II
# FilePath: /arithmetic_oj/LeetCode/P0240.py

import json
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix[0]) == 0: return False
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            if target == matrix[row][col]: return True
            elif target < matrix[row][col]: col -= 1
            else: row += 1
        return False
        
        

def stringToInt2dArray(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

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
            line = next(lines)
            target = stringToInt(line)
            
            ret = Solution().searchMatrix(matrix, target)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()