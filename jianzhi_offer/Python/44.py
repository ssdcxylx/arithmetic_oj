# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 20:31:45
# LastEditTime: 2020-12-05 23:36:25
# LastEditors: ssdcxy
# Description:  数字序列中某一位的数字
# FilePath: /arithmetic_oj/JianzhiOffer/44.py

class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10: return n
        i = 1
        count = 9
        while n - count > 0:
            n -= count
            count = (i+1) * (10 ** (i+1) - 10 ** i)
            i += 1
        num = (n - 1) // i + 10 ** (i-1)
        pos = (n - 1) % i
        return (num // (10 ** (i-1-pos))) % 10
            


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
            
            ret = Solution().findNthDigit(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()