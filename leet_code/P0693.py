# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-06 08:25:18
# LastEditTime: 2020-03-06 08:31:46
# LastEditors: ssdcxy
# Description: 交替位二进制数
# FilePath: /arithmetic_oj/LeetCode/P0693.py

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n ^= 0b1010101010101010
        if n == 0 or n & (n+1) == 0:
            return True
        return False

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
            
            ret = Solution().hasAlternatingBits(n)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()