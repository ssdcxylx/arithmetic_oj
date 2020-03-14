# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 14:09:17
# LastEditTime: 2020-03-12 14:17:56
# LastEditors: ssdcxy
# Description: 滑动窗口的最大值
# FilePath: /arithmetic_oj/JianzhiOffer/59-1.py

import json
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        if k == 1: return nums
        res = [max(nums[:k])]
        for i in range(len(nums) - k):
            if nums[k+i] > res[-1]:
                res.append(nums[i+k])
            else:
                if nums[i] == res[-1]:
                    res.append(max(nums[i+1:k+i+1]))
                else:
                    res.append(res[-1])
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
            line = next(lines)
            k = int(line);
            
            ret = Solution().maxSlidingWindow(nums, k)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()