# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-07 23:13:14
# LastEditTime: 2020-12-22 11:06:44
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
        p1, p2 = m-1, n-1
        cur = (m + n) - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[cur] = nums1[p1]
                p1 -= 1
            else:
                nums1[cur] = nums2[p2]
                p2 -= 1
            cur -= 1
        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1


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
