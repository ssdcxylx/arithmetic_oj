# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 21:18:51
# LastEditTime: 2020-02-22 21:26:46
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0169.py

import json
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, major = 0, nums[0]
        for num in nums:
            major = num if cnt == 0 else major
            cnt = cnt + 1 if major == num else cnt - 1
        return major

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
            
            ret = Solution().majorityElement(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()