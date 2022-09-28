# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-05 08:15:33
# LastEditTime: 2021-01-05 08:16:05 
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0830.py

import json
from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if not s: return []
        n = len(s)
        prev_index = 0
        cur = s[0]
        res = []
        for i in range(1, n):
            if s[i] != cur:
                if i - prev_index >= 3:
                    res.append([prev_index, i-1])
                cur = s[i]
                prev_index = i
        if n - prev_index >= 3:
            res.append([prev_index, n-1])
        return res

def stringToString(input):
    return input[1:-1]

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
            line = lines.next()
            s = stringToString(line)
            
            ret = Solution().largeGroupPositions(s)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()