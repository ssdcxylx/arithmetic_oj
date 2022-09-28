# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-01 11:42:37
# LastEditTime: 2021-01-12 21:33:05
# LastEditors: ssdcxy
# Description: 最大矩形
# FilePath: /arithmetic_oj/LeetCode/P0085.py

import json
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights):
            n = len(heights)
            left, right = [0] * n, [n] * n
            stack = list()
            for i in range(n):
                while stack and heights[stack[-1]] > heights[i]:
                    right[stack[-1]] = i
                    stack.pop()
                left[i] = stack[-1] if stack else - 1
                stack.append(i)
            area = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n else 0
            return area
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        all_heights = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    all_heights[i][j] = all_heights[i-1][j] + 1
        ans = max(largestRectangleArea(all_heights[i]) for i in range(rows))
        return ans

def stringToChar2dArray(input):
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
            line = lines.next()
            matrix = stringToChar2dArray(line)
            
            ret = Solution().maximalRectangle(matrix)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()