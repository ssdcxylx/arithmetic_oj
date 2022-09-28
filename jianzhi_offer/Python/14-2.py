# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 09:36:36
# LastEditTime: 2020-03-10 09:59:39
# LastEditors: ssdcxy
# Description: 剪绳子 II
# FilePath: /arithmetic_oj/JianzhiOffer/14-2.py

class Solution:
    def cuttingRope(self, n: int) -> int:
        def helper(x, a, b):
            rem = 1
            while a > 0:
                if a % 2: rem = (rem * x) % 1000000007
                x = x ** 2 % 1000000007
                a //= 2
            return rem
        if n <= 3: return n - 1
        a, b= n // 3 - 1, n % 3
        rem = helper(3, a, b)
        if b == 0: return (rem * 3) % 1000000007
        if b == 1: return (rem * 4) % 1000000007
        return (rem * 6) % 1000000007

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
            
            ret = Solution().cuttingRope(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()