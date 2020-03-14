# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-05 09:30:43
# LastEditTime: 2020-03-05 10:59:31
# LastEditors: ssdcxy
# Description: 冗余连接
# FilePath: /arithmetic_oj/LeetCode/P0684.py

from typing import List
import json

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(cur):
            while tmp[cur] != cur:
                cur = tmp[cur]
            return cur
        def union(u, v):
            fu = find(u)
            fv = find(v)
            if fu != fv:
                if rank[fv] > rank[fu]:
                    tmp[fv] = tmp[fu]
                else:
                    tmp[fu] = tmp[fv]
                    rank[fv] += 1
        tmp = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]
        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            else:
                union(u, v)

            
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