# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-24 22:22:01
# LastEditTime: 2019-12-10 20:30:18
# LastEditors: ssdcxy
# Description: 反转字符串中的单词3
# FilePath: /arithmetic_oj/LeetCode/P0557.py


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        tmp = []
        for c in s:
            tmp.append(c[::-1])
        s = ' '.join(tmp)
        return s


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

            ret = Solution().reverseWords(s)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
