# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 08:14:12
# LastEditTime: 2020-03-10 08:23:00
# LastEditors: ssdcxy
# Description: 斐波那契数列
# FilePath: /arithmetic_oj/JianzhiOffer/10.py

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, (a + b) % 1000000007
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
            
            ret = Solution().fib(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()