# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-19 10:26:44
# LastEditTime: 2020-03-19 11:09:00
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0026.py

import json
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        pre, cur = 0, 1
        n = len(nums)
        while cur < n:
            if nums[cur] != nums[pre]:
                if cur - pre > 1:
                    nums[pre] = nums[cur]
                pre += 1
            cur += 1
        return pre + 1

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
            
            ret = Solution().removeDuplicates(nums)

            out = integerListToString(nums, len_of_list=ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()