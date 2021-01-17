# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-09 20:41:22
# LastEditTime: 2021-01-01 12:06:33
# LastEditors: ssdcxy
# Description: 分发饼干
# FilePath: /arithmetic_oj/LeetCode/P0455.py


import json
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g: return 0
        if not s: return 0
        g.sort()
        s.sort()
        m, n = len(g), len(s)
        ans = 0
        i, j = 0, 0
        while i < m and j < n:
            if g[i] <= s[j]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1
        return ans


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
