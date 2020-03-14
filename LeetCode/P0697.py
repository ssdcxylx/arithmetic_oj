# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-07 11:44:09
# LastEditTime: 2020-03-07 12:01:41
# LastEditors: ssdcxy
# Description: 数组的度
# FilePath: /arithmetic_oj/LeetCode/P0697.py

import json
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        _dict = {}
        first = {}
        last = {}
        n = len(nums)
        for i in range(n):
            val = _dict.get(nums[i], -1)
            if val == -1:
                _dict[nums[i]] = 1
                first[nums[i]] = i
                last[nums[i]] = i
            else:
                _dict[nums[i]] = val + 1
                last[nums[i]] = i
        _max, res = 0, n
        for key, val in _dict.items():
            count = last.get(key, -1) - first.get(key, -1) + 1
            if val > _max or (val == _max and count < res):
                _max = val
                res = count
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
            
            ret = Solution().findShortestSubArray(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()