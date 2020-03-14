# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-18 20:07:51
# LastEditTime: 2019-12-18 20:30:41
# LastEditors: ssdcxy
# Description:
# FilePath: /arithmetic_oj/LeetCode/P0074.py

from typing import List
import json


class Solution(object):
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n - 1
        while left <= right:
            m = int(left + (right - left) / 2)
            if letters[m] > target and letters[m-1] <= target:
                return letters[m]
            elif letters[m] <= target:
                left = m + 1
            else:
                right = m - 1
        return letters[0]


def stringToCharArray(input):
    return json.loads(input)


def stringToChar(line):
    if not line:
        return ''
    c = line[0]
    if len(line) == 1:
        line = '"%s"' % c
    elif len(line) == 2 and c == '\\':
        c = line[1]
        line = '"\\%s"' % c
    return json.loads(line)


def charToString(c):
    return json.dumps(c)


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            letters = stringToCharArray(line)
            line = next(lines)
            target = stringToChar(line)

            ret = Solution().nextGreatestLetter(letters, target)

            out = charToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
