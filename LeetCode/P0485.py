# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-07 08:36:37
# LastEditTime: 2020-03-07 08:41:28
# LastEditors: ssdcxy
# Description: 最大连续1的个数
# FilePath: /arithmetic_oj/LeetCode/P0485.py

import json
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        _max = 0
        cur = 0
        for num in nums:
            cur = cur + 1 if num == 1 else 0
            if cur > _max:
                _max = cur
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
            
            ret = Solution().findMaxConsecutiveOnes(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()