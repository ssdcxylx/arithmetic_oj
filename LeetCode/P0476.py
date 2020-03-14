# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-06 08:34:27
# LastEditTime: 2020-03-06 08:40:26
# LastEditors: ssdcxy
# Description: 数字的补数
# FilePath: /arithmetic_oj/LeetCode/P0476.py

class Solution:
    def findComplement(self, num: int) -> int:
        mask = num
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return num ^ mask

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
            num = int(line);
            
            ret = Solution().findComplement(num)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()