# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 20:10:45
# LastEditTime: 2020-03-02 10:22:46
# LastEditors: ssdcxy
# Description: 打家劫舍
# FilePath: /arithmetic_oj/LeetCode/P0198.py

import json
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for num in nums:
            cur = max(a+num, b)
            a, b = b, cur
        return b
            

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
            
            ret = Solution().rob(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()