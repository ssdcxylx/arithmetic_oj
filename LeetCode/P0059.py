# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-19 16:39:50
# LastEditTime: 2020-03-19 16:46:22
# LastEditors: ssdcxy
# Description: 螺旋矩阵 II
# FilePath: /arithmetic_oj/LeetCode/P0059.py

import json
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n: return [[]]
        res = [[0] * n for i in range(n)]
        t, b, l, r = 0, n-1, 0, n - 1
        cur = 1
        while True:
            for i in range(l, r+1):
                res[t][i] = cur
                cur += 1
            t += 1
            if t > b: break
            for i in range(t, b+1):
                res[i][r] = cur
                cur += 1
            r -= 1
            if l > r: break
            for i in range(r, l-1, -1):
                res[b][i] = cur
                cur += 1
            if t > b: break
            b -= 1
            for i in range(b, t-1, -1):
                res[i][l] = cur
                cur += 1
            l += 1
            if l > r: break
        return res
                


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
            line = lines.next()
            n = stringToInt(line)
            
            ret = Solution().generateMatrix(n)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()