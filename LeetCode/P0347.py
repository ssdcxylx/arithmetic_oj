# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-08 22:37:55
# LastEditTime: 2019-12-10 20:25:47
# LastEditors: ssdcxy
# Description: 前 K 个高频元素
# FilePath: /arithmetic_oj/LeetCode/P0347.py


from typing import List
import json
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n = len(nums)
        # lst = [None for i in range(n)]
        # res = []
        # for i in set(nums):
        #     _c = nums.count(i)
        #     if lst[_c-1] is None:
        #         lst[_c-1] = [i]
        #     else:
        #         lst[_c-1].append(i)
        # for i in range(len(lst) - 1, -1, -1):
        #     if lst[i] is not None:
        #         res.extend(lst[i])
        # return res[:k]
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


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
            k = int(line)

            ret = Solution().topKFrequent(nums, k)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
