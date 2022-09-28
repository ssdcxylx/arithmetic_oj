# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 15:14:01
# LastEditTime: 2020-12-14 12:29:43
# LastEditors: ssdcxy
# Description: 圆圈中最后剩下的数字
# FilePath: /arithmetic_oj/JianzhiOffer/62.py

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # import sys
        # sys.setrecursionlimit(100000)
        # if n == 1: return 0
        # pre = self.lastRemaining(n-1, m)
        # return (m + pre) % n
        pre = 0
        for i in range(2, n+1):
            pre = (pre+m) % i
        return pre

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
            line = next(lines)
            m = int(line);
            
            ret = Solution().lastRemaining(n, m)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()