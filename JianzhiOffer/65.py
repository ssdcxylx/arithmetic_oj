# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-13 08:20:59
# LastEditTime: 2020-12-14 23:49:33
# LastEditors: ssdcxy
# Description: 不用加减乘除做加法
# FilePath: /arithmetic_oj/JianzhiOffer/65.py

class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xFFFFFFFF
        a, b = a&x, b&x
        while b:
            a, b = (a^b), (a&b)<<1&x
        return a if a <= 0x7FFFFFFF else ~(a^x)

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
            a = int(line);
            line = next(lines)
            b = int(line);
            
            ret = Solution().add(a, b)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()