# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 09:22:54
# LastEditTime: 2020-03-25 09:09:12
# LastEditors: ssdcxy
# Description: 全排列
# FilePath: /arithmetic_oj/LeetCode/P0046.py

import json
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(tmp):
            nonlocal n
            if len(tmp) == n:
                res.append(tmp)
                return
            for j in range(n):
                if nums[j] in tmp:
                    continue
                backtrack(tmp+[nums[j]])
        n = len(nums)
        res = []
        backtrack([])
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
            
            ret = Solution().permute(nums)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()