# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-08 20:57:04
# LastEditTime: 2021-01-14 10:40:53
# LastEditors: ssdcxy
# Description: 通过删除字母匹配到字典里最长单词
# FilePath: /arithmetic_oj/LeetCode/P0524.py


from typing import List
import json


class Solution(object):
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ans = ""
        for string in d:
            l1, l2 = len(s) - 1, len(string) - 1
            if l1 < l2 or (l1 == l2 and string != s):
                continue
            while l1 >= 0 and l2 >= 0:
                if s[l1] == string[l2]:
                    l1 -= 1
                    l2 -= 1
                else:
                    l1 -= 1
            if l2 == -1:
                if len(ans) < len(string) or (len(ans) == len(string) and string < ans):
                    ans = string
        return ans


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
