# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-21 10:29:24
# LastEditTime: 2020-12-21 10:30:30
# LastEditors: ssdcxy
# Description: 两数之和 II - 输入有序数组
# FilePath: /arithmetic_oj/LeetCode/P0167.py

import json

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            sum1 = numbers[left] + numbers[right]
            if sum1 < target:
                left += 1
            elif sum1 > target:
                right -= 1
            else:
                return [left+1, right+1]
        return [0, 0]

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
            numbers = stringToIntegerList(line);
            line = next(lines)
            target = int(line);
            
            ret = Solution().twoSum(numbers, target)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()