# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 08:43:22
# LastEditTime: 2020-12-06 21:56:35
# LastEditors: ssdcxy
# Description: 丑数
# FilePath: /arithmetic_oj/JianzhiOffer/49.py

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2 = i3 = i5 = 0
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            u2, u3, u5 = dp[i2]*2, dp[i3]*3, dp[i5]*5
            dp[i] = min(u2, u3, u5)
            if u2 == dp[i]:        
                i2 += 1
            if u3 == dp[i]:
                i3 += 1
            if u5 == dp[i]:
                i5 += 1
        return dp[n-1]

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
            
            ret = Solution().nthUglyNumber(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()