# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-21 10:16:04
# LastEditTime: 2020-02-21 10:49:14
# LastEditors: ssdcxy
# Description: 最长数对链
# FilePath: /arithmetic_oj/LeetCode/P0646.py

import json
from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        for i, val in enumerate(pairs):
            for j in range(i-1, -1, -1):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
                    break
        return max(dp)
                

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
            pairs = stringToInt2dArray(line)
            
            ret = Solution().findLongestChain(pairs)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()