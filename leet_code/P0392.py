# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-10 21:42:33
# LastEditTime: 2019-12-10 21:56:12
# LastEditors: ssdcxy
# Description:  判断子序列
# FilePath: /arithmetic_oj/LeetCode/P0392.py


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = -1
        for c in s:
            index = t.find(c, index+1)
            if index == -1:
                return False
        return True


def stringToString(input):
    return input[1: -1]


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
            s = stringToString(line)
            line = next(lines)
            t = stringToString(line)

            ret = Solution().isSubsequence(s, t)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
