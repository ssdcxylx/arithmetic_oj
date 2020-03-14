# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-23 07:33:38
# LastEditTime: 2020-02-23 07:34:35
# LastEditors: ssdcxy
# Description: 有效的完全平方数
# FilePath: /arithmetic_oj/LeetCode/P0367.py

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        subNum = 1
        while num > 0:
            num -= subNum
            subNum += 2
        return num == 0

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
            
            ret = Solution().isPerfectSquare(num)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()