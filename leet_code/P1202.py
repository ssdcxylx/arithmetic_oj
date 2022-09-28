# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-11 09:44:39
# LastEditTime: 2021-01-11 11:18:21
# LastEditors: ssdcxy
# Description: 交换字符串中的元素
# FilePath: /arithmetic_oj/LeetCode/P1202.py

import json
from typing import List

class UnionFind:
    def __init__(self, s):
        self.lst = [i for i in range(len(s))]
    
    def find(self, i):
        while i != self.lst[i]:
            self.lst[i] = self.lst[self.lst[i]]
            i = self.lst[i]
        return i

    def union(self, i, j):
        p_i, p_j = self.find(i), self.find(j)
        self.lst[p_i] = self.lst[p_j]
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        import collections
        uf = UnionFind(s)
        for (x, y) in pairs:
            uf.union(x, y)
        dct = collections.defaultdict(list)
        for i in range(len(s)):
            dct[uf.find(i)].append(i)
        res = list(s)
        for nodes in dct.values():
            string = [res[node] for node in nodes]
            string.sort()
            for node, c in zip(nodes, string):
                res[node] = c
        return ''.join(res)

def stringToString(input):
    return input[1:-1]

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
            s = stringToString(line)
            line = next(lines)
            pairs = stringToInt2dArray(line)
            
            ret = Solution().smallestStringWithSwaps(s, pairs)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()