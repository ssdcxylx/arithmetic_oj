# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-05 11:17:24
# LastEditTime: 2020-03-05 11:18:40
# LastEditors: ssdcxy
# Description: 只出现一次的数字
# FilePath: /arithmetic_oj/LeetCode/P0136.py

from typing import List
import json

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums: res ^= num
        return res

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
            
            ret = Solution().singleNumber(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()