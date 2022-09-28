# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-16 07:25:09
# LastEditTime: 2020-03-16 08:06:12
# LastEditors: ssdcxy
# Description: 盛最多水的容器
# FilePath: /arithmetic_oj/LeetCode/P0011.py

import json
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        ans = 0
        while i < j:
            if height[i] < height[j]:
                ans = max(ans, height[i] * (j-i))
                i += 1
            else:
                ans = max(ans, height[j] * (j-i))
                j -= 1
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
            height = stringToIntegerList(line);
            
            ret = Solution().maxArea(height)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()