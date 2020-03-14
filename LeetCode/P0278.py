# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-18 23:20:59
# LastEditTime: 2019-12-18 23:44:03
# LastEditors: ssdcxy
# Description: 第一个错误的版本
# FilePath: /arithmetic_oj/LeetCode/P0278.py


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left < right:
            mid = int(left + (right - left) / 2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


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
            n = int(line)
            line = next(lines)
            bad = int(line)

            ret = Solution().firstBadVersion(n, bad)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
