# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-07 20:46:00
# LastEditTime: 2019-12-10 20:30:39
# LastEditors: ssdcxy
# Description: 平方数之和
# FilePath: /arithmetic_oj/LeetCode/P0633.py


import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(math.sqrt(c))
        while i <= j:
            pow_sum = i ** 2 + j ** 2
            if pow_sum == c:
                return True
            elif pow_sum > c:
                j -= 1
            else:
                i += 1


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
            c = int(line)

            ret = Solution().judgeSquareSum(c)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
