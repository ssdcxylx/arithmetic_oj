# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-13 08:18:13
# LastEditTime: 2020-12-14 23:36:24
# LastEditors: ssdcxy
# Description: 求1+2+…+n
# FilePath: /arithmetic_oj/JianzhiOffer/64.py

class Solution:
    def sumNums(self, n: int) -> int:
        return n and n + self.sumNums(n-1)
        
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
            
            ret = Solution().sumNums(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()