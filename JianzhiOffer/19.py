# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 10:28:25
# LastEditTime: 2020-03-10 11:05:35
# LastEditors: ssdcxy
# Description: 正则表达式匹配
# FilePath: /arithmetic_oj/JianzhiOffer/19.py

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if j == 0:
                    dp[i][j] = (i == 0)
                else:
                    if p[j-1] != "*":
                        if i > 0 and (s[i-1] == p[j-1] or p[j-1] == "."):
                            dp[i][j] = dp[i-1][j-1]
                    else:
                        if j >= 2:
                            dp[i][j] = dp[i][j-2]
                        if i >= 1 and j >= 2 and (s[i-1] == p[j-2] or p[j-2] == "."):
                            dp[i][j] |= dp[i-1][j]
        return dp[m][n]
                

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
            s = stringToString(line);
            line = next(lines)
            p = stringToString(line);
            
            ret = Solution().isMatch(s, p)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()