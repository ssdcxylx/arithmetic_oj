# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-21 14:39:19
# LastEditTime: 2020-02-21 17:06:08
# LastEditors: ssdcxy
# Description: 一和零
# FilePath: /arithmetic_oj/LeetCode/P0474.py

import json
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs: return 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        for _str in strs:
            count0 = _str.count('0')
            count1 = _str.count('1')
            for i in range(m, count0-1, -1):
                for j in range(n, count1-1, -1):
                    dp[i][j] = max(dp[i][j], 1+dp[i-count0][j-count1])
        return dp[m][n]


def stringToStringArray(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

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
            strs = stringToStringArray(line)
            line = next(lines)
            m = stringToInt(line)
            line = next(lines)
            n = stringToInt(line)
            
            ret = Solution().findMaxForm(strs, m, n)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()