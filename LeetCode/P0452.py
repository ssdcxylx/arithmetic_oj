# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-09 21:22:57
# LastEditTime: 2020-11-23 19:22:50
# LastEditors: ssdcxy
# Description: 用最少数量的箭引爆气球
# FilePath: /arithmetic_oj/LeetCode/P0452.py


import json
from typing import List


class Solution(object):
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(lambda point: point[1])
        pos = points[0][1]
        ans = 1
        for point in points:
            if point[0] > pos:
                pos = point[1]
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
            points = stringToInt2dArray(line)

            ret = Solution().findMinArrowShots(points)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
