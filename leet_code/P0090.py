# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 10:12:52
# LastEditTime: 2020-02-20 10:21:27
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0090.py


import json
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, tmp):
            if tmp not in res:
                res.append(tmp)
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]: continue
                backtrack(j + 1, tmp + [nums[j]])
        res = []
        n = len(nums)
        nums.sort()
        backtrack(0, [])
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
            
            ret = Solution().subsetsWithDup(nums)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()