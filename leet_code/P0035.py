# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-12 20:59:46
# LastEditTime: 2021-01-12 21:00:01
# LastEditors: ssdcxy
# Description: 搜索插入位置
# FilePath: /arithmetic_oj/LeetCode/P0035.py

from typing import List
import json

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        n = len(nums)
        if nums[0] >= target: return 0
        for i in range(1, n):
            if nums[i] == target:
                return i
            elif nums[i] > target and nums[i-1] < target:
                return i
        return n

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
            
            ret = Solution().searchInsert(nums, target)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()