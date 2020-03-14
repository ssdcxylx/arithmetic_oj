# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 20:31:45
# LastEditTime: 2020-03-11 21:13:12
# LastEditors: ssdcxy
# Description:  数字序列中某一位的数字
# FilePath: /arithmetic_oj/JianzhiOffer/44.py

class Solution:
    def findNthDigit(self, n: int) -> int:
        if not n: return 0
        i = 0
        count = 1
        while n - count > 0:
            n -= count
            count = (i+1) * (10 ** (i+1) - 10 ** (i))
            i += 1
        num = n // i + 10 ** (i-1)
        pos = n % i
        return str(num)[pos]
            





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