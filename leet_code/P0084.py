# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-01 11:07:19
# LastEditTime: 2021-01-01 11:47:30
# LastEditors: ssdcxy
# Description: 柱状图中最大的矩形
# FilePath: /arithmetic_oj/LeetCode/P0084.py

import json
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n
        stack = list()
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
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
            heights = stringToIntegerList(line);
            
            ret = Solution().largestRectangleArea(heights)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()