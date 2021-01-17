# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 15:04:19
# LastEditTime: 2021-01-11 09:54:22
# LastEditors: ssdcxy
# Description: 省份数量
# FilePath: /arithmetic_oj/LeetCode/P0547.py

import json
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(i):
            if lst[i] != i:
                lst[i] = find(lst[i])
            return lst[i]
        def union(i, j):
            pi = find(i)
            pj = find(j)
            lst[pi] = lst[pj]
        cities = len(isConnected)
        lst = [i for i in range(cities)]
        for i in range(cities):
            for j in range(i+1, cities):
                if isConnected[i][j]:
                    union(i, j)
        return sum([1 if lst[i] == i else 0 for i in range(cities)])


def stringToInt2dArray(input):
    return json.loads(input)

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
            M = stringToInt2dArray(line)
            
            ret = Solution().findCircleNum(M)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()