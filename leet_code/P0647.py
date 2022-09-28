# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-04 08:37:51
# LastEditTime: 2020-03-04 09:47:29
# LastEditors: ssdcxy
# Description: 回文子串
# FilePath: /arithmetic_oj/LeetCode/P0647.py

class Solution:
    def countSubstrings(self, s: str) -> int:
        m = len(s)
        dp = [[False]*m for i in range(m)]
        res = 0
        for j in range(m):
            for i in range(j, -1, -1):
                if s[i] == s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1
        return res

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
            
            ret = Solution().countSubstrings(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()