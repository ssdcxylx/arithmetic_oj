# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-08 23:34:35
# LastEditTime: 2019-12-10 20:16:34
# LastEditors: ssdcxy
# Description: 颜色分类
# FilePath: /arithmetic_oj/LeetCode/P0075.py


import json
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            j = i
            while nums[j-1] > nums[j] and j - 1 >= 0:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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

            ret = Solution().sortColors(nums)

            out = integerListToString(nums)
            if ret is not None:
                print
                "Do not return anything, modify nums in-place instead."
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
