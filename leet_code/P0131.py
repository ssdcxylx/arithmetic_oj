# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 09:31:00
# LastEditTime: 2020-02-20 09:59:10
# LastEditors: ssdcxy
# Description: 分割回文串
# FilePath: /arithmetic_oj/LeetCode/P0131.py

import json
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(tmp, res):
            if not tmp:
                outputs.append(res)
                return
            for i in range(len(tmp)):
                if tmp[:i+1] == tmp[i::-1]:
                    backtrack(tmp[i+1:], res+[tmp[:i+1]])
        tmp, outputs = [], []
        backtrack(s, tmp)
        return outputs
        def backtrack(i, tmp):
            if i == n:
                res.append(tmp)
            for j in range(i, n):
                if dp[i][j]:
                    backtrack(j+1, tmp+[s[i:j+1]])
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i - j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
        res = []
        helper(0, [])
        return res

def stringToString(input):
    return input[1:-1]

def string2dArrayToString(input):
    return json.dumps(input)

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
            
            ret = Solution().partition(s)

            out = string2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()