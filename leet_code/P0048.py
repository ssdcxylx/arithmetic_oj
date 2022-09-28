# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-22 07:57:32
# LastEditTime: 2020-12-19 09:59:11
# LastEditors: ssdcxy
# Description: 旋转图像
# FilePath: /arithmetic_oj/LeetCode/P0048.py

import json
from typing import List

class Solution(object):
    def rotate(self, matrix):
        if not matrix: return
        n = len(matrix)
        for i in range(n//2+1):
            for j in range(i, n-i-1):
                matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] =\
                     matrix[n-j-1][i], matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1]
                

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