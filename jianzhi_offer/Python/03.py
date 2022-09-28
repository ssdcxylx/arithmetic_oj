# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-09 21:15:33
# LastEditTime: 2020-03-09 21:28:30
# LastEditors: ssdcxy
# Description: 数组中重复的数字   
# FilePath: /arithmetic_oj/JianzhiOffer/03.py

import json
from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                else:
                    tmp = nums[i]
                    nums[tmp], nums[i] = nums[i], nums[tmp]


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
            
            ret = Solution().findRepeatNumber(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()