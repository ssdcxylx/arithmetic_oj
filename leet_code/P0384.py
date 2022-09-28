# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-04-10 17:01:28
# LastEditTime: 2020-04-10 17:29:35
# LastEditors: ssdcxy
# Description: 打乱数组
# FilePath: /arithmetic_oj/LeetCode/P0384.py

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()