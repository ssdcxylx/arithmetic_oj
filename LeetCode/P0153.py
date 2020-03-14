# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-19 21:36:14
# LastEditTime: 2019-12-20 22:53:09
# LastEditors: ssdcxy
# Description:寻找旋转排序数组中的最小值
# FilePath: /arithmetic_oj/LeetCode/P0153.py

from typing import List
import json


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        left, right = 0, n - 1
        while left < right:
            mid = int(left + (right - left)/2)
            if nums[left] > nums[mid]:
                right = mid
            elif nums[right] < nums[mid]:
                left = mid + 1
            else:
                return nums[left]
        return nums[left]


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

            ret = Solution().findMin(nums)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
