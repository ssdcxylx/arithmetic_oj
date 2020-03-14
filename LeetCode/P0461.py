# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-05 11:04:01
# LastEditTime: 2020-03-05 11:05:47
# LastEditors: ssdcxy
# Description: 汉明距离
# FilePath: /arithmetic_oj/LeetCode/P0461.py

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        cnt = 0
        while z != 0:
            z &= (z-1)
            cnt += 1
        return cnt

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
            x = int(line);
            line = next(lines)
            y = int(line);
            
            ret = Solution().hammingDistance(x, y)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()