# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-09 20:57:52
# LastEditTime: 2019-12-10 20:26:28
# LastEditors: ssdcxy
# Description: 无重叠区间
# FilePath: /arithmetic_oj/LeetCode/P0435.py


from typing import List
import json


class Solution(object):
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda i: i[-1])
        n = len(intervals)
        i = 0
        res = 0
        while i + 1 < n:
            if intervals[i][-1] <= intervals[i+1][0]:
                i += 1
            else:
                intervals[i + 1] = intervals[i]
                i += 1
                res += 1
        return res


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
