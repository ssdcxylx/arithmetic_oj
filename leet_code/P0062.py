# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 20:50:53
# LastEditTime: 2020-02-20 21:15:56
# LastEditors: ssdcxy
# Description: 不同路径
# FilePath: /arithmetic_oj/LeetCode/P0062.py

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[1 for _ in range(n)] for _ in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[m-1][n-1]
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

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
            m = int(line);
            line = next(lines)
            n = int(line);
            
            ret = Solution().uniquePaths(m, n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()