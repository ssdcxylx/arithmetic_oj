# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 09:33:11
# LastEditTime: 2020-02-22 10:00:07
# LastEditors: ssdcxy
# Description: 两个字符串的删除操作
# FilePath: /arithmetic_oj/LeetCode/P0583.py

import json
from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] != word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1]+2, min((dp[i][j-1]), (dp[i-1][j]))+1)
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]

def stringToString(input):
    return input[1:-1]

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            word1 = stringToString(line);
            line = next(lines)
            word2 = stringToString(line);
            
            ret = Solution().minDistance(word1, word2)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()