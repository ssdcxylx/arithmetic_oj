# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 13:55:06
# LastEditTime: 2020-12-11 11:31:35
# LastEditors: ssdcxy
# Description: 和为s的两个数字
# FilePath: /arithmetic_oj/JianzhiOffer/57.py

import json
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            s = nums[left] + nums[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return [nums[left], nums[right]]

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
            nums = stringToIntegerList(line);
            line = next(lines)
            target = int(line);
            
            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()