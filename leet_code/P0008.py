# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-24 22:16:22
# LastEditTime: 2019-12-10 20:14:39
# LastEditors: ssdcxy
# Description: 字符串转换整数
# FilePath: /arithmetic_oj/LeetCode/P0008.py


class Solution:
    def myAtoi(self, _str: str) -> int:
        l = len(_str)
        if l <= 0:
            return 0
        start = 0
        while start < l and _str[start] == " ":
            start += 1
        end = start
        if start < l and _str[start] != "-" and _str[start] != "+" and not _str[start].isnumeric():
            return 0
        else:
            end += 1
        while end < l and (_str[end].isnumeric()):
            end += 1
        try:
            number = int(_str[start:end])
        except:
            return 0
        if number >= 2 ** 31:
            return 2 ** 31 - 1
        if number < -2 ** 31:
            return -2 ** 31
        return number


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
            _str = line

            ret = Solution().myAtoi(_str)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
