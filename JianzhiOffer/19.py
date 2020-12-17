# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 10:28:25
# LastEditTime: 2020-11-25 23:40:20
# LastEditors: ssdcxy
# Description: 正则表达式匹配
# FilePath: /arithmetic_oj/JianzhiOffer/19.py

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j-2] and p[j-1] == "*"
        for i in range(1, m):
            for j in range(1, n):
                if p[j-1] == "*":
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == "."))
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == ".")
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