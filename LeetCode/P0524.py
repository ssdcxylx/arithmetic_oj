# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-08 20:57:04
# LastEditTime: 2019-12-10 20:30:11
# LastEditors: ssdcxy
# Description: 通过删除字母匹配到字典里最长单词
# FilePath: /arithmetic_oj/LeetCode/P0524.py


from typing import List
import json


class Solution(object):
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longest = ''
        for i in d:
            l1, l2 = len(s) - 1, len(i) - 1
            if l1 < l2 or (l1 == l2 and s != i):
                continue
            while l1 >= 0 and l2 >= 0:
                if s[l1] == i[l2]:
                    l1 -= 1
                    l2 -= 1
                else:
                    l1 -= 1
            if l2 == -1:
                if len(i) > len(longest) or(len(i) == len(longest) and i < longest):
                    longest = i
        return longest


def stringToString(input):
    return input[1:-1]


def stringToStringArray(input):
    return json.loads(input)


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line)
            line = next(lines)
            d = stringToStringArray(line)

            ret = Solution().findLongestWord(s, d)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
