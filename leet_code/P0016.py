# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-19 08:39:28
# LastEditTime: 2020-03-19 09:17:08
# LastEditors: ssdcxy
# Description: 最接近的三数之和
# FilePath: /arithmetic_oj/LeetCode/P0016.py

import json
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums: return 
        ans = 0
        delta = float('inf')
        n = len(nums)
        nums = sorted(nums)
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                cur = val - target
                if cur < 0:
                    if abs(cur) < delta:
                        ans = val
                        delta = abs(cur)
                    left += 1
                elif cur > 0:
                    if abs(cur) < delta:
                        ans = val
                        delta = abs(cur)
                    right -= 1
                else:
                    return target
        return ans
            
            
                

        
        

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
            
            ret = Solution().threeSumClosest(nums, target)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()