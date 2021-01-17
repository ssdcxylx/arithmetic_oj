# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-09 20:57:52
# LastEditTime: 2020-12-31 20:35:22
# LastEditors: ssdcxy
# Description: 无重叠区间
# FilePath: /arithmetic_oj/LeetCode/P0435.py


from typing import List
import json


class Solution(object):
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1: return 0
        intervals.sort()
        ans = 0
        p1, p2 = n-2, n-1
        while p1 >= 0:
            if intervals[p1][1] <= intervals[p2][0]:
                p2 = p1
                p1 -= 1
            else:
                p1 -= 1
                ans += 1
        return ans


def stringToInt2dArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            intervals = stringToInt2dArray(line)

            ret = Solution().eraseOverlapIntervals(intervals)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
