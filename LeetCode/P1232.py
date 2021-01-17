# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-17 09:33:04
# LastEditTime: 2021-01-17 09:37:08
# LastEditors: ssdcxy
# Description:  缀点成线
# FilePath: /arithmetic_oj/LeetCode/P1232.py

import json
from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        deltaX, deltaY = coordinates[0][0], coordinates[0][1]
        n = len(coordinates)
        for i in range(n):
            coordinates[i][0] -= deltaX
            coordinates[i][1] -= deltaY
        a, b = coordinates[1][1], coordinates[1][0]
        for i in range(2, n):
            x, y = coordinates[i][0], coordinates[i][1]
            if a * x != b * y:
                return False
        return True

def stringToInt2dArray(input):
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
            coordinates = stringToInt2dArray(line)
            
            ret = Solution().checkStraightLine(coordinates)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()