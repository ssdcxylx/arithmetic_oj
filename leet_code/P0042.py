# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-12 21:26:39
# LastEditTime: 2021-01-13 13:21:23
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0042.py

import json
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0] * n, [0] * n
        stack = list()
        ans = 0
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                stack.pop()
            left[i] = stack[0] if stack else -1
            stack.append(i)
        stack = list()
        for i in range(n-1, -1, -1):
            while stack and height[i] > height[stack[-1]]:
                stack.pop()
            right[i] = stack[0] if stack else n
            stack.append(i)
        ans = 0
        for i in range(n):
            if left[i] != -1 and right[i] != n:
                mn = min(height[left[i]], height[right[i]])
                ans += (mn - height[i])
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
            
            ret = Solution().trap(height)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()