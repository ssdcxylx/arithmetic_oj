# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-12 20:52:00
# LastEditTime: 2021-01-12 20:52:17
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0027.py

import json
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count

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
            val = int(line);
            
            ret = Solution().removeElement(nums, val)

            out = integerListToString(nums, len_of_list=ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()