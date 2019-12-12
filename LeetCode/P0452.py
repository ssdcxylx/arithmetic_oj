# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-09 21:22:57
# LastEditTime: 2019-12-10 20:29:42
# LastEditors: ssdcxy
# Description: 用最少数量的箭引爆气球
# FilePath: /arithmetic_oj/LeetCode/P0452.py


import json
from typing import List


class Solution(object):
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda i: i[-1])
        n = len(points) - 1
        res = 0
        while n >= 0:
            start, end = points[n][0], points[n][1]
            count = 0
            while n - count - 1 >= 0 and start <= points[n-count-1][1] <= end:
                start = points[n-count -
                               1][0] if start < points[n-count-1][0] else start
                end = points[n-count-1][1] if end > points[n -
                                                           count-1][1] else end
                count += 1
            n -= 1
            n -= count
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
            points = stringToInt2dArray(line)

            ret = Solution().findMinArrowShots(points)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
