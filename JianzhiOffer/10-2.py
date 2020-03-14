# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 08:23:41
# LastEditTime: 2020-03-10 08:25:41
# LastEditors: ssdcxy
# Description: 青蛙跳台阶问题
# FilePath: /arithmetic_oj/JianzhiOffer/10-2.py

class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, (a+b)%1000000007
        return a

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
            
            ret = Solution().numWays(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()