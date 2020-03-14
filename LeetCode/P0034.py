# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-19 22:15:36
# LastEditTime: 2019-12-19 22:56:52
# LastEditors: ssdcxy
# Description: 在排序数组中查找元素的第一个和最后一个位置
# FilePath: /arithmetic_oj/LeetCode/P0034.py

from typing import List
import json


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left, right = 0, n - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if left > right:
            return [-1, -1]
        left, right = mid, mid
        while left > 0 and nums[left-1] == target:
            left -= 1
        while right < n - 1 and nums[right+1] == target:
            right += 1
        return [left, right]


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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
            line = next(lines)
            target = int(line)

            ret = Solution().searchRange(nums, target)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
