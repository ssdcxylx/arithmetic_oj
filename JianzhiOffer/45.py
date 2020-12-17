# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 21:15:57
# LastEditTime: 2020-12-06 11:07:07
# LastEditors: ssdcxy
# Description: 把数组排成最小的数
# FilePath: /arithmetic_oj/JianzhiOffer/45.py

import json
from typing import List

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        if not nums: return ""
        n = len(nums)
        for i in range(n):
            nums[i] = str(nums[i])
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return "".join(nums)


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
            
            ret = Solution().minNumber(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()