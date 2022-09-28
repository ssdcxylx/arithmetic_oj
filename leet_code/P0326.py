# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-23 07:35:51
# LastEditTime: 2020-02-23 07:37:48
# LastEditors: ssdcxy
# Description: 3的幂
# FilePath: /arithmetic_oj/LeetCode/P0326.py

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and ((3**19)%n)

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
            
            ret = Solution().isPowerOfThree(n)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()