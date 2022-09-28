# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-05 09:30:43
# LastEditTime: 2021-01-13 13:40:58
# LastEditors: ssdcxy
# Description: 冗余连接
# FilePath: /arithmetic_oj/LeetCode/P0684.py

from typing import List
import json

class UnionFind:
    def __init__(self, n: int):
        self.lst = [i for i in range(n)]

    def find(self, i):
        while i != self.lst[i]:
            self.lst[i] = self.lst[self.lst[i]]
            i = self.lst[i]
        return i 

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            return False
        else:
            self.lst[pi] = self.lst[pj]
            return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges: return []
        n = len(edges)
        uf = UnionFind(n)
        for edge in edges:
            if not uf.union(edge[0]-1, edge[1]-1):
                return edge
        return []

            
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
            edges = stringToInt2dArray(line)
            
            ret = Solution().findRedundantConnection(edges)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()