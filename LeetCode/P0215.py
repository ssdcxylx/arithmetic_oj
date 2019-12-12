# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-08 21:31:19
# LastEditTime: 2019-12-10 20:22:54
# LastEditors: ssdcxy
# Description: 数组中的第K个最大元素
# FilePath: /arithmetic_oj/LeetCode/P0215.py


import json
from typing import List
from random import randint


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = randint(0, len(nums) - 1)
        pivot = nums[index]
        left = [i for i in nums[:index] + nums[index+1:] if i > pivot]
        right = [i for i in nums[:index] + nums[index+1:] if i <= pivot]
        _k = len(left)
        if _k == k - 1:
            return pivot
        elif _k > k - 1:
            return self.findKthLargest(left, k)
        else:
            return self.findKthLargest(right, k - _k - 1)


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
            nums = stringToIntegerList(line)
            line = next(lines)
            k = int(line)

            ret = Solution().findKthLargest(nums, k)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
