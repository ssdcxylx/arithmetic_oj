# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-21 11:50:55
# LastEditTime: 2020-02-21 12:00:24
# LastEditors: ssdcxy
# Description: 分割等和子集
# FilePath: /arithmetic_oj/LeetCode/P0416.py

import json
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = 0
        for num in nums:
            _sum += num
        if _sum % 2 != 0:
            return False
        W = (_sum-1)//2 + 1
        dp = [False] * (W+1)
        dp[0] = True
        for num in nums:
            for i in range(W, num-1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[W]

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
            
            ret = Solution().canPartition(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()