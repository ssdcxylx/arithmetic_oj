# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-23 08:42:13
# LastEditTime: 2020-03-23 09:12:35
# LastEditors: ssdcxy
# Description: 四数之和
# FilePath: /arithmetic_oj/LeetCode/P0018.py

import json
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        p = 0
        while p < n - 3:
            if nums[p] + 3 * nums[p + 1] > target: break  
            if nums[p] + 3 * nums[-1] < target:           
                while p < n - 4 and nums[p] == nums[p + 1]: p += 1
                p += 1
                continue
            k = p + 1
            while k < n - 2:
                if nums[p] + nums[k] + 2 * nums[k + 1] > target: break
                if nums[p] + nums[k] + 2 * nums[-1] < target: 
                    while k < n - 3 and nums[k] == nums[k + 1]:
                        k += 1
                    k += 1
                    continue
                i = k + 1
                j = n - 1
                new_target = target - nums[p] - nums[k]
                while i < j:
                    if nums[i] + nums[j] > new_target: j -= 1
                    elif nums[i] + nums[j] < new_target: i += 1
                    else:
                        res.append([nums[p],nums[k],nums[i],nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i - 1]: i += 1
                        while i < j and nums[j] == nums[j + 1]: j -= 1
                while k < n - 3 and nums[k] == nums[k + 1]: k += 1
                k += 1
            while p < n - 4 and nums[p] == nums[p + 1]: p += 1
            p += 1
        return res


def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

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
            line = next(lines)
            target = stringToInt(line)
            
            ret = Solution().fourSum(nums, target)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()