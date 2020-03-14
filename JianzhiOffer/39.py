# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 15:44:51
# LastEditTime: 2020-03-11 15:52:36
# LastEditors: ssdcxy
# Description: 数组中出现次数超过一半的数字
# FilePath: /arithmetic_oj/JianzhiOffer/39.py

import json
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if x == num else -1
        return x
            

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