# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-10 23:33:10
# LastEditTime: 2019-12-11 01:18:41
# LastEditors: ssdcxy
# Description: 最大子序和
# FilePath: /arithmetic_oj/LeetCode/P0053.py

import json
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -float('inf')
        temp = 0
        for num in nums:
            if temp > 0:
                temp += num
            else:
                temp = num
            if temp > result:
                result = temp
        return result


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

            ret = Solution().maxSubArray(nums)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
