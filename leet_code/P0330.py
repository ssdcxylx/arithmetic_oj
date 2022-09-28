# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-01 09:59:14
# LastEditTime: 2021-01-01 10:01:43
# LastEditors: ssdcxy
# Description:  按要求补齐数组
# FilePath: /arithmetic_oj/LeetCode/P0330.py

import json
from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, x = 0, 1
        length, index = len(nums), 0
        
        while x <= n:
            if index < length and nums[index] <= x:
                x += nums[index]
                index += 1
            else:
                x <<= 1
                patches += 1
        return patches

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
            line = next(lines)
            n = int(line);
            
            ret = Solution().minPatches(nums, n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()