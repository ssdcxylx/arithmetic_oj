# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 08:43:22
# LastEditTime: 2020-03-12 09:00:20
# LastEditors: ssdcxy
# Description: 丑数
# FilePath: /arithmetic_oj/JianzhiOffer/49.py

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2 = p3 = p5 = 0
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1
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