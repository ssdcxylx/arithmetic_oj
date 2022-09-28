# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-21 12:11:24
# LastEditTime: 2020-02-21 14:38:57
# LastEditors: ssdcxy
# Description: 目标和
# FilePath: /arithmetic_oj/LeetCode/P0494.py

import json
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n, dp = len(nums), {(0, 0): 1}
        for i in range(1, n+1):
            for j in range(-sum(nums), sum(nums)+1):
                dp[(i,j)] = dp.get((i-1, j-nums[i-1]), 0) + dp.get((i-1, j + nums[i-1]), 0)
        return dp.get((n, S), 0)

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
            S = int(line);
            
            ret = Solution().findTargetSumWays(nums, S)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()