# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-09 20:41:22
# LastEditTime: 2019-12-10 20:29:56
# LastEditors: ssdcxy
# Description: 分发饼干
# FilePath: /arithmetic_oj/LeetCode/P0455.py


import json
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        m, n = len(g), len(s)
        res = 0
        j = m - 1
        for i in range(n-1, -1, -1):
            while j >= 0 and g[j] > s[i]:
                j -= 1
            if j >= 0:
                j -= 1
                res += 1
        return res


def stringToIntegerList(input):
    return json.loads(input)


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
            g = stringToIntegerList(line)
            line = next(lines)
            s = stringToIntegerList(line)

            ret = Solution().findContentChildren(g, s)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
