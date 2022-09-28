# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-24 22:16:36
# LastEditTime: 2020-03-04 09:54:09
# LastEditors: ssdcxy
# Description: 回文数
# FilePath: /arithmetic_oj/LeetCode/P0009.py


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return False
        if x < 0 or x % 10 == 0:
            return False
        right = 0
        while x > right:
            right = right * 10 + x % 10
            x //= 10
        return x == right or x == right // 10


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

            ret = Solution().isPalindrome(x)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
