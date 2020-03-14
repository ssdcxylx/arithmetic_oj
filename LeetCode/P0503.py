# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-03 10:04:00
# LastEditTime: 2020-03-03 10:19:12
# LastEditors: ssdcxy
# Description: 下一个更大元素 II
# FilePath: /arithmetic_oj/LeetCode/P503.py

from typing import List
import json

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1 for _ in range(n)]
        stack = list()
        for i in range(2*n):
            num = nums[i%n]
            while stack and num > nums[stack[-1]]:
                res[stack.pop()] = num
            if i < n:
                stack.append(i)
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
            
            ret = Solution().nextGreaterElements(nums)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()