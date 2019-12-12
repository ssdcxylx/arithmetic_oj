# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-16 09:24:27
# LastEditTime: 2019-12-10 20:09:44
# LastEditors: ssdcxy
# Description: 两数之和
# FilePath: /arithmetic_oj/LeetCode/P0001.py

from typing import List
import json


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            if num in nums_dict:
                return [nums_dict[num], i]
            else:
                nums_dict[target - num] = i


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
            line = next(lines)
            target = int(line)

            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
