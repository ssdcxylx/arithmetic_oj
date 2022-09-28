# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-16 11:38:27
# LastEditTime: 2021-01-16 17:54:45
# LastEditors: ssdcxy
# Description: 打砖块
# FilePath: /arithmetic_oj/LeetCode/P0903.py

import json
from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.lst = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, i: int) -> None:
        while i != self.lst[i]:
            self.lst[i] = self.lst[self.lst[i]]
            i = self.lst[i]
        return i
    
    def union(self, i: int, j: int) -> None:
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj: return
        self.lst[pi] = self.lst[pj]
        self.rank[pj] += self.rank[pi]

    def size(self, i):
        return self.rank[self.find(i)]
    
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n + 1)
        status = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                status[i][j] = grid[i][j]
        for i, j in hits:
            status[i][j] = 0
        for i in range(m):
            for j in range(n):
                if status[i][j]:
                    if i == 0:
                        uf.union(m * n, i * n + j)
                    if i > 0 and status[i-1][j]:
                        uf.union(i * n + j, (i - 1) * n + j)
                    if j > 0 and status[i][j-1]:
                        uf.union(i * n + j, i * n + j - 1)
        directions = ([0, 1], [1, 0], [0, -1], [-1, 0])
        res = [0 for _ in range(len(hits))]
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i][0], hits[i][1]
            if not grid[r][c]:
                continue
            prev = uf.size(m * n)
            if not r:
                uf.union(c, m * n)
            for direction in directions:
                dr, dc = direction[0], direction[1]
                fr, fc = r + dr, c + dc
                if fr >= 0 and fr < m and fc >= 0 and fc < n:
                    if status[fr][fc]:
                        uf.union(r * n + c, fr * n + fc)
            size = uf.size(m * n)
            res[i] = max(0, size - prev - 1)
            status[r][c] = 1
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
            line = lines.next()
            grid = stringToInt2dArray(line)
            line = lines.next()
            hits = stringToInt2dArray(line)
            
            ret = Solution().hitBricks(grid, hits)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()