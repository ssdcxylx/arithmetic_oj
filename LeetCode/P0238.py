# -*- coding: utf-8 -*-
# @time       : 2019-10-24 22:54
# @author     : ssdcxy
# @email      : 18379190862@163.com
# @file       : P0238.py
# @description: 除自身意外数组的乘积

from typing import List
import json


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, l, r = [1 for _ in range(len(nums))], 1, 1
        for i, j in zip(range(len(nums)), range(len(nums)-1, -1, -1)):
            res[i] *= l
            res[j] *= r
            l *= nums[i]
            r *= nums[j]
        return res


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
            nums = stringToIntegerList(line);

            ret = Solution().productExceptSelf(nums)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()