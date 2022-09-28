# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-27 07:35:27
# LastEditTime: 2020-03-27 07:42:11
# LastEditors: ssdcxy
# Description: 杨辉三角
# FilePath: /arithmetic_oj/LeetCode/P0118.py

import json
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0: return []
        if numRows == 1: return [[1]]
        res = [[1], [1, 1]]
        if numRows == 2: return res
        for i in range(2, numRows):
            cur = [1] * (i+1)
            for j in range(1, i):
                cur[j] = res[i-1][j-1] + res[i-1][j]
            res.append(cur)
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
            line = next(lines)
            numRows = stringToInt(line)
            
            ret = Solution().generate(numRows)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()