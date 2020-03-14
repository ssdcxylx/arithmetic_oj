# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 17:59:54
# LastEditTime: 2020-02-20 20:30:14
# LastEditors: ssdcxy
# Description: 爬楼梯
# FilePath: /arithmetic_oj/LeetCode/P0070.py

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(2, n):
            cur = a + b
            a, b = b, cur
        return b
            

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
            
            ret = Solution().climbStairs(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()