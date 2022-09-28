# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-04 10:13:01
# LastEditTime: 2020-03-04 10:41:36
# LastEditors: ssdcxy
# Description: 判断二分图
# FilePath: /arithmetic_oj/LeetCode/P0785.py

import json
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def isBipartite(curNode, curColor):
            if colors[curNode] != - 1:
                return curColor == colors[curNode]
            colors[curNode] = curColor
            for nextNode in graph[curNode]:
                if not isBipartite(nextNode, 1-curColor):
                    return False
            return True
        m = len(graph)
        colors = [-1] * m
        for i in range(m):
            if colors[i] == -1 and not isBipartite(i, 0):
                return False
        return True

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
            graph = stringToInt2dArray(line)
            
            ret = Solution().isBipartite(graph)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()