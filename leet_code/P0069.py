# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-18 19:35:54
# LastEditTime: 2019-12-18 20:27:40
# LastEditors: ssdcxy
# Description: x的平方根
# FilePath: /arithmetic_oj/LeetCode/P0069.py


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 1, x
        while left <= right:
            m = int(left + (right - left) / 2)
            sqrt = x / m
            if sqrt == m:
                return m
            elif sqrt > m:
                left = m + 1
            else:
                right = m - 1
        return right


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
            x = int(line)

            ret = Solution().mySqrt(x)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
