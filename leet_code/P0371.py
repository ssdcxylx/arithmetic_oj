# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-06 08:40:58
# LastEditTime: 2020-03-06 08:48:00
# LastEditors: ssdcxy
# Description:  两整数之和
# FilePath: /arithmetic_oj/LeetCode/P00371.py

class Solution:
    def getSum(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
        return a if a < 0x80000000 else -(a^0xFFFFFFFF)

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
            
            ret = Solution().getSum(a, b)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()