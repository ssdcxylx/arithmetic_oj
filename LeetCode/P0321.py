# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-19 10:23:38
# LastEditTime: 2020-12-20 09:17:00
# LastEditors: ssdcxy
# Description: 拼接最大
# FilePath: /arithmetic_oj/LeetCode/P0321.py

import json
from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]
        def merge(A, B):
            res = []
            while A or B:
                mx = max(A, B)
                res.append(mx.pop(0))
            return res
        return max(merge(pick_max(nums1, i), pick_max(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))

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
            nums1 = stringToIntegerList(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);
            line = next(lines)
            k = int(line);
            
            ret = Solution().maxNumber(nums1, nums2, k)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()