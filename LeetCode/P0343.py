# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-21 08:15:55
# LastEditTime: 2020-02-21 08:32:18
# LastEditors: ssdcxy
# Description: 整数拆分
# FilePath: /arithmetic_oj/LeetCode/P0343.py

import json

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n+1)]
        dp[0] = 0
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(max(i-j, dp[i-j]) * j, dp[i])
        return dp[n]

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
            n = int(line);
            
            ret = Solution().integerBreak(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()