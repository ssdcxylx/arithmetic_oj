# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-04-10 17:34:36
# LastEditTime: 2020-04-10 17:50:15
# LastEditors: ssdcxy
# Description: 旋转数组
# FilePath: /arithmetic_oj/LeetCode/P0189.py

import json
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l = l + 1
                r = r - 1
        n = len(nums)
        k = k % n
        swap(0, n-k-1)
        swap(n-k, n-1)
        swap(0, n-1)

        

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
            line = next(lines)
            k = int(line);
            
            ret = Solution().rotate(nums, k)

            out = integerListToString(nums)
            if ret is not None:
                print "Do not return anything, modify nums in-place instead."
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()