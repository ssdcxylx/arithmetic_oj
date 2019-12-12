# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-07 23:13:14
# LastEditTime: 2019-12-10 20:17:05
# LastEditors: ssdcxy
# Description: 合并两个有序数组
# FilePath: /arithmetic_oj/LeetCode/P0088.py


import json
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        bias = 0
        while i < m + bias and j < n:
            if nums1[i-bias+j] <= nums2[j]:
                i += 1
            else:
                nums1[i+1:] = nums1[i:n+m-1]
                nums1[i-bias+j] = nums2[j]
                i += 1
                bias += 1
                j += 1
        if j < n:
            nums1[i-bias+j:] = nums2[j:]


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
            nums1 = stringToIntegerList(line)
            line = next(lines)
            m = int(line)
            line = next(lines)
            nums2 = stringToIntegerList(line)
            line = next(lines)
            n = int(line)

            ret = Solution().merge(nums1, m, nums2, n)

            out = integerListToString(nums1)
            if ret is not None:
                print
                "Do not return anything, modify nums1 in-place instead."
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
