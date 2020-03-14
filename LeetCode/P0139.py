# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-21 17:18:04
# LastEditTime: 2020-02-21 17:32:22
# LastEditors: ssdcxy
# Description: 单词拆分
# FilePath: /arithmetic_oj/LeetCode/P0139.py


import json
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]

def stringToString(input):
    return input[1:-1]

def stringToStringArray(input):
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
            wordDict = stringToStringArray(line)
            
            ret = Solution().wordBreak(s, wordDict)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()