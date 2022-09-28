# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-07 08:22:33
# LastEditTime: 2020-03-07 08:35:49
# LastEditors: ssdcxy
# Description: 重塑矩阵
# FilePath: /arithmetic_oj/LeetCode/P0566.py

import json
from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums: return nums
        tmp = []
        m, n = len(nums), len(nums[0])
        for i in range(m):
            for j in range(n):
                tmp.append(nums[i][j])
        if r * c != m * n:
            return nums
        res = [[0] * c for i in range(r)]
        for i in range(r):
            for j in range(c):
                res[i][j] = tmp[c*i+j]
        return res
def stringToInt2dArray(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

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
            nums = stringToInt2dArray(line)
            line = next(lines)
            r = stringToInt(line)
            line = next(lines)
            c = stringToInt(line)
            
            ret = Solution().matrixReshape(nums, r, c)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()