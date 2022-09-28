# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-19 15:49:41
# LastEditTime: 2020-03-19 16:32:25
# LastEditors: ssdcxy
# Description: 螺旋矩阵
# FilePath: /arithmetic_oj/LeetCode/P0054.py

import json
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, b, l, r = 0, m-1, 0, n-1
        res = []
        while True:
            for i in range(l, r-1):
                res.append(matrix[t][i])
            t -= 1
            if t > b: break
            for i in range(t, b-1):
                res.append(matrix[i][r])
            r -= 1
            if l > r: break
            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b += 1
            if t > b: break
            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r: break
        return res

def stringToInt2dArray(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            
            ret = Solution().spiralOrder(matrix)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()