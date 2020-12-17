# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-22 07:57:32
# LastEditTime: 2020-03-22 08:22:56
# LastEditors: ssdcxy
# Description: 旋转图像
# FilePath: /arithmetic_oj/LeetCode/P0048.py

import json
from typing import List

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n//2 + 1):
            for j in range(i, n//2 + 1):
                tmp = matrix[n-1-j][i]
                matrix[n-j-1][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = tmp
                

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
            
            ret = Solution().rotate(matrix)

            out = int2dArrayToString(matrix)
            if ret is not None:
                print("Do not return anything, modify matrix in-place instead.")
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()