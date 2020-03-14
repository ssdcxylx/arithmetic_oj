# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 15:04:19
# LastEditTime: 2020-02-20 15:29:00
# LastEditors: ssdcxy
# Description: 朋友圈
# FilePath: /arithmetic_oj/LeetCode/P0547.py

import json
from typing import List

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(row):
            for col in range(cols):
                if col not in visited and M[row][col] == 1:
                    visited.add(col)
                    dfs(col)
        if M is None or len(M) == 0:
            return 0
        count = 0
        rows, cols = len(M), len(M[0])
        visited = set()
        for row in range(rows):
            if row not in visited:
                visited.add(row)
                dfs(row)
                count += 1
        return count


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