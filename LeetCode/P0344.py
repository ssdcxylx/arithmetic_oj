# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-24 22:43:28
# LastEditTime: 2019-12-10 20:24:50
# LastEditors: ssdcxy
# Description: 反转字符串
# FilePath: /arithmetic_oj/LeetCode/P0344.py


from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s = s[::-1]
        print(s)


def stringToString(input):
    return input[1:-1].decode('string_escape')


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
            s = line

            ret = Solution().reverseString(s)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
