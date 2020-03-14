# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 09:23:59
# LastEditTime: 2020-03-10 09:47:13
# LastEditors: ssdcxy
# Description:  剪绳子
# FilePath: /arithmetic_oj/JianzhiOffer/14-1.py

class Solution:
    def cuttingRope(self, n: int) -> int:
        import math
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a-1) * 4)
        return int(math.pow(3, a) * 2)

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