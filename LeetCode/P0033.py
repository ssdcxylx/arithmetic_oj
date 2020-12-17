# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-19 11:09:25
# LastEditTime: 2020-03-19 15:23:33
# LastEditors: ssdcxy
# Description: 搜索旋转排序数组
# FilePath: /arithmetic_oj/LeetCode/P0033.py

import json
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binsearch(l, r):
            nonlocal target
            if l > r: return -1
            mid = (l + r) >> 1
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binsearch(l, mid-1)
            else:
                return binsearch(mid+1, r)
        if not nums: return -1
        mid = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                mid = i
            else:
                break
        if target == nums[0]:
            return 0
        elif target > nums[0]:
            return binsearch(0, mid)
        else:
            return binsearch(mid+1, n-1)
            

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
            target = int(line);
            
            ret = Solution().search(nums, target)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()