# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-21 13:41:27
# LastEditTime: 2020-03-21 13:46:59
# LastEditors: ssdcxy
# Description: 加一
# FilePath: /arithmetic_oj/LeetCode/P0066.py

import json
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1
        flag = 1
        while i >= 0 and flag:
            val = digits[i] + flag
            if val == 10:
                digits[i] = 0
                flag = True
            else:
                digits[i] = val
                return digits
        return digits
            

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
            digits = stringToIntegerList(line);
            
            ret = Solution().plusOne(digits)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()