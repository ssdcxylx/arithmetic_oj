# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-21 10:49:28
# LastEditTime: 2020-02-21 11:43:42
# LastEditors: ssdcxy
# Description: 摆动序列
# FilePath: /arithmetic_oj/LeetCode/P0376.py

import json
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)
        

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
            nums = stringToIntegerList(line)
            ret = Solution().wiggleMaxLength(nums)
            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()