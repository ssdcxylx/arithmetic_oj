# -*- coding: utf-8 -*-
# @time       : 2019-10-16 22:32
# @author     : ssdcxy
# @email      : 18379190862@163.com
# @file       : P0004.py
# @description: 寻找两个有序数组的中位数

from typing import List
import json


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        nums3 = []
        index1, index2 = 0, 0
        while index1 < l1 and index2 < l2:
            if nums1[index1] <= nums2[index2]:
                nums3.append(nums1[index1])
                index1 += 1
            else:
                nums3.append(nums2[index2])
                index2 += 1
        if index1 < l1:
            nums3 += nums1[index1:]
        if index2 < l2:
            nums3 += nums2[index2:]
        l3 = len(nums3)
        if l3 % 2 == 0:
            return (nums3[int(l3/2)-1] + nums3[int(l3/2)])/2
        else:
            return nums3[int(l3/2)]


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
            nums1 = stringToIntegerList(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);

            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
