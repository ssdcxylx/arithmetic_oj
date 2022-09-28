# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 20:21:22
# LastEditTime: 2020-02-20 20:30:21
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0213.py

import json
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            a, b = 0, 0
            for num in nums:
                cur = max(a + num, b)
                a, b = b, cur
            return bb
        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]

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
            
            ret = Solution().rob(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()