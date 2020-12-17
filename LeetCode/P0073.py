# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-21 16:39:23
# LastEditTime: 2020-03-21 16:57:51
# LastEditors: ssdcxy
# Description: 矩阵置零
# FilePath: /arithmetic_oj/LeetCode/P0073.py

import json
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if is_col:
            for i in range(m):
                matrix[i][0] = 0


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
            
            ret = Solution().setZeroes(matrix)

            out = int2dArrayToString(matrix)
            if ret is not None:
                print("Do not return anything, modify matrix in-place instead.")
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()