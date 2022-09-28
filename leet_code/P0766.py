# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-07 12:03:23
# LastEditTime: 2020-03-07 12:16:41
# LastEditors: ssdcxy
# Description: 托普利茨矩阵
# FilePath: /arithmetic_oj/LeetCode/P0766.py

import json
from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix or len(matrix[0]) == 0: return False
        m, n = len(matrix), len(matrix[0])
        for i in range(n):
            j, k, val = 0, i, matrix[0][i]
            while j + 1 < m and k + 1 < n:
                if matrix[j+1][k+1] != val:
                    return False 
                j += 1
                k += 1
        for j in range(m):
            i, k, val = j, 0, matrix[j][0]
            while i + 1 < m and k + 1 < n:
                if matrix[i+1][k+1] != val:
                    return False 
                i += 1
                k += 1
        return True
            



def stringToInt2dArray(input):
    return json.loads(input)

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
            
            ret = Solution().isToeplitzMatrix(matrix)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()