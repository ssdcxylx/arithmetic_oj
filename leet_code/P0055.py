# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-22 10:58:34
# LastEditTime: 2020-03-22 11:18:23
# LastEditors: ssdcxy
# Description: 跳跃游戏
# FilePath: /arithmetic_oj/LeetCode/P0055.py

import json
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0
        for i, jump in enumerate(nums):
            if i <= max_i and i + jump > max_i:
                max_i = i + jump
        return max_i >= i
                


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
            
            ret = Solution().canJump(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()