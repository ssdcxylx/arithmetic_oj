# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-18 20:35:40
# LastEditTime: 2019-12-18 23:05:23
# LastEditors: ssdcxy
# Description: 有序数组的单一元素
# FilePath: /arithmetic_oj/LeetCode/P0540.py

from typing import List
import json


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = int(left + (right - right) / 2)
            flag = (right - left) % 2 == 0
            if nums[mid + 1] == nums[mid]:
                if flag:
                    left = mid + 2
                else:
                    right = mid - 1
            elif nums[mid-1] == nums[mid]:
                if flag:
                    right = mid - 2
                else:
                    right = mid + 1
            else:
                return nums[mid]
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

            ret = Solution().singleNonDuplicate(nums)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
