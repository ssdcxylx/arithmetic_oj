# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-15 20:31:28
# LastEditTime: 2021-01-15 21:38:58
# LastEditors: ssdcxy
# Description: 移除最多的同行或同列石头
# FilePath: /arithmetic_oj/LeetCode/P0947.py

import json
from typing import List

class UnionFind:
    def __init__(self):
        self.dct = dict()
    
    def find(self, x):
        if x not in self.dct:
            self.dct[x] = x
        while x != self.dct[x]:
            self.dct[x] = self.dct[self.dct[x]]
            x = self.dct[x]
        return x

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.dct[py] = px

    def count(self):
        return sum(1 for x, y in self.dct.items() if x == y)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        for x, y in stones:
            uf.union(x, y + 10001)
        return len(stones) - uf.count()

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
            line = lines.next()
            stones = stringToInt2dArray(line)
            
            ret = Solution().removeStones(stones)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()