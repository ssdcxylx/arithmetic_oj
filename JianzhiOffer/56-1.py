# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 11:15:53
# LastEditTime: 2020-03-12 11:53:39
# LastEditors: ssdcxy
# Description: 数组中数字出现的次数
# FilePath: /arithmetic_oj/JianzhiOffer/56-1.py

import json
from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num
        diff &= -diff
        res = [0, 0]
        for num in nums:
            if (num&diff) == 0: res[0] ^= num
            else: res[1] ^= num
        return res


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
            
            ret = Solution().singleNumbers(nums)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()