# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 07:43:14
# LastEditTime: 2020-02-20 08:25:41
# LastEditors: ssdcxy
# Description: 子集
# FilePath: /arithmetic_oj/LeetCode/P0078.py

import json
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                backtrack(j + 1, tmp + [nums[j]])
        res = []
        n = len(nums)
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
            
            ret = Solution().subsets(nums)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()