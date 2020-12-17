# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-04-10 16:38:09
# LastEditTime: 2020-04-10 16:54:57
# LastEditors: ssdcxy
# Description: 摆动排序 II
# FilePath: /arithmetic_oj/LeetCode/P0324.py

import json
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort(reverse=True)
        mid = len(nums) // 2
        nums[0::2], nums[1::2] = nums[:mid], nums[mid:]

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
            
            ret = Solution().wiggleSort(nums)

            out = integerListToString(nums)
            if ret is not None:
                print "Do not return anything, modify nums in-place instead."
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()