# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 16:21:41
# LastEditTime: 2020-02-22 16:47:21
# LastEditors: ssdcxy
# Description: Excel表列名称
# FilePath: /arithmetic_oj/LeetCode/P0168.py


class Solution:
    def convertToTitle(self, n: int) -> str: 
        if n == 0: return ""
        n -= 1
        return self.convertToTitle(n//26) + (chr)(n%26+ord('A'))


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
            
            ret = Solution().convertToTitle(n)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()