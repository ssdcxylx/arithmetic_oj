# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-24 22:16:07
# LastEditTime: 2019-12-10 20:14:28
# LastEditors: ssdcxy
# Description: 整数反转
# FilePath: /arithmetic_oj/LeetCode/P0007.py


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            is_negative = True
        else:
            is_negative = False
        s = str(abs(x))
        s = s[::-1]
        x = int(s)
        if is_negative:
            if x > 2**31:
                x = 0
            x = -x
        else:
            if x > 2 ** 31 - 1:
                x = 0
        return x


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

            ret = Solution().reverse(x)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
