# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-05 14:23:53
# LastEditTime: 2020-03-05 14:24:53
# LastEditors: ssdcxy
# Description: 2的幂
# FilePath: /arithmetic_oj/LeetCode/P0231.py

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

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
            
            ret = Solution().isPowerOfTwo(n)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()