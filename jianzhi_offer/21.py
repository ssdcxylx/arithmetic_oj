# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 11:45:00
# LastEditTime: 2020-03-10 12:04:02
# LastEditors: ssdcxy
# Description: 调整数组顺序使奇数位于偶数前面
# FilePath: /arithmetic_oj/JianzhiOffer/21.py


import json
from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            while left < right and nums[left] & 1:
                left += 1
            while left < right and not nums[right] & 1:
                right += 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums


                


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
            
            ret = Solution().exchange(nums)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()