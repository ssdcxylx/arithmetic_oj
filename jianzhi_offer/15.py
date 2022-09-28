# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 10:00:00
# LastEditTime: 2020-03-10 10:07:59
# LastEditors: ssdcxy
# Description: 二进制中1的个数
# FilePath: /arithmetic_oj/JianzhiOffer/15.py

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += 1
            n = n & (n-1)
        return ans
            
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
            
            ret = Solution().hammingWeight(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()