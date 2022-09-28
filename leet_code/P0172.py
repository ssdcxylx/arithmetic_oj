# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 16:44:44
# LastEditTime: 2020-02-22 16:56:10
# LastEditors: ssdcxy
# Description: 阶乘后的零
# FilePath: /arithmetic_oj/LeetCode/P0172.py

class Solution:
    def trailingZeroes(self, n: int) -> int:
        return int(0 if n == 0 else n // 5 + self.trailingZeroes(n/5))

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
            
            ret = Solution().trailingZeroes(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()