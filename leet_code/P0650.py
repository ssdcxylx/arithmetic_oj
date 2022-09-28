# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 10:55:05
# LastEditTime: 2020-02-22 11:50:19
# LastEditors: ssdcxy
# Description: 只有两个键的键盘
# FilePath: /arithmetic_oj/LeetCode/P0650.py

import json
from typing import List

class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans
        # dp = [[0] * n for _ in range(n)]
        # for j in range(1, n):
        #     dp[0][j] = j+1
        # for i in range(1, n):
        #     for j in range(i, n):
        #         cur = j - (i+1)
        #         count = 2
        #         while (cur - (i+1)) >= 0:
        #             count += 1
        #             cur -= (i+1)
        #         if dp[i][cur] > 0:
        #             dp[i][j] = min(dp[i-1][j], dp[i-1][cur]+count)
        #         else:
        #             dp[i][j] = dp[i-1][j]
        # return dp[-1][-1]
                
                 
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
            
            ret = Solution().minSteps(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()