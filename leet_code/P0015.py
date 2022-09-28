# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-19 08:12:30
# LastEditTime: 2020-03-19 08:37:07
# LastEditors: ssdcxy
# Description: 三数之和
# FilePath: /arithmetic_oj/LeetCode/P0015.py

import json
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []
        n = len(nums)
        nums = sorted(nums)
        res = []
        cur = 0
        while cur < n:
            if nums[cur] > 0: 
                cur += 1
                break
            if cur > 0 and nums[cur] == nums[cur-1]:
                cur += 1
                continue
            left, right = cur + 1, n-1
            while left < right:
                val = nums[cur] + nums[left] + nums[right]
                if val < 0:
                    left += 1
                elif val > 0:
                    right -= 1
                else:
                    res.append([nums[cur], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
            cur += 1
        return res



def stringToIntegerList(input):
    return json.loads(input)

def int2dArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)
            
            ret = Solution().threeSum(nums)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()