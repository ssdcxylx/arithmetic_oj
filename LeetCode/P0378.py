# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-07 09:03:09
# LastEditTime: 2020-03-07 09:47:36
# LastEditors: ssdcxy
# Description: 有序矩阵中第K小的元素
# FilePath: /arithmetic_oj/LeetCode/P0378.py

import json
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or len(matrix[0]) == 0: return -1
        m, n = len(matrix), len(matrix[0])
        start, end = matrix[0][0], matrix[m-1][n-1]
        while start <= end:
            mid = start + (end - start) // 2
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] > mid:
                        break
                    cnt += 1
            if cnt < k: start = mid + 1
            else: end = mid - 1
        return start

                

def stringToInt2dArray(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

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
            k = stringToInt(line)
            
            ret = Solution().kthSmallest(matrix, k)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()