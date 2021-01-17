# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-10 08:48:45
# LastEditTime: 2021-01-10 08:54:41
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0228.py

import json
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        n = len(nums)
        cur = 0
        res = []
        while cur < n:
            if cur + 1 < n and nums[cur] + 1 == nums[cur+1]:
                prev = cur
                while cur + 1 < n and nums[cur] + 1 == nums[cur+1]:
                    cur += 1
                res.append("{}->{}".format(nums[prev], nums[cur]))
            else:
                res.append(str(nums[cur]))
            cur += 1
        return res
        

def stringToIntegerList(input):
    return json.loads(input)

def stringArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)
            
            ret = Solution().summaryRanges(nums)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()