# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-21 09:14:00
# LastEditTime: 2020-02-21 09:48:14
# LastEditors: ssdcxy
# Description: 最长上升子序列
# FilePath: /arithmetic_oj/LeetCode/P0300.py

import json
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        res = 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if dp[m] < num: i = m + 1
                else: j = m
            dp[i] = num
            if j == res: res += 1
        return res

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
            
            ret = Solution().lengthOfLIS(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()