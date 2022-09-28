# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 20:17:52
# LastEditTime: 2020-02-22 21:11:49
# LastEditors: ssdcxy
# Description: 最少移动次数使数组元素相等 II
# FilePath: /arithmetic_oj/LeetCode/P0462.py

import json
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # nums.sort()
        # l, h = 0, len(nums) - 1
        # move = 0
        # while l <= h:
        #     move += nums[h] - nums[l]
        #     l += 1
        #     h -= 1
        # return move
        
        def findK(k):
            l, h = 0, len(nums) - 1
            while l < h:
                j = partition(l, h)
                if j == k:
                    break
                if j < k:
                    l = j + 1
                if j > k:
                    h = j - 1
            return nums[k]
        def partition(l, h):
            i, j = l, h
            while i < j:
                while i < j and nums[j] <= nums[l]:
                    j -= 1
                while i < j and nums[i] >= nums[l]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[j] = nums[j], nums[l]
            return j
        move = 0
        median = findK(len(nums)//2)
        for num in nums:
            move += abs(num - median)
        return move
            


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
            
            ret = Solution().minMoves2(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()