# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 19:48:09
# LastEditTime: 2020-03-11 20:30:38
# LastEditors: ssdcxy
# Description: 1～n整数中1出现的次数
# FilePath: /arithmetic_oj/JianzhiOffer/43.py

class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        index = 1
        high = n
        low = cur = 0
        while high:
            high //= 10
            cur = (n // index) % 10
            low = n - (n // index) * index
            if cur == 0:
                count += high * index
            elif cur == 1:
                count += high * index + low + 1
            else:
                count += (high+1) * index
            index *= 10
        return count


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
            
            ret = Solution().countDigitOne(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()