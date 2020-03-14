# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-07 10:10:32
# LastEditTime: 2020-03-07 11:16:14
# LastEditors: ssdcxy
# Description: 寻找重复数
# FilePath: /arithmetic_oj/LeetCode/P0287.py

import json
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        finder = 0
        while slow != finder:
            slow = nums[slow]
            finder = nums[finder]
        return slow

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
            nums = stringToIntegerList(line);
            
            ret = Solution().findDuplicate(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()