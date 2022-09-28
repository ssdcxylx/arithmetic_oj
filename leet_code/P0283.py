# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-07 07:45:34
# LastEditTime: 2020-03-07 08:01:36
# LastEditors: ssdcxy
# Description: 移动零
# FilePath: /arithmetic_oj/LeetCode/P0283.py

import json
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        if n < 1: return
        flag = -1
        for i in range(n):
            if nums[i] == 0:
                flag = i
                break
        if flag < 0:
            return
        i = flag + 1
        while i < n:
            if nums[i] != 0:
                nums[flag], nums[i] = nums[i], nums[flag]
                flag += 1
            i += 1



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
            
            ret = Solution().moveZeroes(nums)

            out = integerListToString(nums)
            if ret is not None:
                print("Do not return anything, modify nums in-place instead.")
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()