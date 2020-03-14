# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-07 09:48:09
# LastEditTime: 2020-03-07 10:07:27
# LastEditors: ssdcxy
# Description: 错误的集合   
# FilePath: /arithmetic_oj/LeetCode/P0645.py

import json
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            while nums[i] != i + 1 and nums[nums[i]-1] != nums[i]:
                flag = nums[i]-1
                nums[i], nums[flag] = nums[flag], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i+1]

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
            
            ret = Solution().findErrorNums(nums)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()