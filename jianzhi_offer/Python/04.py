# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-09 21:27:55
# LastEditTime: 2020-03-09 21:38:03
# LastEditors: ssdcxy
# Description: 二维数组中的查找
# FilePath: /arithmetic_oj/JianzhiOffer/04.py


import json
from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
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
            line = lines.next()
            target = stringToInt(line)
            
            ret = Solution().findNumberIn2DArray(matrix, target)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()