# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 21:28:31
# LastEditTime: 2020-02-20 22:29:30
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0303.py

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        size = len(nums)
        self.dp = [0] * (size + 1)
        self.dp[1] = nums[0]
        for i in range(2, size+1):
            self.dp[i]=nums[i-1]+self.dp[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]

obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,2))
print(obj.sumRange(2,5))
print(obj.sumRange(0,5))