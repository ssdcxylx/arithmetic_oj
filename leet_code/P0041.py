# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-21 11:02:50
# LastEditTime: 2020-03-21 11:53:05
# LastEditors: ssdcxy
# Description: 缺失的第一个正数
# FilePath: /arithmetic_oj/LeetCode/P0041.py

import json
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 not in nums:
            return 1
        if n == 1:
            return 2
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        for i in range(n):
            cur = abs(nums[i])
            if cur == n:
                nums[0] = -abs(nums[0])
            else:
                nums[cur] = -abs(nums[cur])
        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n + 1
        
        

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
            nums = stringToIntegerList(line);
            
            ret = Solution().firstMissingPositive(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()