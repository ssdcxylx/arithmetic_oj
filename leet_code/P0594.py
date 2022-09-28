# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-03 10:31:00
# LastEditTime: 2020-03-03 10:45:55
# LastEditors: ssdcxy
# Description: 最长和谐子序列
# FilePath: /arithmetic_oj/LeetCode/P0594.py

from typing import List
import json

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        _dict = dict()
        for num in nums:
            _dict[num] = _dict.get(num, 0) + 1
        _max = 0
        for k in _dict.keys():
            if _dict.__contains__(k+1):
                _max = max(_max, _dict.get(k+1, 0) + _dict.get(k, 0))
        return _max
            

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
            
            ret = Solution().findLHS(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()