# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-05 11:49:04
# LastEditTime: 2020-03-05 12:00:23
# LastEditors: ssdcxy
# Description: 颠倒二进制位
# FilePath: /arithmetic_oj/LeetCode/P0190.py

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 32
        
        while count:
            res <<= 1
            res += n&1
            n >>= 1
            count -= 1
            
        return int(bin(res), 2)
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
            
            ret = Solution().reverseBits(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()